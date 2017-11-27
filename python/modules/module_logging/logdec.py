# -*- encoding:utf-8 -*-
import logging

def log(func):
    def wrapper(*args, **kw):
        # create logger
        logger_name = "example"
        logger = logging.getLogger(logger_name)

        sh = logging.StreamHandler()
        sh.setLevel(logging.WARN)

        # create file handler
        log_path = "./log.log"
        fh = logging.FileHandler(log_path)
        fh.setLevel(logging.WARN)

        # create formatter
        fmt = "%(asctime)-15s %(levelname)s %(filename)s " \
              "%(lineno)d %(process)d %(message)s"
        datefmt = "%a %d %b %Y %H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)

        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(sh)
        logger.warn('warn message before %s'%(func.__name__))

        result = func(*args, **kw)
        logger.warn('warn message after %s'%(func.__name__))
        return result
    return wrapper

@log
def now():
    print('2015-3-25')

now()
