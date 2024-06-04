from base_de_datos import Database
import random

first_names = [
    "Sofía", "Martín", "Lucía", "Lucas", "María", "Hugo", "Carmen", "Mateo", "Ana", "Leo",
    "Laura", "Daniel", "Valentina", "Alejandro", "Marta", "Pablo", "Paula", "Adrián", "Sara", "David"
]

last_names = [
    "García", "Martínez", "López", "Sánchez", "Pérez", "González", "Rodríguez", "Fernández", "Moreno", "Jiménez",
    "Hernández", "Díaz", "Muñoz", "Álvarez", "Romero", "Gutiérrez", "Ruiz", "Torres", "Vázquez", "Domínguez"
]

def generate_random_data():
    randomDni = random.randrange(10000000, 99999999)
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    estilo = random.choice(['mariposa', 'espalda', 'pecho', 'crol'])
    distancia = random.choice(['50', '100', '200', '500', '1000', '2000'])
    randomTime1 = str(random.randrange(0, 9))
    randomTime2 = str(random.randrange(0, 9))
    randomTime = '0' + randomTime1 + ':' + '0' + randomTime2
    return randomDni, first_name, last_name, estilo, distancia, randomTime

def llenar_base():
    db = Database()
    db.conexion()
    cursor = db.con.cursor()
    for i in range(100):
        data = generate_random_data()
        sql = "INSERT INTO alumnos (dni, nombre, apellido, estilo, distancia, tiempo) VALUES (?, ?, ?, ?, ?, ?);"
        cursor.execute(sql, data)
        db.con.commit()

llenar_base()