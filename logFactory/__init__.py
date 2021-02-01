import logging


def getLogger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    logger.addHandler(ch)
    return logger
