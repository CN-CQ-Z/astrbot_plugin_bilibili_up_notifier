# Bilibili UP主视频通知插件

这是一个AstrBot的插件，用于检测B站UP主发布的新视频并自动发送通知给订阅的用户。

## 功能特点

- 支持订阅多个UP主
- 自动检测UP主发布的新视频，每小时4次（每15分钟/900秒一次）
- 及时发送通知包含视频标题和链接
- 支持查看订阅列表
- 支持取消订阅

## 命令说明

- `/bili_sub UP主ID` - 订阅指定的UP主
- `/bili_unsub UP主ID` - 取消订阅指定的UP主
- `/bili_list` - 查看已订阅的UP主列表
- `/bili_help` - 显示帮助信息

## 安装方法

1. 将本插件放在AstrBot的`data/plugins/`目录下
2. 安装依赖：`pip install -r requirements.txt`
3. 重启AstrBot或在插件管理界面重载插件

## 注意事项

- UP主ID是B站用户的数字ID，可在UP主个人主页URL中找到
- 插件会在首次运行时自动创建配置文件
- 插件使用B站的公开API获取视频信息，可能受到B站API限制

## 配置文件说明

插件配置文件位于`data/plugins/bilibili_up_notifier/config.json`，包含以下内容：

- `last_video_info` - 存储UP主最后发布视频的信息
- `subscriptions` - 存储用户的UP主订阅关系

## 开发说明

萌新开发，欢迎反馈问题和建议。

## 版本历史

- v1.0.0 - 初始版本，实现基本功能