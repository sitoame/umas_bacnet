class UMA:
    def __init__(self, device_id, ip, tipo, bacnet):
        self.device_id = device_id
        self.ip = ip
        self.tipo = tipo
        self.bacnet = bacnet
        self.puntos = {}  # Se define en la subclase
        self.puerto = 47816 
    
    def leer_punto(self, punto_nombre):
        punto = self.puntos.get(punto_nombre)
        if punto and self.bacnet:
            return self.bacnet.read(f"{self.device_id} {punto['obj']} {punto['instancia']}")
        return None

    def escribir_punto(self, punto_nombre, valor):
        punto = self.puntos.get(punto_nombre)
        if punto and self.bacnet:
            return self.bacnet.write(f"{self.device_id} {punto['obj']} {punto['instancia']}", valor)
        return None

class UMA_Tipico1(UMA):
    def __init__(self, device_id, ip):
        super().__init__(device_id, ip, tipo="T1")
        self.puntos = {
            "Temperatura de Suministro":            {"obj": "analogValue", "instancia": 1},
            "Temperatura de Retorno":               {"obj": "analogValue", "instancia": 2},
            # "Posicion de Valvula":                  {"obj": "analogValue", "instancia": 3},
            "Alarma Termica":                       {"obj": "binaryValue", "instancia": 6},
            "Modo Automático":                      {"obj": "binaryValue", "instancia": 7},
            "Detector de humo":                     {"obj": "binaryValue", "instancia": 9},
            "Alarma Prefiltro":                     {"obj": "binaryValue", "instancia": 10},
            "Alarma Filtro":                        {"obj": "binaryValue", "instancia": 11},
            "Estatus Abanico":                      {"obj": "binaryValue", "instancia": 12},
            "Regulacion de Valvula":                {"obj": "analogValue", "instancia": 13},
            "Comando de Arranque":                  {"obj": "binaryValue", "instancia": 17},
            "Encendido/Apagado del Sistema":        {"obj": "binaryValue", "instancia": 201},
            "Alarma del Sistema":                   {"obj": "binaryValue", "instancia": 202},
            "SetPoint de Temperatura":              {"obj": "analogValue", "instancia": 204},
            "Porcentaje de Apertura de Valvula":    {"obj": "analogValue", "instancia": 208},
            "Modo manual":                          {"obj": "binaryValue", "instancia": 223},
            "Habilitar Horario":                    {"obj": "binaryValue", "instancia": 224},
        }

class UMA_Tipico2(UMA):
    def __init__(self, device_id, ip):
        super().__init__(device_id, ip, tipo="T2")
        self.puntos = {
            "Temperatura de Suministro":            {"obj": "analogValue", "instancia": 1},
            "Temperatura de Retorno":               {"obj": "analogValue", "instancia": 2},
            # "Posicion de Valvula":                  {"obj": "analogValue", "instancia": 3},
            # "Frecuencia del variador":              {"obj": "analogValue", "instancia": 4},
            "Alarma del variador":                  {"obj": "binaryValue", "instancia": 8},
            "Detector de humo":                     {"obj": "binaryValue", "instancia": 9},
            "Alarma Prefiltro":                    {"obj": "binaryValue", "instancia": 10},
            "Alarma Filtro":                       {"obj": "binaryValue", "instancia": 11},
            "Estatus Abanico":                      {"obj": "binaryValue", "instancia": 12},
            "Regulacion de Valvula":                {"obj": "analogValue", "instancia": 13},
            "Regulacion de Frecuencia":             {"obj": "analogValue", "instancia": 14},
            "Comando de Arranque":                  {"obj": "binaryValue", "instancia": 17},
            "Encendido/Apagado del Sistema":        {"obj": "binaryValue", "instancia": 201},
            "Alarma del Sistema":                   {"obj": "binaryValue", "instancia": 202},
            "SetPoint de Temperatura":              {"obj": "analogValue", "instancia": 204},
            "Porcentaje de Apertura de Valvula":    {"obj": "analogValue", "instancia": 208},
            "Frecuencia en Hertz del variador":     {"obj": "analogValue", "instancia": 209},
            "Modo manual":                          {"obj": "binaryValue", "instancia": 223},
            "Habilitar Horario":                    {"obj": "binaryValue", "instancia": 224},
        }

class UMA_Tipico3(UMA):
    def __init__(self, device_id, ip):
        super().__init__(device_id, ip, tipo="T3")
        self.puntos = {
            "Temperatura de Suministro":            {"obj": "analogValue", "instancia": 1},
            "Temperatura de Retorno":               {"obj": "analogValue", "instancia": 2},
            # "Posicion de Valvula":                  {"obj": "analogValue", "instancia": 3},
            # "Frecuencia del variador":              {"obj": "analogValue", "instancia": 4},
            # "Transmisor de CO2":                    {"obj": "analogValue", "instancia": 5},
            # "Transmisor de Humedad":                {"obj": "analogValue", "instancia": 6},
            # "Posicion de Damper de ducto":        {"obj": "analogValue", "instancia": 7},
            "Alarma del variador":                  {"obj": "analogValue", "instancia": 8},
            "Detector de humo":                     {"obj": "binaryValue", "instancia": 9},
            "Alarma Prefiltro":                    {"obj": "binaryValue", "instancia": 10},
            "Alarma Filtro":                       {"obj": "binaryValue", "instancia": 11},
            "Estatus Abanico":                      {"obj": "binaryValue", "instancia": 12},
            "Regulacion de Valvula":                {"obj": "analogValue", "instancia": 13},
            "Regulacion de Frecuencia":             {"obj": "analogValue", "instancia": 14},
            "Regulacion de Calentador":             {"obj": "analogValue", "instancia": 15},
            "Regulacion de Damper":                 {"obj": "analogValue", "instancia": 16},
            "Comando de Arranque":                  {"obj": "binaryValue", "instancia": 17},
            "Comando de Luz Ultravioleta":          {"obj": "binaryValue", "instancia": 18},
            "Encendido/Apagado del Sistema":        {"obj": "binaryValue", "instancia": 201},
            "Alarma del Sistema":                   {"obj": "binaryValue", "instancia": 202},
            "SetPoint de Temperatura":              {"obj": "analogValue", "instancia": 204},
            "SetPoint de CO2":                      {"obj": "analogValue", "instancia": 206},
            "SetPoint de Humedad":                  {"obj": "analogValue", "instancia": 207},
            "Porcentaje de Apertura de Valvula":    {"obj": "analogValue", "instancia": 208},
            "Frecuencia en Hertz del variador":     {"obj": "analogValue", "instancia": 209},
            "Porcentaje de Calentador":             {"obj": "analogValue", "instancia": 210},
            "Porcentaje de Apertura de Damper":   {"obj": "analogValue", "instancia": 211},
            "CO2 ppm":                              {"obj": "analogValue", "instancia": 212},
            "Porcentaje de Humedad Relativa":       {"obj": "analogValue", "instancia": 213},
            "Modo manual":                          {"obj": "binaryValue", "instancia": 223},
            "Habilitar Horario":                    {"obj": "binaryValue", "instancia": 224},
        }

class UMA_Tipico4(UMA):
    def __init__(self, device_id, ip):
        super().__init__(device_id, ip, tipo="T4")
        '''Undevice_idades manejadoras de Quirófanos'''
        self.puntos = {
            "Temperatura de Suministro":            {"obj": "analogValue", "instancia": 1},
            "Transmisor de Temperatura de Retorno": {"obj": "analogValue", "instancia": 2},
            # "Posicion de Valvula":                  {"obj": "analogValue", "instancia": 3},
            # "Frecuencia del variador":              {"obj": "analogValue", "instancia": 4},
            # "Sensor de presion Quir/Pas":           {"obj": "analogValue", "instancia": 5},
            # "Transmisor de Humedad":                {"obj": "analogValue", "instancia": 6},
            # "Transmisor SetPoint Temperatura":      {"obj": "analogValue", "instancia": 7},
            # "Transmisor SetPoint Humedad":          {"obj": "analogValue", "instancia": 8},
            "Detector de humo":                     {"obj": "binaryValue", "instancia": 9},
            "Alarma Prefiltro":                    {"obj": "binaryValue", "instancia": 10},
            "Alarma Filtro":                       {"obj": "binaryValue", "instancia": 11},
            "Estatus Abanico":                      {"obj": "binaryValue", "instancia": 12},
            "Regulacion de Valvula":                {"obj": "analogValue", "instancia": 13},
            "Regulacion de Frecuencia":             {"obj": "analogValue", "instancia": 14},
            "Regulacion de Calentador":             {"obj": "analogValue", "instancia": 15},
            "Regulacion de Damper":                 {"obj": "analogValue", "instancia": 16},
            "Comando de Arranque":                  {"obj": "binaryValue", "instancia": 17},
            "Comando de Luz Ultravioleta":          {"obj": "binaryValue", "instancia": 18},
            "Encendido/Apagado del Sistema":        {"obj": "binaryValue", "instancia": 201},
            "Alarma del Sistema":                   {"obj": "binaryValue", "instancia": 202},
            "SetPoint de Temperatura":              {"obj": "analogValue", "instancia": 204}, # Sólo lectura
            "SetPoint de Presión":                  {"obj": "analogValue", "instancia": 206},
            "SetPoint de Humedad":                  {"obj": "analogValue", "instancia": 207}, # Sólo lectura
            "Porcentaje de Apertura de Valvula":    {"obj": "analogValue", "instancia": 208},
            "Frecuencia en Hertz del variador":     {"obj": "analogValue", "instancia": 209},
            "Porcentaje de Calentador":             {"obj": "analogValue", "instancia": 210},
            "Porcentaje de Apertura de Damper":   {"obj": "analogValue", "instancia": 211},
            "Temperatura en Quirofano":             {"obj": "analogValue", "instancia": 212},
            "Humedad Relativa en Quirofano":        {"obj": "analogValue", "instancia": 213},
            "Presion en Quirofano":                 {"obj": "analogValue", "instancia": 214},
            "Alarma Filtro HEPA":                   {"obj": "binaryValue", "instancia": 217},
            "Modo manual":                          {"obj": "binaryValue", "instancia": 223},
            "Habilitar Horario":                    {"obj": "binaryValue", "instancia": 224},
        }

# class Modulo_Tipico4(UMA):
#     def __init__(self, device_id, ip):
#         super().__init__(device_id, ip, tipo="M4")
#         '''Módulo adicional para Undevice_idades manejadoras de Quirófanos'''
#         self.puntos = {
#             "Sensor de presion filtro HEPA":            {"obj": "analogValue", "instancia": 1} # Valdevice_idar
#         }

class UMA_Tipico5(UMA):
    def __init__(self, device_id, ip):
        super().__init__(device_id, ip, tipo="T5")
        self.puntos = {
            "Temperatura de Suministro":            {"obj": "analogValue", "instancia": 1},
            "Temperatura de Retorno":               {"obj": "analogValue", "instancia": 2},
            "Frecuencia del variador":              {"obj": "analogValue", "instancia": 3},
            "Estatus Compresor 1":                  {"obj": "binaryValue", "instancia": 4},
            "Estatus Compresor 2":                  {"obj": "binaryValue", "instancia": 5},
            # "Transmisor de Humedad":                {"obj": "analogValue", "instancia": 6},
            # "Posicion de Damper de ducto":        {"obj": "analogValue", "instancia": 7},
            "Alarma del variador":                  {"obj": "analogValue", "instancia": 8},
            "Detector de humo":                     {"obj": "binaryValue", "instancia": 9},
            "Alarma Prefiltro":                    {"obj": "binaryValue", "instancia": 10},
            "Alarma Filtro":                       {"obj": "binaryValue", "instancia": 11},
            "Estatus Abanico":                      {"obj": "binaryValue", "instancia": 12},
            "Regulacion de Frecuencia":             {"obj": "binaryValue", "instancia": 14},
            "Comando de Arranque y Ultravioleta":                  {"obj": "binaryValue", "instancia": 17},
            "Comando ODU 1":          {"obj": "binaryValue", "instancia": 18},
            "Comando ODU 2":          {"obj": "binaryValue", "instancia": 18},
            "Comando Líneas de Vapor":          {"obj": "binaryValue", "instancia": 18},
            "Comando Etapa 1&2 Resistencia":          {"obj": "binaryValue", "instancia": 18},
            "Comando Etapa 3 Resistencia":          {"obj": "binaryValue", "instancia": 18},
            "Encendido/Apagado del Sistema":        {"obj": "binaryValue", "instancia": 201},
            "Alarma del Sistema":                   {"obj": "binaryValue", "instancia": 202},
            "SetPoint de Temperatura":              {"obj": "analogValue", "instancia": 204},
            "SetPoint de Humedad":                  {"obj": "analogValue", "instancia": 207},
            "Frecuencia en Hertz del variador":     {"obj": "analogValue", "instancia": 209},
            "Porcentaje de Humedad Relativa":       {"obj": "analogValue", "instancia": 213},
            "Modo manual":                          {"obj": "binaryValue", "instancia": 223},
            "Habilitar Horario":                    {"obj": "binaryValue", "instancia": 224},
        }

class UMA_Tipico6(UMA):
    def __init__(self, device_id, ip):
        super().__init__(device_id, ip, tipo="T6")
        self.puntos = {
            "Temperatura de Suministro":            {"obj": "analogValue", "instancia": 1},
            "Temperatura de Retorno":               {"obj": "analogValue", "instancia": 2},
            # "Posicion de Valvula":                  {"obj": "analogValue", "instancia": 3},
            # "Sensor de presion filtro HEPA":                  {"obj": "analogValue", "instancia": 3},
            "Alarma Termica":                       {"obj": "binaryValue", "instancia": 6},
            "Modo Automático":                      {"obj": "binaryValue", "instancia": 7},
            "Detector de humo":                     {"obj": "binaryValue", "instancia": 9},
            "Alarma Prefiltro":                     {"obj": "binaryValue", "instancia": 10},
            "Alarma Filtro":                        {"obj": "binaryValue", "instancia": 11},
            "Estatus Abanico":                      {"obj": "binaryValue", "instancia": 12},
            "Regulacion de Valvula":                {"obj": "analogValue", "instancia": 13},
            "Comando de Arranque":                  {"obj": "binaryValue", "instancia": 17},
            "Encendido/Apagado del Sistema":        {"obj": "binaryValue", "instancia": 201},
            "Alarma del Sistema":                   {"obj": "binaryValue", "instancia": 202},
            "SetPoint de Temperatura":              {"obj": "analogValue", "instancia": 204},
            "Presion en filtro HEPA":               {"obj": "analogValue", "instancia": 204},
            "Alarma filtro HEPA":                   {"obj": "binaryValue", "instancia": 204},
            "Porcentaje de Apertura de Valvula":    {"obj": "analogValue", "instancia": 208},
            "Modo manual":                          {"obj": "binaryValue", "instancia": 223},
            "Habilitar Horario":                    {"obj": "binaryValue", "instancia": 224},
        }

class UMA_Tipico7(UMA):
    def __init__(self, device_id, ip):
        super().__init__(device_id, ip, tipo="T7")
        self.puntos = {
            "Temperatura de Suministro":            {"obj": "analogValue", "instancia": 1},
            "Temperatura de Retorno":               {"obj": "analogValue", "instancia": 2},
            # "Posicion de Valvula":                  {"obj": "analogValue", "instancia": 3},
            # "Frecuencia del variador":              {"obj": "analogValue", "instancia": 4},
            "Alarma del variador":                  {"obj": "binaryValue", "instancia": 8},
            "Detector de humo":                     {"obj": "binaryValue", "instancia": 9},
            "Alarma Prefiltro":                    {"obj": "binaryValue", "instancia": 10},
            "Alarma Filtro":                       {"obj": "binaryValue", "instancia": 11},
            "Estatus Abanico":                      {"obj": "binaryValue", "instancia": 12},
            "Regulacion de Valvula":                {"obj": "analogValue", "instancia": 13},
            "Regulacion de Frecuencia":             {"obj": "analogValue", "instancia": 14},
            "Regulacion de Calentador":             {"obj": "analogValue", "instancia": 15},
            "Comando de Arranque":                  {"obj": "binaryValue", "instancia": 17},
            "Encendido/Apagado del Sistema":        {"obj": "binaryValue", "instancia": 201},
            "Alarma del Sistema":                   {"obj": "binaryValue", "instancia": 202},
            "SetPoint de Temperatura":              {"obj": "analogValue", "instancia": 204},
            "Porcentaje de Apertura de Valvula":    {"obj": "analogValue", "instancia": 208},
            "Frecuencia en Hertz del variador":     {"obj": "analogValue", "instancia": 209},
            "Porcentaje de Calentador":             {"obj": "analogValue", "instancia": 210},
            "Modo manual":                          {"obj": "binaryValue", "instancia": 223},
            "Habilitar Horario":                    {"obj": "binaryValue", "instancia": 224},
        }

class UMA_Tipico8(UMA):
    def __init__(self, device_id, ip):
        super().__init__(device_id, ip, tipo="T8")
        self.puntos = {
            "Temperatura de Suministro":            {"obj": "analogValue", "instancia": 1},
            "Temperatura de Retorno":               {"obj": "analogValue", "instancia": 2},
            # "Posicion de Valvula":                  {"obj": "analogValue", "instancia": 3},
            # "Frecuencia del variador":              {"obj": "analogValue", "instancia": 4},
            "Alarma del variador":                  {"obj": "binaryValue", "instancia": 8},
            "Detector de humo":                     {"obj": "binaryValue", "instancia": 9},
            "Alarma Prefiltro":                     {"obj": "binaryValue", "instancia": 10},
            "Alarma Filtro":                        {"obj": "binaryValue", "instancia": 11},
            "Estatus Abanico":                      {"obj": "binaryValue", "instancia": 12},
            "Regulacion de Valvula":                {"obj": "analogValue", "instancia": 13},
            "Regulacion de Frecuencia":             {"obj": "analogValue", "instancia": 14},
            "Comando de Arranque":                  {"obj": "binaryValue", "instancia": 17},
            "Comando Luz Ultravioleta":             {"obj": "binaryValue", "instancia": 18},
            "Encendido/Apagado del Sistema":        {"obj": "binaryValue", "instancia": 201},
            "Alarma del Sistema":                   {"obj": "binaryValue", "instancia": 202},
            "SetPoint de Temperatura":              {"obj": "analogValue", "instancia": 204},
            "Porcentaje de Apertura de Valvula":    {"obj": "analogValue", "instancia": 208},
            "Frecuencia en Hertz del variador":     {"obj": "analogValue", "instancia": 209},
            "Habilitar Horario":                    {"obj": "binaryValue", "instancia": 224},
            "Modo manual":                          {"obj": "binaryValue", "instancia": 223},
        }