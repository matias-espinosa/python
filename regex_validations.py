import re

class ValidationUtils():
    @staticmethod
    def validate_dni(dni):
        """**Metodo que valida el campo DNI**"""
        dni_str = str(dni)
        regex_dni = r'^\d{7,8}$'
        return bool(re.match(regex_dni, dni_str))

    @staticmethod
    def validate_tiempo(tiempo_50_mts):
        """**Metodo que valida el campo Tiempo**"""
        regex_tiempo = "([0-9]{2}):([0-5][0-9])$"
        return bool(re.match(regex_tiempo, tiempo_50_mts))