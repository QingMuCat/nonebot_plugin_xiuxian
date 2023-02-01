import re
import random

from nonebot.params import CommandArg
from nonebot.adapters import Message, Bot
from nonebot.adapters.onebot.v11 import (
    MessageSegment,
    GroupMessageEvent
)

from nonebot_plugin_guild_patch import (
    MessageSegment,
    GuildMessageEvent,
)

from ..utils import data_check_conf, get_msg_pic, check_user
from ..command import choujiang
from ..item_json import Items
from ..xiuxian_config import XiuConfig
from ..xiuxian2_handle import XiuxianDateManage


items = Items()
sql_message = XiuxianDateManage()  # sql类


def get_random_id(dict_data):
    """随机获取key"""
    l_temp = []
    for k, v in dict_data.items():
        l_temp.append(k)
            
    return random.choice(l_temp)

@choujiang.handle()
async def _(bot: Bot, event: GroupMessageEvent | GuildMessageEvent, args: Message = CommandArg()):
    """抽奖机制"""
    await data_check_conf(bot, event)

    try:
        user_id, group_id, mess = await data_check(bot, event)
    except MsgError:
        return
    isUser, user_info, msg = check_user(event)
    if not isUser:
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}" + msg)
    user_id = user_info.user_id
    arg = args.extract_plain_text().strip()
    ls_faqi = 1000000
    ls_faqi_10 = 9000000
    ls_fangju = 1100000
    ls_fangju_10 = 10000000
    ls_st = 1200000
    ls_st_10 = 11000000
    ls_gf = 1200000
    ls_gf_10 = 11000000
    ls_dy = 3000000
    ls_dy_10 = 28000000
    ls_hcdy = 5000000
    ls_hcdy_10 = 47000000
    ls_yc = 1500000
    ls_yc_10 = 14000000

    if arg == "帮助":
        msg = "※---------修仙祈愿---------※\n法器：\n100w灵石1连\n900w灵石10连\n\n防具：\n110w灵石1连\n1000w灵石10连\n\n神通：\n120w灵石1连\n1100w灵石10连\n\n功法：\n120w灵石1连\n1100w灵石10连\n\n丹药：\n300w灵石1连\n2800w灵石10连\n\n合成丹药：\n500w灵石1连\n4700w灵石10连\n\n药材：\n150w灵石1连\n1400w灵石10连\n"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "法器1连":
        if user_info.stone < ls_faqi:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_faqi)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        faqi_data = items.get_data_by_item_type(['法器'])
        random_faqi_id = get_random_id(faqi_data)
        random_faqi_info = items.get_data_by_item_id(random_faqi_id)
        sql_message.update_ls(user_id, ls_faqi, 2)
        sql_message.send_back(user_id,random_faqi_id,random_faqi_info['name'],random_faqi_info['type'], 1, 0 )
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得{}：{}！！！欢迎下次再来！！！".format(user_info.user_name, ls_faqi, random_faqi_info['level'], random_faqi_info['name'])
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "法器10连":
        if user_info.stone < ls_faqi_10:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_faqi_10)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        for x in range(10):
            faqi_data = items.get_data_by_item_type(['法器'])
            random_faqi_id = get_random_id(faqi_data)
            random_faqi_info = items.get_data_by_item_id(random_faqi_id)
            sql_message.send_back(user_id,random_faqi_id,random_faqi_info['name'],random_faqi_info['type'], 1, 0 )
            msg += "{}：{}\n".format(random_faqi_info['level'], random_faqi_info['name'])
        sql_message.update_ls(user_id, ls_faqi_10, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得\n".format(user_info.user_name, ls_faqi_10) + msg + "！！！欢迎下次再来！！！"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "防具1连":
        if user_info.stone < ls_fangju:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_fangju)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        fangju_data = items.get_data_by_item_type(['防具'])
        random_fangju_id = get_random_id(fangju_data)
        random_fangju_info = items.get_data_by_item_id(random_fangju_id)
        sql_message.update_ls(user_id, ls_fangju, 2)
        sql_message.send_back(user_id, random_fangju_id, random_fangju_info['name'], random_fangju_info['type'], 1, 0)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得{}：{}！！！欢迎下次再来！！！".format(user_info.user_name, ls_fangju, random_fangju_info['level'], random_fangju_info['name'])
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "防具10连":
        if user_info.stone < ls_fangju_10:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_fangju_10)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        for x in range(10):
            fangju_data = items.get_data_by_item_type(['防具'])
            random_fangju_id = get_random_id(fangju_data)
            random_fangju_info = items.get_data_by_item_id(random_fangju_id)
            sql_message.send_back(user_id, random_fangju_id, random_fangju_info['name'], random_fangju_info['type'], 1, 0)
            msg += "{}：{}\n".format(random_fangju_info['level'], random_fangju_info['name'])
        sql_message.update_ls(user_id, ls_fangju_10, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得\n".format(user_info.user_name, ls_fangju_10) + msg + "！！！欢迎下次再来！！！"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "神通1连":
        if user_info.stone < ls_st:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_st)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        shentong_data = items.get_data_by_item_type(['神通'])
        random_shentong_id = get_random_id(shentong_data)
        random_shentong_info = items.get_data_by_item_id(random_shentong_id)
        sql_message.send_back(user_id, random_shentong_id, random_shentong_info['name'], random_shentong_info['type'], 1, 0)
        sql_message.update_ls(user_id, ls_st, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得{}：{}！！！欢迎下次再来！！！".format(user_info.user_name, ls_st, random_shentong_info['level'], random_shentong_info['name'])
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
    
    elif arg == "神通10连":
        if user_info.stone < ls_st_10:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_st_10)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        for x in range(10):
            shentong_data = items.get_data_by_item_type(['神通'])
            random_shentong_id = get_random_id(shentong_data)
            random_shentong_info = items.get_data_by_item_id(random_shentong_id)
            sql_message.send_back(user_id, random_shentong_id, random_shentong_info['name'], random_shentong_info['type'], 1, 0)
            msg += "{}：{}\n".format(random_shentong_info['level'], random_shentong_info['name'])
        sql_message.update_ls(user_id, ls_st_10, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得\n".format(user_info.user_name, ls_st_10) + msg + "！！！欢迎下次再来！！！"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg) 
    
    elif arg == "功法1连":
        if user_info.stone < ls_gf:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_gf)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        gongfa_data = items.get_data_by_item_type(['功法'])
        random_gongfa_id = get_random_id(gongfa_data)
        random_gongfa_info = items.get_data_by_item_id(random_gongfa_id)
        sql_message.send_back(user_id, random_gongfa_id, random_gongfa_info['name'], random_gongfa_info['type'], 1, 0)
        sql_message.update_ls(user_id, ls_gf, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得{}：{}！！！欢迎下次再来！！！".format(user_info.user_name, ls_gf, random_gongfa_info['level'], random_gongfa_info['name'])
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "功法10连":
        if user_info.stone < ls_gf_10:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_gf_10)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        for x in range(10):
            gongfa_data = items.get_data_by_item_type(['功法'])
            random_gongfa_id = get_random_id(gongfa_data)
            random_gongfa_info = items.get_data_by_item_id(random_gongfa_id)
            sql_message.send_back(user_id, random_gongfa_id, random_gongfa_info['name'], random_gongfa_info['type'], 1, 0)
            msg += "{}：{}\n".format(random_gongfa_info['level'], random_gongfa_info['name'])
        sql_message.update_ls(user_id, ls_gf_10, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得\n".format(user_info.user_name, ls_gf_10) + msg + "！！！欢迎下次再来！！！"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "丹药1连":
        if user_info.stone < ls_dy:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_dy)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        danyao_data = items.get_data_by_item_type(['丹药'])
        random_danyao_id = get_random_id(danyao_data)
        random_danyao_info = items.get_data_by_item_id(random_danyao_id)
        sql_message.send_back(user_id, random_danyao_id, random_danyao_info['name'], random_danyao_info['type'], 1, 0)
        sql_message.update_ls(user_id, ls_dy, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得{}\n使用效果及等级需求：{}\n！！！欢迎下次再来！！！".format(user_info.user_name, ls_dy, random_danyao_info['name'], random_danyao_info['desc'])
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "丹药10连":
        if user_info.stone < ls_dy_10:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_dy_10)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        for x in range(10):
            danyao_data = items.get_data_by_item_type(['丹药'])
            random_danyao_id = get_random_id(danyao_data)
            random_danyao_info = items.get_data_by_item_id(random_danyao_id)
            sql_message.send_back(user_id, random_danyao_id, random_danyao_info['name'], random_danyao_info['type'], 1, 0)
            msg += "{},使用效果及等级需求：{}\n".format(random_danyao_info['name'], random_danyao_info['desc'])
        sql_message.update_ls(user_id, ls_dy_10, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得\n".format(user_info.user_name, ls_dy_10) + msg + "！！！欢迎下次再来！！！"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "合成丹药1连":
        if user_info.stone < ls_hcdy:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_hcdy)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        hechengdanyao_data = items.get_data_by_item_type(['合成丹药'])
        random_hechengdanyao_id = get_random_id(hechengdanyao_data)
        random_hechengdanyao_info = items.get_data_by_item_id(random_hechengdanyao_id)
        sql_message.send_back(user_id, random_hechengdanyao_id, random_hechengdanyao_info['name'], random_hechengdanyao_info['type'], 1, 0)
        sql_message.update_ls(user_id, ls_hcdy, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得{}\n使用效果：{}，等级需求：{}\n！！！欢迎下次再来！！！".format(user_info.user_name, ls_dy, random_hechengdanyao_info['name'], random_hechengdanyao_info['desc'], random_hechengdanyao_info['境界'])
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "合成丹药10连":
        if user_info.stone < ls_hcdy_10:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_hcdy_10)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        for x in range(10):
            hechengdanyao_data = items.get_data_by_item_type(['合成丹药'])
            random_hechengdanyao_id = get_random_id(hechengdanyao_data)
            random_hechengdanyao_info = items.get_data_by_item_id(random_hechengdanyao_id)
            sql_message.send_back(user_id, random_hechengdanyao_id, random_hechengdanyao_info['name'], random_hechengdanyao_info['type'], 1, 0)
            msg += "{},使用效果：{}，等级需求：{}\n".format(random_hechengdanyao_info['name'], random_hechengdanyao_info['desc'], random_hechengdanyao_info['境界'])
        sql_message.update_ls(user_id, ls_hcdy_10, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得\n".format(user_info.user_name, ls_hcdy_10) + msg + "！！！欢迎下次再来！！！"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "药材1连":
        if user_info.stone < ls_yc:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_yc)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        yaocai_data = items.get_data_by_item_type(['药材'])
        random_yaocai_id = get_random_id(yaocai_data)
        random_yaocai_info = items.get_data_by_item_id(random_yaocai_id)
        sql_message.send_back(user_id, random_yaocai_id, random_yaocai_info['name'], random_yaocai_info['type'], 1, 0)
        sql_message.update_ls(user_id, ls_yc, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得{}：{}！！！欢迎下次再来！！！".format(user_info.user_name, ls_gf, random_yaocai_info['level'], random_yaocai_info['name'])
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    elif arg == "药材10连":
        if user_info.stone < ls_yc_10:
            msg = "对不起，{}道友所持有的灵石不足以进行{}祈愿，请准备好充足的{}枚灵石再来祈愿，谢谢！".format(user_info.user_name, arg, ls_yc_10)
            if XiuConfig().img:
                pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
                await choujiang.finish(MessageSegment.image(pic))
            else:
                await choujiang.finish(f"@{event.sender.nickname}\n" + msg)
        for x in range(10):
            yaocai_data = items.get_data_by_item_type(['药材'])
            random_yaocai_id = get_random_id(yaocai_data)
            random_yaocai_info = items.get_data_by_item_id(random_yaocai_id)
            sql_message.send_back(user_id, random_yaocai_id, random_yaocai_info['name'], random_yaocai_info['type'], 1, 0)
            msg += "{}：{}\n".format(random_yaocai_info['level'], random_yaocai_info['name'])
        sql_message.update_ls(user_id, ls_yc_10, 2)
        msg = "恭喜{}道友消耗{}枚灵石祈愿获得\n".format(user_info.user_name, ls_yc_10) + msg + "！！！欢迎下次再来！！！"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)

    else:
        msg = "请获取帮助后输入正确的祈愿格式，道友输入的内容不存在或未开放！"
        if XiuConfig().img:
            pic = await get_msg_pic(f"@{event.sender.nickname}\n" + msg)
            await choujiang.finish(MessageSegment.image(pic))
        else:
            await choujiang.finish(f"@{event.sender.nickname}\n" + msg)



async def data_check(bot, event):
    """
    判断用户信息是否存在
    """
    user_qq = event.get_user_id()
    guild_id = await get_guild_id(event.get_session_id())
    msg = sql_message.get_user_message(user_qq)

    if msg:
        pass
    else:
        await bot.send(event=event, message=f"没有您的信息，输入【我要修仙】加入！")
        raise MsgError

    return user_qq, guild_id, msg


async def get_guild_id(session_id):
    """获取guild_id"""
    res = re.findall("_(.*)_", session_id)
    guild_id = res[0]
    return guild_id

class MsgError(ValueError):
    pass