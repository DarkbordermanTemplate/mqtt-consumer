from loguru import logger


def handler(_, __, message):
    logger.info(f"{message.payload.decode()}")
