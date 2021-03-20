import paho.mqtt.client as mqtt
from loguru import logger
from paho.mqtt.client import Client


def create_client(client_id: str, account: str, password: str) -> Client:
    """Create an MQTT client

    Args:
        host (str): Host location
        client_id (str): User's clientid, should be mac address without : delimiter
        access_key (str): Access key
        secret_key (str): Secret key

    Returns:
        Client: Created client
    """
    client = mqtt.Client(client_id=client_id)
    logger.info(
        f"create MQTT client with client_id {client_id} account {account}, password {password}"
    )
    client.username_pw_set(account, password)
    return client


def connect_client(client, host: str, keepalive: int = 20):
    client.connect(host, keepalive=keepalive)
    client.loop_start()
