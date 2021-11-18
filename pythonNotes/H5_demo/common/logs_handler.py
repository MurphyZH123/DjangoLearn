import logging
import logzero
import os
from logzero import logger

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs/test.log')


class Logzero(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.logger = logger
        # console控制台输入日志格式 - 带颜色
        self.console_format = '%(color)s' \
                              '[%(asctime)s]-[%(levelname)1.1s]-[%(filename)s]-[%(funcName)s:%(lineno)d] 日志信息: %(' \
                              'message)s ' \
                              '%(end_color)s '
        # 创建一个Formatter对象
        self.formatter = logzero.LogFormatter(fmt=self.console_format)
        # 将formatter提供给setup_default_logger方法的formatter参数
        logzero.setup_default_logger(formatter=self.formatter)

        # 设置日志文件输出格式
        self.formater = logging.Formatter(
            '[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(funcName)s:%(lineno)d] 日志信息: %(message)s')
        # 设置日志文件等级
        logzero.loglevel(logging.DEBUG)
        # 输出日志文件路径和格式
        logzero.logfile(f'{log_path}', formatter=self.formater)

    def debug(self, msg):
        self.logger.debug(msg=msg)

    def info(self, msg):
        self.logger.info(msg=msg)

    def warning(self, msg):
        self.logger.warning(msg=msg)

    def error(self, msg):
        self.logger.error(msg=msg)

    def exception(self, msg):
        self.logger.exception(msg=msg)


logzeros = Logzero()

if __name__ == '__main__':
    logzeros.debug("debug")
    logzeros.info("info")
    logzeros.warning("warning")
    logzeros.error("error")
    a = 5
    b = 0
    try:
        c = a / b
    except Exception as e:
        logzeros.exception("Exception occurred")
