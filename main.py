from modules.tipico_umas import UMA_Tipico1, UMA_Tipico2, UMA_Tipico3, UMA_Tipico4, UMA_Tipico5, UMA_Tipico6, UMA_Tipico7, UMA_Tipico8
import time
from config import DEV_CONFIG, MQTT_CONFIG
from modules.data_manager import DataManager
from modules.control_manager import ControlManager

def main():
    data_manager = DataManager()
    bacnet_instance = data_manager.bacnet

    # Dictionary to hold the initialized BACnet device instances
    bacnet_devices = {}

    for uma_name, config in DEV_CONFIG.items():
        # Get the corresponding Tipico class by name from globals()
        tipico_class = globals()[config['TIPICO']]
        # Create a new BACnet device instance
        bacnet_devices[uma_name] = tipico_class(
            device_id=config['DEVICE_ID'],
            ip=config['IP'],
            bacnet = bacnet_instance
        )

    data_manager.bacnet_devices = bacnet_devices
    control_manager = ControlManager(bacnet_devices, MQTT_CONFIG, bacnet_instance)
    control_manager.start()

    # data manager main loop
    try:
        data_manager.main_loop()
    except KeyboardInterrupt:
        print("Terminating processes...")
    except Exception as e:
        print(f"An error occurred in main loop: {e}")
        raise
    finally:
        pass  # BAC0.disconnect_all() si es necesario

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        pass  # BAC0.disconnect_all() si es necesario