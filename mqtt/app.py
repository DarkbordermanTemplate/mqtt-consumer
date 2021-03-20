from config import Config
from topics import TOPIC_HANDLERS
from utilities import create_client
from utilities.callbacks import on_connect_callback

if __name__ == "__main__":
    CLIENT = create_client(
        Config.MQTT_CLIENT_ID, Config.MQTT_ACCOUNT, Config.MQTT_PASSWORD
    )
    CLIENT.on_connect = on_connect_callback

    for handlers in TOPIC_HANDLERS:
        if handlers.enabled:
            CLIENT.message_callback_add(handlers.topic, handlers.handle)
            CLIENT.subscribe(handlers.topic)
