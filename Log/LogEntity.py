import datetime
import logging
import os


class LogUtil:
    def __init__(self, name=None):
        # 日志名称
        self.logger = logging.getLogger(name)
        # 日志级别
        self.logger.setLevel(logging.DEBUG)
        # 日志输出到控制台
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)
        # 输出到文件
        self.date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log', self.date + '_normal.log')
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.file = logging.FileHandler(self.filename, encoding='utf-8')
        self.file.setLevel(logging.DEBUG)
        self.error_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log', self.date + '_error.log')
        self.error_file = logging.FileHandler(self.error_filename, encoding='utf-8')
        self.error_file.setLevel(logging.ERROR)
        # 日志显示内容
        self.formatstr = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
        self.format = logging.Formatter(self.formatstr)
        self.console.setFormatter(self.format)
        self.file.setFormatter(self.format)
        self.error_file.setFormatter(self.format)
        # 加入到hander
        self.logger.addHandler(self.console)
        self.logger.addHandler(self.file)
        self.logger.addHandler(self.error_file)

    def getLogger(self):
        return self.logger


logger = LogUtil("test_project").getLogger()