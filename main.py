import asyncio
import logging

from handlers import *
from loader import bot, dp
from database import users, nodes, nodesUptime, votes
import utils
import text

import aiohttp


async def main():
    dp.include_router(settings_router)
    dp.include_router(start_router)
    dp.include_router(nodes_router)
    dp.include_router(network_router)
    dp.include_router(mailing_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

async def check_nodes():
    while True:
        for node in nodes:
            userID = node["userID"]
            userlang = users.get_user_settings(userID, "lang")
            if utils.check_rpc_node_format(node["ip"]): # ip or http
                nodeAlert = users.get_user_settings(userID, "nodeAlert")
                if not nodeAlert:
                    continue
                node_status = await utils.get_node_data(node["ip"], "status")
                if not node_status:
                    _text = text.get_nodeisnotavailable_text(userlang).format(ip=node["ip"])
                    await bot.send_message(chat_id=userID, text=_text)
                elif node_status['result']['sync_info']['catching_up']:
                    _text = text.get_nodeisnotcathingup_text(userlang).format(
                        ip=node["ip"], block=node_status["result"]["sync_info"]["latest_block_height"])
                    await bot.send_message(chat_id=userID, text=_text)

                state = await utils.check_rpc_address_exists(node["ip"])
                state = state['state'] if state else '?'
                last_node_state = nodes.get_node_state(node["ip"], userID)
                last_node_state = "?" if not last_node_state else last_node_state
                if last_node_state != state:
                    nodes.set_node_state(node["ip"], userID, state)
                    if users.get_user_settings(userID, "nodeAlert"):
                        try:
                            await bot.send_message(node["userID"], text=text.get_node_changed_state(userlang, node["ip"], last_node_state, state))
                        except:
                            continue

            else: # address
                state = await utils.check_rpc_address_exists(node["ip"])
                if not state:
                    try:
                        await bot.send_message(userID, text=text.get_node_addr_not_state(userlang, node["ip"]))
                    except:
                        pass
                    continue
                state = state['state']
                last_node_state = nodes.get_node_state(node["ip"], userID)
                last_node_state = "?" if not last_node_state else last_node_state
                if last_node_state != state:
                    nodes.set_node_state(node["ip"], userID, state)
                    if users.get_user_settings(userID, "nodeAlert"):
                        try:
                            await bot.send_message(node["userID"], text=text.get_node_changed_state(userlang, node["ip"], last_node_state, state))
                        except:
                            continue
        await asyncio.sleep(60)

async def update_addresses():
    while True:
        for network in ["namada-shielded-expedition-rpc.denodes.xyz"]: # only 1 network right now
            db_last_block_height = nodesUptime.get_last_block_height(network)
            if db_last_block_height:
                db_last_block_height = int(db_last_block_height["block_height"])
                status = await utils.get_node_data(network, "status")
                if not status:
                    continue
                last_block_height = int(status["result"]["sync_info"]["latest_block_height"])

                # (last_in_db; current]
                for height in range(db_last_block_height+1, last_block_height+1):
                    addressess = await utils.get_network_addresses(network, height)
                    nodesUptime.add_addresses(network, height, addressess)
            else:
                status = await utils.get_node_data(network, "status")
                if not status:
                    continue
                last_block_height = int(status["result"]["sync_info"]["latest_block_height"])

                addressess = await utils.get_network_addresses(network, last_block_height)
                nodesUptime.add_addresses(network, last_block_height, addressess)

        await asyncio.sleep(60)

async def cleanup_addressess():
    while True:
        nodesUptime.cleanup()
        await asyncio.sleep(60*60*24) # 1 day

async def check_epoch():
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://namada-indexer.kintsugi-nodes.com/proposals") as proposals:
                proposals = await proposals.json()

            async with session.get("https://namada-alt.denodes.xyz/epoch.json") as response:
                result = await response.json()
                current_epoch = int(result["epoch"])

        used_proposals = votes.get_all_votes()

        for proposal in proposals:
            if proposal['voting_start_epoch'] == current_epoch and proposal['id'] not in used_proposals:
                for user in users:
                    if not user["voteAlert"]:
                        continue
                    userlang = users.get_user_settings(user["userID"], "lang")
                    await bot.send_message(chat_id=user["userID"], text=text.get_vote_text(userlang, proposal))
                votes.add_vote(proposal['id'])


        # 10 minutes
        await asyncio.sleep(600)

async def uptime_alerts():
    last_uptimes = dict()
    while True:
        for node in nodes:
            userID = node["userID"]
            userLang = users.get_user_settings(userID, "lang")
            if not users.get_user_settings(userID, "nodeAlert"):
                continue
            if not utils.check_rpc_address_format(node["ip"]): # is url
                data = await utils.get_node_data(node["ip"], "status")

                node_network = "namada-shielded-expedition-rpc.denodes.xyz"
                node_addr = data['result']['validator_info']['address']

                count_approved = 0
                all_addresses = nodesUptime.get_all_addresses(node_network)
                for addrs in all_addresses:
                    if node_addr in addrs:
                        count_approved += 1

                uptime=(count_approved/len(all_addresses))*100,
                for i in range(0, 100, 5):
                    if uptime < i and last_uptimes.get(userID, 100) > i:
                        last_uptimes[userID] = i
                        try:
                            await bot.send_message(userID, text=text.get_low_uptime(userLang, i))
                        except:
                            break
            else: # is addr
                count_approved = 0
                all_addresses = nodesUptime.get_all_addresses("namada-shielded-expedition-rpc.denodes.xyz")
                for addrs in all_addresses:
                    if str(node["ip"]) in addrs:
                        count_approved += 1

                uptime=float((count_approved/len(all_addresses))*100)
                for i in range(0, 100, 5):
                    if uptime < i and last_uptimes.get(userID, 100) > i:
                        last_uptimes[userID] = i
                        try:
                            await bot.send_message(userID, text=text.get_low_uptime(userLang, i))
                        except:
                            break

        await asyncio.sleep(60)

async def halt_alert():
    should_check = ["namada-rpc.zenode.app", "namada-testnet-rpc.stakeandrelax.net", "namada-rpc.stake-machine.com", "namadarpcse.cryptosj.net:19902"]
    while True:
        heights = list()
        for network in should_check:
            try:
                latest_block = await utils.get_node_data(network, "status")
                latest_block = latest_block["sync_info"]["latest_block_height"]
            except:
                continue
            heights.append(latest_block)

        # all rpc is available and returns the same latest_block
        if len(set(heights)) == 1:
            for user in users:
                userID = user["userID"]
                if users.get_user_settings(userID, "haltAlert"):
                    userLang = users.get_user_settings(userID, "lang")
                    try:
                        await bot.send_message(userID, text=text.get_new_halt(userLang, heights[0]))
                    except:
                        continue

        await asyncio.sleep(300)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="log.txt", filemode="w", format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(check_nodes())
    loop.create_task(update_addresses())
    loop.create_task(cleanup_addressess())
    loop.create_task(check_epoch())
    loop.create_task(halt_alert())
    loop.create_task(uptime_alerts())

    loop.run_forever()
