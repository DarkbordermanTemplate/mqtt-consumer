"""Service-wide config"""
import os


class Config:
    BROKERS = os.environ.get("BROKERS", "127.0.0.1:1883")
    MQTT_CLIENT_ID = os.environ.get("MQTT_CLIENT_ID", "")
    MQTT_ACCOUNT = os.environ.get("MQTT_ACCOUNT", "")
    MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD", "")
