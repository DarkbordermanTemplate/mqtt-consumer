from loguru import logger


def on_connect_callback(client, userdata, flags, response_code):
    if response_code != 0:
        logger.error(f"Connect to MQTT broker failed, status code: {response_code}")
    else:
        logger.info(f"{client} connect to MQTT broker successfully")
        logger.info(f"client data {userdata}, response flags {flags}")
