import paho.mqtt.client as mqtt
import logging
import json

class ControlManager:
    def __init__(self, bacnet_devices, mqtt_config, bacnet):
        self.bacnet_devices = bacnet_devices
        self.mqtt_config = mqtt_config
        self.bacnet = bacnet
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.logger = logging.getLogger(__name__)

    def start(self):
        self.client.connect(self.mqtt_config['host'], self.mqtt_config['port'], 60)
        self.client.loop_start()
        self.logger.info("MQTT client started and listening for control commands.")

    def on_connect(self, client, userdata, flags, rc):
        self.logger.info(f"Connected to MQTT broker with result code {rc}")
        # Suscribirse a los tópicos de control
        client.subscribe("umas/control/#")

    def on_message(self, client, userdata, msg):
        self.logger.info(f"Received MQTT message: {msg.topic} {msg.payload}")
        try:
            payload = json.loads(msg.payload.decode())
            # uma_id = payload.get(uma_name)
            # uma_ip = payload.get('ip')
            uma_name = payload.get('name')
            command = payload.get('command')
            value = payload.get('value')
            if command == 'power':
                self.set_power(uma_name, value)
            elif command == 'setpoint_temp':
                self.set_setpoint_temp(uma_name, value)
            elif command == 'setpoint_hum':
                self.set_setpoint_hum(uma_name, value)
            elif command == 'setpoint_pres':
                self.set_setpoint_pres(uma_name, value)
            else:
                self.logger.warning(f"Comando desconocido: {command}")
        except Exception as ex:
            self.logger.error(f"Error procesando mensaje MQTT: {ex}")

    def set_power(self, device, value):
        punto = "Encendido/Apagado del sistema"
        try:
            device.escribir_punto(punto, value)
            self.logger.info(f"Power set to {value} for device {device.device_id}")
        except Exception as ex:
            self.logger.error(f"Error setting power: {ex}")

    def set_setpoint_temp(self, device, value):
        punto = 'SetPoint de Temperatura'
        try:
            device.escribir_punto(punto, value)
            self.logger.info(f"SetPoint de Temperatura set to {value} for device {device.device_id}")
        except Exception as ex:
            self.logger.error(f"Error setting temperature setpoint: {ex}")

    def set_setpoint_hum(self, device, value):
        punto = 'SetPoint de Humedad'
        try:
            device.escribir_punto(punto, value)
            self.logger.info(f"SetPoint de Humedad set to {value} for device {device.device_id}")
        except Exception as ex:
            self.logger.error(f"Error setting humidity setpoint: {ex}")

    def set_setpoint_pres(self, device, value):
        punto = 'SetPoint de Presión'
        try:
            device.escribir_punto(punto, value)
            self.logger.info(f"SetPoint de Presión set to {value} for device {device.device_id}")
        except Exception as ex:
            self.logger.error(f"Error setting pressure setpoint: {ex}")