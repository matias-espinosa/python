# Swim Tracker
Aplicacion pensada para que los entrenadores lleven registro del tiempo de cada estilo en diferentes distancias.
<br> <br> <br>
**Que nos ofrece?**
- Un menu para elegir entre Entrenadores (que van a tener varios alumnos) o Admin (que da de alta a los entrenadores)
- Alta de Swimming Tracker user (Usuario y Password) para dar de alta diferentes tiempos de cada alumno.
- Registro del tiempo (MM:SS) por alumno (Nombre y Apellido) para los 4 estilos (crol, espalda, pecho, mariposa).
- Modificacion del tiempo previamente registrado.
- Consulta de los tiempos de cada alumno.
- Borrar alumno (junto con todos los tiempos).

## Menu  

- Login para Entrenadores
     - User Name
     - Password
- Login para Admin
    - User Name
    - Passowrd
        - Crear Usuario
        - Resetear Password de Usuario
        - Listar Usuarios
        - Eliminar Usuario

## Funciones para el Admin

**Alta de usuario**  

- Crear un Username:
    - No puede contener espacios.
    - Se guarda en mayusculas.
    - No puede contener caracteres epeciales.
    - No puede contener numeros.
    - Validar que sea unico.
    - Manejo de errores para lo requerido anteriormente.
- Crear Password:
    - 4 a 8 caracteres.
    - Al menos 1 caracter especial.
    - Al menos 1 mayuscula.
    - Al menos 1 minuscula.
    - Al menso 1 numero.
    - Que se guarde hasheada (posbiles librerias bcrypt or passlib)
    - Manejo de errores para lo requerido anteriormente.

**Actualizar User Password**
- Listar todos los users.
- Seleccionar un user para cambiarle el password (usando un ID).
- La nueva Password debe tener las mismas caracteristicas que cuando se da de alta un user.
- Mostrar mensaje que describa actualización de password exitosa

**Baja de usuario**
- Listar todos los users.
- Seleccionar un user para ser eliminado (usando un ID).
- Mostrar mensaje que describa eliminacion de user exitosa
