# Swim Tracker
Aplicacion pensada para que los entrenadores y alumnos lleven registro de los tiempos para cada estilo en diferentes distancias y permitiendo comparar 2 o mas entradas.
<br> <br> <br>
**Que nos ofrece?**
- Login para definir que perfil mostrar: Entrenadores o Admin.
- El Admin, va a poder dar de alta, modificar o deshabilitar perfiles de Entrenador.
- El Entrenador, va a poder dar de alta alumnos:
     - Registro del tiempo (MM:SS) por alumno (Nombre y Apellido) para los 4 estilos (crol, espalda, pecho, mariposa).
     - Modificacion del tiempo previamente registrado.
     - Consulta de los tiempos de cada alumno.
     - Deshabilitar alumno.
     - Borrar alumno (junto con todos los tiempos).

## Funciones de Menu  

**Login**
- Pedir User y Password:
     - User
     - Password
- Dependiendo del rol de las credenciales usadas, el usuario va a ver el Menu Admin, o el Menu Entrenador.

      
**Menu Admin**
- Que desea hacer?:
     - Crear Usuario.
     - Resetear Password de Usuario.
     - Listar Usuarios.
     - Deshabilitar Usuario.
  
**Menu Entrenadores**
- Que desea hacer?:
     - Crear Alumno.
     - Cargar tiempo para Alumno.
     - Listar tiempos por Alumno.
     - Listar mejores tiempos por distancia y estilo.
     - Busqueda por nombre de alumno.
     - Modificar Alumno.
     - Deshabilitar Alumno.
     - Eliminar Alumno.

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
    - Usar regex en lo posible para validar lo anterior.
    - Que se guarde hasheada (posbiles librerias bcrypt or passlib).
    - Manejo de errores para lo requerido anteriormente.

**Actualizar User Password**
- Listar a todos los users.
- Seleccionar un user para cambiarle el password (usando un ID).
- La nueva Password debe tener las mismas caracteristicas que cuando se da de alta un user.
- Mostrar mensaje que describa actualización de password exitosa.

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
         - Formato DD/MM/AAAA.
     - Edad:
         - Calculada con la fecha de cumpleaños, no se pide cargar.
- Modificar Alumno:
     - Agregar tiempos por estilo.
     - Cambiar nombre.
- Deshabilitar Alumno.
- Eliminar Alumno. 
           
## Base de datos

<img width="622" alt="image" src="https://github.com/matias-espinosa/swim_tracker/assets/19157242/298968db-ad16-4773-8e84-294ded49dd3c">

