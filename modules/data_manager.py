import multiprocessing
from modules.tipico_umas import UMA_Tipico1, UMA_Tipico2, UMA_Tipico3, UMA_Tipico4, UMA_Tipico5, UMA_Tipico6, UMA_Tipico7, UMA_Tipico8
import BAC0
from influxdb import InfluxDBClient
import time
from config import DEVICE_IP, BACNET_PORT, influx_config, DEV_CONFIG
import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

class DataManager:
    def __init__(self):
        self.bacnet = BAC0.lite(ip=DEVICE_IP, port=BACNET_PORT)
        self.data = multiprocessing.Manager().dict()
        self.bacnet_devices = {}

    def main_loop(self):
        logger.info("Iniciando main_loop de DataManager")
        # Eventos para sincronización
        read_event = multiprocessing.Event()
        ingest_event = multiprocessing.Event()
        read_event.set()  # Comienza con lectura permitida
        # Procesos para leer dispositivos
        procesos = []
        for uma_name, device in self.bacnet_devices.items():
            p = multiprocessing.Process(target=self.leer_dispositivo, args=(uma_name, device, self.data, read_event, ingest_event))
            procesos.append(p)
            p.start()
        # Proceso para ingestión en InfluxDB
        p_influx = multiprocessing.Process(target=self.ingestar_influxdb, args=(self.data, influx_config, read_event, ingest_event))
        p_influx.start()
        # Espera a que los procesos de lectura terminen
        for p in procesos:
            p.join()
        # El proceso de InfluxDB sigue corriendo

    def leer_dispositivo(self, device_name, device, shared_dict, read_event, ingest_event):
        """Lee todos los puntos de un dispositivo BACnet y los almacena en shared_dict, sincronizado por eventos."""
        while True:
            read_event.wait()  # Espera a que se permita leer
            resultados = {}
            for punto_nombre, punto_info in device.puntos.items():
                try:
                    valor = BAC0.read(f"{device.device_id} {punto_info['obj']} {punto_info['instancia']}")
                    logger.debug(f"{device_name}: {punto_nombre} = {valor}")
                except Exception as ex:
                    valor = None
                    logger.warning(f"Error leyendo {punto_nombre} en {device_name}: {ex}")
                resultados[punto_nombre] = valor
            shared_dict[device_name] = resultados
            # Señala que terminó la lectura y activa la ingesta
            read_event.clear()
            ingest_event.set()

    def ingestar_influxdb(self, shared_dict, influx_config, read_event, ingest_event):
        """Ingesta los datos de shared_dict en InfluxDB, sincronizado por eventos."""
        client = InfluxDBClient(
            host=influx_config['host'],
            port=influx_config['port'],
            username=influx_config['username'],
            password=influx_config['password'],
            database=influx_config['database']
        )
        while True:
            ingest_event.wait()  # Espera a que haya datos para ingestar
            for device_name, puntos in shared_dict.items():
                for punto_nombre, valor in puntos.items():
                    if valor is not None:
                        json_body = [{
                            "measurement": punto_nombre,
                            "tags": {"device": device_name},
                            "fields": {"value": valor}
                        }]
                        client.write_points(json_body)
            # Señala que terminó la ingesta y activa la lectura
            ingest_event.clear()
            read_event.set()
            time.sleep(0.05)  # Espera antes de la siguiente lectura