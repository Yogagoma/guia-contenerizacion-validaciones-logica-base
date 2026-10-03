# guia-contenerizacion-validaciones-logica-base
Ejercicios prácticos sobre contenerización, validaciones de datos y lógica de programación. Desarrollados por tres equipos

## Consideraciones
Para ejecutar estos programas, se requiere la instalación de:

1. Python 3.10 o superior.
2. Docker Desktop o Docker Engine.
3. XAMPP.

Para obtener el repositorio, puede descargar el archivo comprimido (.zip) o, teniendo instalado Git, clonar el repositorio ejecutando:

``` sh
git clone https://github.com/Yogagoma/guia-contenerizacion-validaciones-logica-base.git
```

## Reto 1
Creación conjunta de un archivo docker-compose.yml para levantar dos contenedores, uno con una base de datos postgreSQL y otra con un servidor web fastAPI.

Una vez clonado el repositorio, debe añadir en la raíz de este un archivo .env con los siguientes datos:

``` sh
POSTGRES_USER: postgres
POSTGRES_PASSWORD: pgAdmin
POSTGRES_DB: Prueba
```

Seguidamente, para levantar los contenedores, ejecute:
``` sh
docker compose up -d
```

#### NOTA:
El directorio app con el archivo main.py solo existen para el levantamiento correcto del servicio web, cumpliendo com las especificaciones escritas en el Dockerfile.
## Reto 2

Script escrito en PHP que contienen funciones usando preg_match para limpiar datos de entrada, de manera que cumplan con el propósito de:

1. Validar un formato estricto de correo electrónico. 

2. Validar un formato de número telefónico y Cédula de Identidad. 

3. Aplicar sanitización básica simulando la prevención de un ataque XSS.

Se debe contar con XAMPP para permitir la creacion del servidor local de PHP.

Para encender dicho servidor se debe ejecutar en el terminal (asegurandose de que el terminal este ubicado en la carpeta que almacena el archivo) el comando:

``` sh
php -S localhost:8000
```

Una vez se haya levantado el servidor se debe ingresar en el navegador el URL

``` sh
http://localhost:8000/validaciones.php 
```
Lo cual muestra la interfaz del programa creada con un script de HTML

## Reto 3
Función que recibe dos rangos de horas y retorna True, si estos chocan y False, en caso contrario.

Posee un bloque try-except para ejecutar la comparación entre los rangos y capturar excepciones en caso de no cumplir con el formato 'HH:MM-HH:MM', un rango comience y termine a la misma hora o este culmine antes de empezar.

Los rangos son recibidos como cadenas y después son convertidos en tuplas con objetos datetime para la posterior evaluación de la condición de choque de horarios.

Para probar el programa, ejecute:
``` sh
python funcion_horarios.py
```