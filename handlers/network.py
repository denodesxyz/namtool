from aiogram import Router, F
from aiogram.types import Message
import keyboards
from database import users
from aiogram.fsm.context import FSMContext
import states
import utils
import text
 

router = Router()

@router.message(F.text.in_({"Network Status", "Статус Сети", "Статус Мережі"}))
async def process_network_status(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_network_status_text(lang), reply_markup=keyboards.get_networks(lang))
    await state.set_state(states.NetworkStatus.status)


@router.message(states.NetworkStatus.status)
async def get_network_status(msg: Message, state: FSMContext):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    if msg.text not in ["Campfire Testnet",
                        "Shielded Expedition",
                        "Namada Mainnet (Upcoming)"]:
        await msg.answer(text.get_nosuchnetwork_text(lang))
        return
    
    # this network is unavailable
    if msg.text != "Campfire Testnet" and \
            msg.text != "Shielded Expedition":
        await msg.answer(text.get_noinfonetwork_text(lang))
        return

    network_url = ""
    chain_id = ""

    if msg.text == "Campfire Testnet":
        network_url = "rpc.luminara.icu"
        chain_id = "luminara.c3c6d2a524160fd4de13e"
        explorer = "https://explorer.luminara.icu/campfire"
        last_block_height = await utils.get_node_data(network_url, "abci_info")
        last_block_height = last_block_height["result"]["response"]["last_block_height"]
        validators = await utils.get_node_data(network_url, f"validators?height={last_block_height}")
        count_validators = validators["result"]["total"]
        await msg.answer(f"""
Network: <b>{msg.text}</b>

Chain Id: {chain_id}
Latest Block: {last_block_height}
Validator Set: {count_validators}

<b>Explorer:</b> <a href="{explorer}">Link</a>
    """, reply_markup=keyboards.get_menu(lang, utils.is_admin(msg.from_user.id)), disable_web_page_preview=True)

    elif msg.text == "Shielded Expedition":
        network_url = "namada-shielded-expedition-rpc.denodes.xyz/"
        chain_id = "shielded-expedition.b40d8e9055"
        explorer = "https://namada.deportal.xyz/explorer/dashboard"
        last_block_height = await utils.get_node_data(network_url, "abci_info")
        last_block_height = last_block_height["result"]["response"]["last_block_height"]
        validators = await utils.get_node_data("namada-alt.denodes.xyz", "validators.json")
        epoch = await utils.get_node_data("namada-alt.denodes.xyz", "epoch.json")
        epoch = epoch["epoch"]
        consensus = len(list(filter(lambda validator: validator["state"] == "consensus", validators["validators"])))
        count_validators = len(validators["validators"])
        await msg.answer(f"""
Network: <b>{msg.text}</b>
Chain Id: <code>{chain_id}</code>
Latest Block: {last_block_height}
Validator Set: {consensus}/{count_validators}
Epoch: {epoch}

<b>Explorer:</b> <a href="{explorer}">Link</a>
    """, reply_markup=keyboards.get_menu(lang, utils.is_admin(msg.from_user.id)), disable_web_page_preview=True)

    await state.clear()



@router.message(F.text.in_({"Explore Namada", "Больше информации о Namada", "Більше інформації про Namada"}))
async def process_explore_namada(msg: Message):
    lang = users.get_user_settings(msg.from_user.id, "lang")
    await msg.answer(text.get_explore_namada(lang), disable_web_page_preview=True)
