class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

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
            dni, nombre, tiempo = args
            print(f"Alta de registro Observador: {nombre}, DNI:{dni}, tiempo de 50 metros crol {tiempo}")

class ModificacionRegistro(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, tipo_notificacion, *args):
        if tipo_notificacion == 'modificar':
            dni, nombre, tiempo = args
            print(f"El registro ha sido modificado Observador: {nombre}, DNI: {dni}, tiempo de 50 metros crol: {tiempo}")

class BajaRegistro(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, tipo_notificacion, *args):
        if tipo_notificacion == 'baja':
            dni, nombre, tiempo = args
            print(f"El registro ha sido eliminado Observador: {nombre}, DNI: {dni}")