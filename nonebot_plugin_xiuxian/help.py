
from .xiuxian_config import XiuConfig

"""
Help帮助信息

"""

__xiuxian_version__ = "v0.4.26"

__xiuxian_notes__ = f"""
指令：
1、我要修仙：进入修仙模式
2、我的修仙信息：获取修仙数据
3、修仙签到：获取灵石及修为
4、重入仙途：重置灵根数据，每次{XiuConfig().remake}灵石
5、金银阁：猜大小/奇偶/数字，赌灵石 示例:金银阁10大/小/奇/偶/猜3
6、改名xx：修改你的道号
7、突破：修为足够后，可突破境界（一定几率失败）
8、闭关、出关、灵石出关：修炼增加修为，挂机功能
9、送灵石100@xxx,偷灵石@xxx,抢灵石@xxx
10、排行榜：修仙排行榜，灵石排行榜，战力排行榜，宗门排行榜
11、悬赏令帮助：获取悬赏令帮助信息
12、我的状态：查看当前HP,我的功法：查看当前技能
13、宗门系统：发送"宗门帮助"获取
14、灵庄系统：发送"灵庄帮助"获取
15、世界BOSS：发送"世界boss帮助"获取
16、功法：发送“我的功法”查看，当前获取途径看“宗门帮助”
17、背包/交友：发送"背包帮助"获取
18、秘境系统：发送"秘境帮助"获取
19、启用/禁用修仙功能：当前群开启或关闭修仙功能
20、炼丹帮助：炼丹功能
21、修仙祈愿：发送"修仙祈愿帮助"获取
""".strip()
