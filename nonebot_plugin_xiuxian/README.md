## nonebot_plugin_xiuxian_GCDI

### 插件说明：
    基于nonebot_plugin_xiuxian原版进行修改，可以在QQ频道与QQ群进行互联

> 欢迎各位体验，如遇bug请及时issue反馈

### 食用方法

1. 解压至bot插件目录，正常情况为src='src.plugins.'
   若有不同，请按照以下方式修改：根目录下__init__.py文件中的42行：src=''中的内容，填写的是存放插件的目录

2. 安装依赖：

```
频道补丁
pip install nonebot_plugin_guild_patch -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 更新
**2023/02/01**
1.修复部分逻辑，对之后便与进行重构以及增加新功能准备
2.更改部分功能权限
3.金银阁可自行注释，群聊默认无法使用
