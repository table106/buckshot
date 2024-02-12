import logging
logging.basicConfig(level=logging.INFO, filename="debug.log", filemode="w", format="@ line %(lineno)d - %(message)s")

def debug(msg):
    return logging.debug(msg)

def info(msg):
    return logging.info(msg)

def warning(msg):
    return logging.warning(msg)

def error(msg):
    return logging.error(msg)

def critical(msg):
    return logging.critical(msg)