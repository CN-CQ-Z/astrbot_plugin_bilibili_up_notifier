# Bilibili UP主视频通知插件
# 该文件导入BilibiliUpNotifier类并作为插件入口

from .main import BilibiliUpNotifier

# 确保模块正确导出插件类
export = BilibiliUpNotifier