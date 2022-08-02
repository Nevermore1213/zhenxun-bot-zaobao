from nonebot import on_command
from services.log import logger
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent
from nonebot.typing import T_State
import requests
from utils.http_utils import AsyncHttpx


__zx_plugin_name__ = "每日60秒早报"
__plugin_usage__ = """
usage：
    每日60秒早报
    指令：
        早报/新闻
""".strip()
__plugin_des__ = "第一次写插件"
__plugin_cmd__ = ["早报/新闻"]
__plugin_version__ = 0.1
__plugin_author__ = "Nevermore"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["早报", "新闻"],
}


zaobao = on_command("早报", aliases={"早报", "新闻"}, priority=5, block=True)

url = "https://v2.alapi.cn/api/zaobao"
payload = "token= xxxxx &format=json"
headers = {'Content-Type': "application/x-www-form-urlencoded"}


@zaobao.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    response = requests.request("POST", url, data=payload, headers=headers)
    text = response.json()
    text_1 = text['data']['news']
    str = text['data']['date'] + '\n'
    for i in text_1:
        str += i
        str += '\n'
    result = str
    await zaobao.send(result)
