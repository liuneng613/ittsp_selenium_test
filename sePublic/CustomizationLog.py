import logging
import time

from sePublic import ReadConfig


class CustomizationLog:
    """
    指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中
    """

    def __init__(self, logger):
        # 1. 初始化 logger = logging.getLogger(logger)，getLogger()方法后面最好加上所要日志记录的模块名字，
        # 后面的日志格式中的%(name)s 对应的是这里的模块名字
        self.logger = logging.getLogger(logger)
        # 2. 设置级别 logger.setLevel(logging.DEBUG),Logging中有NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
        # 这几种级别，日志会记录设置级别以上的日志
        self.logger.setLevel(logging.DEBUG)
        # 3. 定义log文件名
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = ReadConfig.root_path + r'/logs/'
        log_name = log_path + rq + r'.log'
        # 4. 创建一个FileHandler，用于写入日志文件
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.DEBUG)
        # 5. 创建一个StreamHandler(),用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # 6. 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(funcName)s - '
                                      '%(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 7. 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    my_logger = CustomizationLog('TestMyLog')
    my_logger.info('打开浏览器')
    my_logger.debug("最大化浏览器窗口。")
    my_logger.warn("打开百度首页。")
    my_logger.error("打开百度首页。")
    my_logger.critical("打开百度首页。")
