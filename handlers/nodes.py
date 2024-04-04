from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

import keyboards
from database import users, nodes, nodesUptime
import text
import states
import utils


router = Router()

@router.message(F.text.in_({"Node Status", "Статус Ноды", "Статус Ноди"}))
async def process_node_status(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")

    user_nodes = nodes.get_user_nodes(msg.from_user.id)
    if not user_nodes:
        await msg.answer(text.get_node_status_not_exist(lang), reply_markup=keyboards.get_back(lang))
        await state.set_state(states.CreateNode.newnode)
    else:
        for node in user_nodes:
            if utils.check_rpc_node_format(node["ip"]):
                try:
                    node_status = await utils.get_node_data(node["ip"], "status")
                except Exception as e:
                    await msg.answer(text.get_nodeisnotavailable_text(lang).format(ip=node["ip"]))
                    continue
                if not node_status:
                    await msg.answer(f"No data for {node['ip']}")
                    continue

                node_network = "namada-shielded-expedition-rpc.denodes.xyz"
                node_addr = node_status['result']['validator_info']['address']

                latest_block_height = await utils.get_node_data(node["ip"], "abci_info")
                latest_block_height = latest_block_height['result']['response']['last_block_height']

                addresses = await utils.get_network_addresses(node_network, latest_block_height)

                count_approved = 0
                all_addresses = nodesUptime.get_all_addresses(node_network)
                for addrs in all_addresses:
                    if node_addr in addrs:
                        count_approved += 1

                await msg.answer(text.get_node_status_text(lang).format(
                        ip=node['ip'],
                        moniker=node_status['result']['node_info']['moniker'],
                        active="Yes" if node_addr in addresses else "No",
                        catching=str(data['result']['sync_info']['catching_up']).capitalize(),
                        height=data['result']['sync_info']['latest_block_height'],
                        uptime=round((count_approved/len(all_addresses))*100, 2),
                        addr=node_addr
                ))
            else:
                try:
                    data = await utils.check_rpc_address_exists(node["ip"])
                except Exception as e:
                    await msg.answer(text.get_nodeisnotavailable_text(lang).format(ip=node["ip"]))
                    continue
                if not data:
                    await msg.answer(f"No data for {node['ip']}")
                    continue

                uptime = "-"
                if data['state'] == 'consensus':
                    count_approved = 0
                    all_addresses = nodesUptime.get_all_addresses("namada-shielded-expedition-rpc.denodes.xyz")
                    for addrs in all_addresses:
                        if str(node["ip"]) in addrs:
                            count_approved += 1

                    uptime=round((count_approved/len(all_addresses))*100, 2)

                await msg.answer(text.get_address_data(lang, data, uptime))


@router.message(states.CreateNode.newnode)
async def process_newnode(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    is_admin = utils.is_admin(msg.from_user.id)

    if (not utils.check_rpc_node_format(msg.text)) and (not utils.check_rpc_address_format(msg.text)):
        await msg.answer(text.get_error_invalid_ipv4(lang))
        return

    if len(nodes.get_user_nodes(msg.from_user.id)) == 0:
        if utils.check_rpc_node_format(msg.text):
            print("url")
            node_data = await utils.get_node_data(msg.text, "status")
            if node_data:
                nodes.add_user_node(msg.from_user.id, msg.text)
                await msg.answer(text.get_new_node_success_text(lang), reply_markup=keyboards.get_menu(lang, is_admin))
            else:
                await msg.answer(text.get_nodatafornode_text(lang).format(ip=msg.text), reply_markup=keyboards.get_menu(lang, is_admin))
        else:
            exists = await utils.check_rpc_address_exists(msg.text)
            if not exists:
                await msg.answer(text.get_wrong_rpc_address(lang), reply_markup=keyboards.get_menu(lang, is_admin))
            else:
                if "tnam1" in msg.text:
                    # if user passes address address, we should save only tm-address, but not address
                    nodes.add_user_node(msg.from_user.id, exists['tm-address'])
                    await msg.answer(text.get_new_node_success_text(lang), reply_markup=keyboards.get_menu(lang, is_admin))
                else:
                    nodes.add_user_node(msg.from_user.id, msg.text)
                    await msg.answer(text.get_new_node_success_text(lang), reply_markup=keyboards.get_menu(lang, is_admin))
    else:
        await msg.answer(text.get_new_node_failure_text(lang), reply_markup=keyboards.get_menu(lang, is_admin))
    await state.clear()


@router.message(F.text.in_({"Run a Node", "Запуск Ноды", "Запуск Ноди"}))
async def process_run_node(msg: Message):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_run_node(lang), disable_web_page_preview=True)
