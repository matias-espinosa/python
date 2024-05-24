class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    #def quitar(self, obj):
    #    pass

    def notificar(self, tipo_notificacion, *args):
        for observador in self.observadores:
            observador.update(tipo_notificacion, *args)

class Observador:
    def update(self, tipo_notificacion, *args):
        raise NotImplementedError("Delegación de actualización")

class AltaRegistro(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, tipo_notificacion, *args):
        if tipo_notificacion == 'alta':
            dni, nombre, tiempo_50_mts = args
            print(f"Alta de registro: {nombre}, DNI:{dni}, tiempo de 50 metros crol {tiempo_50_mts}")

class ModificacionRegistro(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, tipo_notificacion, *args):
        if tipo_notificacion == 'modificar':
            dni, nombre, tiempo_50_mts = args
            print(f"El registro ha sido modificado: {nombre}, DNI: {dni}, tiempo de 50 metros crol: {tiempo_50_mts}")

class BajaRegistro(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, tipo_notificacion, *args):
        if tipo_notificacion == 'baja':
            dni, nombre, tiempo_50_mts = args
            print(f"El registro ha sido eliminado: {nombre}, DNI: {dni}")