"""
Ejercicio8
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
"""
import pprint

def main():
    diccionario = {}
    key_inicial = 0
    opcion = 1

    while opcion != 0:
        print(" ")
        print("-= Bienvenido a Verdulerias tech =-")
        print("1= Nueva compra")
        print("2= Modificar una compra")
        print("3= Consutlar estado de la compra")
        print("4= Eliminar una compra")
        print("0= Salir")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            alta(diccionario, key_inicial)
            key_inicial += 1
        elif opcion == 2:
            modificacion(diccionario)
        elif opcion == 3:
            consulta(diccionario)
        elif opcion == 4:
            consulta(diccionario)
            baja(diccionario)


def alta(diccionario, key):
    verdura = input("Ingrese la verdura a comprar: ")
    try:
        cantidad = float(input(f"Ingrese la cantidad en kg de {verdura}: "))
    except ValueError:
        print(f"{cantidad} no es un valor valido.")
        return diccionario
    try:
        precio = float(input(f"Ingrese el precio por kg de {verdura}: "))
    except ValueError:
        print(f"{precio} no es un valor valido.") 
        return diccionario
    salio = precio * cantidad
    diccionario[key] = {"verdura": verdura, "cantidad en kg": cantidad,"precio por kg": precio, f"total gastado en {verdura}": f"{salio} pesos"}
    return diccionario

def consulta(diccionario):
    pprint.pprint(diccionario)

def buscar_verdura(diccionario):
    verdura_a_buscar = input("Ingrese verdura buscada: ")
    #aca le paso al for la posicion y los datos de una tupla, y el .items 
    #esto se llama unpacking
    #          V
    for position, data in diccionario.items():
        if verdura_a_buscar == data["verdura"]:
            return position
        """ tambien podria hacerlo asi, donde x seria el key del diccionario:
    for x in diccionario:
        if verdura_a_buscar == diccionario[x]["verdura"]:
            return x
"""

def modificacion(diccionario):
    posicion_buscada = buscar_verdura(diccionario)
    #si buscar verdura no lo encuentra devuelve none
    if posicion_buscada == None:
        print("No se ha encontrado esa verdura")
        return
    else:
        alta(diccionario,posicion_buscada)

def baja(diccionario):
    valor_a_eliminar = int(input("Ingrese el numero de compra a eliminar: "))
    try:
        diccionario.pop(valor_a_eliminar)
    #aca si alguno de los inputs no es valido, el programa no crashea
    except KeyError:
        print(f"Compra {valor_a_eliminar} no encontrada. No se elimino ninguna compra.")

    #no have falta xq pop ya lo modifica al diccionario: 
    #return diccionario
    
main()