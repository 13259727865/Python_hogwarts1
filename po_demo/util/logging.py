import logging, time, os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:

    def __init__(self):
        # self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        # self.logger = logging.getLogger("log")
        # self.logger.setLevel(logging.INFO)
        #
        # self.formater = logging.Formatter(
        #     '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        #
        # self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        # self.console = logging.StreamHandler()
        # self.console.setLevel(logging.DEBUG)
        # self.filelogger.setLevel(logging.DEBUG)
        # self.filelogger.setFormatter(self.formater)
        # self.console.setFormatter(self.formater)
        # self.logger.addHandler(self.filelogger)
        # self.logger.addHandler(self.console)
        # 绑定绑定句柄到logger对象
        self.logger = logging.getLogger(__name__)
        # 获取当前⼯具⽂件所在的路径
        root_path = os.path.dirname(os.path.abspath(__file__))
        # 拼接当前要输出⽇志的路径
        log_dir_path = os.sep.join([root_path, '..', f'/log'])
        if not os.path.isdir(log_dir_path):
            os.mkdir(log_dir_path)
        # 创建⽇志记录器，指明⽇志保存路径,每个⽇志的⼤⼩，保存⽇志的上限
        file_log_handler = RotatingFileHandler(os.sep.join([log_dir_path, 'log.txt']),
                                               maxBytes=1024 * 1024, backupCount=10, encoding="utf-8")
        # 设置⽇志的格式
        date_string = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(filename)s]/[line: %(lineno)d]/[%(funcName)s] %(message)s ', date_string)
        # ⽇志输出到控制台的句柄
        stream_handler = logging.StreamHandler()
        # 将⽇志记录器指定⽇志的格式
        file_log_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        # 为全局的⽇志⼯具对象添加⽇志记录器
        # 绑定绑定句柄到logger对象
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_log_handler)
        # 设置⽇志输出级别
        self.logger.setLevel(level=logging.INFO)


LogRoot = Logger().logger
