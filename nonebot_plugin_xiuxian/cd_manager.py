from random import choice
from typing import Dict, Any
import snoop
from nonebot import get_driver
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot_plugin_guild_patch import GuildMessageEvent
from .xiuxian2_handle import XiuxianDateManage

driver = get_driver()
cdtype :Dict[str, int] = {}
cd_data :Dict[str, Any] = {}
sql_message = XiuxianDateManage()  # sql类

cdmsg = [
    '你急啥呢？{cd_msg}后再来吧',
    'CD:{cd_msg}',
    '{cd_msg}后再来哦',
    
]

@snoop
def check_cd(event: MessageEvent, cdtype: str) -> int:
    """
    :说明: `check_cd`
        * 检查是否达到CD时间\n
        * 如果达到则返回 `0`\n
        * 如果未达到则返回 `剩余CD时间`
    :参数:
      * `event: MessageEvent`: 事件对象
      * `cdtype: str`: cd类型
    :返回:
      - `int`: 剩余时间
    """
    if isinstance(event, GuildMessageEvent):
        tiny_id = event.get_user_id()
        user_info = sql_message.get_user_message3(tiny_id)
        uid = int(user_info.user_id)
    else:
        uid = int(event.get_user_id())
    # cd = 设置的到期时间 - 当前时间
    try:
        cd: int = cd_data[uid][cdtype] - event.time
        logger.debug(f"{uid} 还剩: {cd}")
    except KeyError:
        cd = -1
    if cd < 0:
        return 0
    else:
        return cd
    
@snoop    
def add_cd(event: MessageEvent, config_time, cdtype, times: int = 1):
    """
    :说明: `add_cd`
    > 添加cd, 到期时间 = 当前时间 + 设定的CD * 倍数
    :参数:
      * `event: MessageEvent`: 事件
      * `times: int`: 倍数, 默认为 `1`
    """
    if isinstance(event, GuildMessageEvent):
        tiny_id = event.get_user_id()
        user_info = sql_message.get_user_message3(tiny_id)
        user_id = int(user_info.user_id)
    else:
        user_id = int(event.get_user_id())
    try:
        cd_data[user_id]
    except:
        cd_data[user_id] = {}
    
    cd_data[user_id][cdtype] = event.time + times * config_time
    logger.debug("查询CD: {}".format(cd_data))
    
@snoop    
def cd_msg(time_last) -> str:
    """获取CD提示信息"""
    hours, minutes, seconds = 0, 0, 0
    if time_last >= 60:
        minutes, seconds = divmod(time_last, 60)
        hours, minutes = divmod(minutes, 60)
    else:
        seconds = time_last
    cd_msg = f"{str(hours) + '小时' if hours else ''}{str(minutes) + '分钟' if minutes else ''}{str(seconds) + '秒' if seconds else ''}"

    return choice(cdmsg).format(cd_msg=cd_msg)