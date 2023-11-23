# Swim Tracker
Aplicacion pensada para que los entrenadores lleven registro del tiempo de sus alumnos para cada estilo, en diferentes distancias.
<br> <br> <br>
**Que nos ofrece?**
- Un menu para elegir entre Entrenadores (que van a tener varios alumnos) o Entrenador

(que da de alta a los entrenadores)
- Alta de Swimming Tracker user (Usuario y Password) para dar de alta diferentes tiempos de cada alumno.
- Registro del tiempo (MM:SS) por alumno (Nombre y Apellido) para los 4 estilos (crol, espalda, pecho, mariposa).
- Modificacion del tiempo previamente registrado.
- Consulta de los tiempos de cada alumno.
- Borrar alumno (junto con todos los tiempos).

## Funciones de Menu  

**Menu Principal**
- Como se desea identificar?:
     - Entrenador
          - User Name
          - Password
     - Admin
         - User Name
         - Passowrd
      
**Menu Admin**
- Que desea hacer?
     - Crear Usuario
     - Resetear Password de Usuario
     - Listar Usuarios
     - Eliminar Usuario
  
**Menu Entrenadores**


## Funciones para el Admin

**Alta de User**  

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

**Deshabilitar User**
- Listar todos los users.
- Seleccionar un user para ser deshabilitado (usando un ID).
- Mostrar mensaje que describa la desabilitacion exitosa del user.

## Funciones para el Entrenador

**Alta de alumno**

- Crear Alumno:
     - Nombre de Pila:
         - No puede contener espacios.
         - Se guarda en mayusculas.
         - No puede contener caracteres epeciales.
         - No puede contener numeros.
     - Apellido:
         - No puede contener espacios.
         - Se guarda en mayusculas.
         - No puede contener caracteres epeciales.
         - No puede contener numeros.
     - Fecha de cumpleaños:
         - Formato DD/MM/AAAA
     - Edad:
         - Calculada con la fecha de cumpleaños, no se pide cargar
           
## Base de datos

<img width="622" alt="image" src="https://github.com/matias-espinosa/swim_tracker/assets/19157242/298968db-ad16-4773-8e84-294ded49dd3c">

