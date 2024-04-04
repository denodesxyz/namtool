import hashlib
import aiohttp
import config
from json import loads
import string
import re
import socket


url_regex = re.compile(
    r"(\w+://)?"                # protocol                      (optional)
    r"(\w+\.)?"                 # host                          (optional)
    r"(([\w-]+)\.(\w+))"        # domain
    r"(\.\w+)*"                 # top-level domain              (optional, can have > 1)
    r"([\w\-\._\~/]*)*(?<!\.)"  # path, params, anchors, etc.   (optional)
)

# not used
def get_hash(value: str):
    return hashlib.md5(value.encode()).hexdigest()


def is_admin(user_id):
    return int(user_id) in loads(config.env_values["ADMINS"])


async def get_node_data(ip, path):
    url_path = f"http://{ip}/{path}" if "http" not in ip else f"{ip}/{path}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url_path) as response:
                res = await response.json()
                return res
    except Exception as e:
        print(e)
        return {}


async def check_node_active(ip):
    node_status = await get_node_data(ip, "status")
    node_validators = await get_node_data(ip, "validators")
    if node_status and node_validators:
        return node_validators['result']['validators'] in [j['address'] for j in [i for i in node_status['result']['validators']]]
    return False


async def get_network_addresses(ip, block):
    val_signs = []
    r = await get_node_data(ip, f"block?height={block}")
    signs = r['result']['block']['last_commit']['signatures']
    for sign in signs:
        val_signs.append(sign['validator_address'])
    return val_signs


def is_ip(addr):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False


def check_rpc_node_format(input_string):
    return is_ip(input_string) or url_regex.match(input_string)


def check_rpc_address_format(input_string: str):
    input_string = input_string.lower()
    return (len(input_string) == 40 and all(c in string.hexdigits for c in input_string)) \
    or (len(input_string) == 45 and input_string.startswith("tnam1"))


async def check_rpc_address_exists(address):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://namada-alt.denodes.xyz/validators.json") as response:
            res = await response.json()
    for validator in res['validators']:
        if validator['address'] == address or validator['tm-address'] == address:
            return validator
    return False
