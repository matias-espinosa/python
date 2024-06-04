import re

class ValidationUtils():
    @staticmethod
    def validar_dni(dni):
        """**Metodo que valida el campo DNI**"""
        dni_str = str(dni)
        regex_dni = r'^\d{7,8}$'
        return bool(re.match(regex_dni, dni_str))

    @staticmethod
    def validar_tiempo(tiempo):
        """**Metodo que valida el campo Tiempo**"""
        regex_tiempo = r'([0-9]{2}):([0-5][0-9])$'
        return bool(re.match(regex_tiempo, tiempo))

    @staticmethod
    def validate_fullname(nombre):
        """**Metodo que valida el nombre completo**"""
        regex_fullname = r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ]+(?:\s[a-zA-ZáéíóúÁÉÍÓÚüÜ]+)*$'
        return bool(re.match(regex_fullname, nombre))

    @staticmethod
    def validar_nombre(nombre):
        """**Metodo que valida el nombre completo**"""
        regex_nombre = r"^[A-ZÁÉÍÓÚÜÑa-záéíóúüñ]+(([' -][A-ZÁÉÍÓÚÜÑa-záéíóúüñ])?[A-ZÁÉÍÓÚÜÑa-záéíóúüñ]*)*$"
        return bool(re.match(regex_nombre, nombre))

    @staticmethod
    def validar_apellido(apellido):
        """**Metodo que valida el nombre completo**"""
        regex_apellido = r"^[A-ZÁÉÍÓÚÜÑa-záéíóúüñ]+([ '-][A-ZÁÉÍÓÚÜÑa-záéíóúüñ]+)*$"
        return bool(re.match(regex_apellido, apellido))