import logging
logging.basicConfig(level=logging.DEBUG, filename="debug.log", filemode="w", format="%(asctime)s at line no. %(lineno)d - %(message)s")

def debug(msg):
    logging.debug(msg)

def info(msg):
    logging.info(msg)

def warning(msg):
    logging.warning(msg)

def error(msg):
    logging.error(msg)

def critical(msg):
    logging.critical(msg)

print("wrong file idiot")