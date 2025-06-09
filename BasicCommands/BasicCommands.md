# Basic Commands

Estas tareas son fácilmente realizables usando la línea de comandos de Linux. Por ejemplo, el comando:

``grep ^2015 datos.csv``

permite imprimir en pantalla los registros del año 2015; para grabar los resultados en el archivo 2015.csv solo es necesario modificar ligeramente el comando anterior:

``grep ^2015 datos.csv > 2015.csv``

## pwd
``` bash
#
# Imprime el directorio de trabajo
#
pwd
```

## whoami
``` bash
#
# Imprime el nombre de usuario
#
whoami
```

## ls
``` bash
#
# Lista el contenido del directorio
#
ls
```

``` bash
#
# listado detallado (letra l)
#
# Al principio de cada línea hay una cadena de diez caracteres, por ejemplo
# `-rw-r--r--`. El primer carácter indica si el elemento es un archivo (`-`)
# o un directorio (`d`). Luego siguen tres grupos de tres caracteres que
# indican:
#
#   * Permisos de usuario.
#   * Permisos de grupo.
#   * Otros permisos.
#
# En su orden, los tres caracteres de cada grupo representan lo siguiente:
#
# * Si el archivo tiene permiso de lectura (`r`) o no (`-`).
# * Si el archivo tiene permiso de escritura (`w`) o no (`-`).
# * Si el archivo es ejecutable (`x`) o no (`-`); consulte la ayuda de `ls`
# para obtener más opciones.
#
# Por ejemplo, la cadena `-rwxr-xr-x` indica que el elemento es un archivo
# (`-`), que el usuario (dueño) tiene permisos de lectura y escritura (`rw`),
# que el archivo es ejecutable (`x`) y que otros usuarios solo pueden leerlo
# (`r--`).
#
ls -l

-rw-rw-r-- 1 ezapataq ezapataq   9574885 Jun  9 17:31 2015.csv
-rw-rw-r-- 1 ezapataq ezapataq       527 Jun  9 17:40 Commands.md
-rw-rw-r-- 1 ezapataq ezapataq 105226710 Jun  9 17:19 datos.csv
-rw-rw-r-- 1 ezapataq ezapataq      1834 Jun  9 17:18 generate_large_csv.py
```

``` bash
#
# Solo los nombres de los archivos (número 1)
#
ls -1

2015.csv
Commands.md
datos.csv
generate_large_csv.py
```

``` bash
#
# Incluye archivos ocultos
#
ls -la
```

## >

``` bash
#
# Redirecciona la salida a un archivo:
#
ls -la > listado.txt
#
# Contenido de lista.txt
#
cat listado.txt

total 112140
drwxrwxr-x 3 ezapataq ezapataq      4096 Jun  9 17:45 .
drwxrwxr-x 3 ezapataq ezapataq      4096 Jun  9 16:58 ..
-rw-rw-r-- 1 ezapataq ezapataq   9574885 Jun  9 17:31 2015.csv
-rw-rw-r-- 1 ezapataq ezapataq      1793 Jun  9 17:43 Commands.md
-rw-rw-r-- 1 ezapataq ezapataq 105226710 Jun  9 17:19 datos.csv
-rw-rw-r-- 1 ezapataq ezapataq      1834 Jun  9 17:18 generate_large_csv.py
-rw-rw-r-- 1 ezapataq ezapataq         0 Jun  9 17:45 listado.txt
drwxrwxr-x 5 ezapataq ezapataq      4096 Jun  9 17:18 .venv
```

## >>

``` bash
# Agrega la salida a un archivo
#
ls -la >> listado.txt
# Contenido de lista.txt
#
cat listado.txt

total 112140
drwxrwxr-x 3 ezapataq ezapataq      4096 Jun  9 17:45 .
drwxrwxr-x 3 ezapataq ezapataq      4096 Jun  9 16:58 ..
-rw-rw-r-- 1 ezapataq ezapataq   9574885 Jun  9 17:31 2015.csv
-rw-rw-r-- 1 ezapataq ezapataq      1793 Jun  9 17:43 Commands.md
-rw-rw-r-- 1 ezapataq ezapataq 105226710 Jun  9 17:19 datos.csv
-rw-rw-r-- 1 ezapataq ezapataq      1834 Jun  9 17:18 generate_large_csv.py
-rw-rw-r-- 1 ezapataq ezapataq         0 Jun  9 17:45 listado.txt
drwxrwxr-x 5 ezapataq ezapataq      4096 Jun  9 17:18 .venv
total 112144
drwxrwxr-x 3 ezapataq ezapataq      4096 Jun  9 17:45 .
drwxrwxr-x 3 ezapataq ezapataq      4096 Jun  9 16:58 ..
-rw-rw-r-- 1 ezapataq ezapataq   9574885 Jun  9 17:31 2015.csv
-rw-rw-r-- 1 ezapataq ezapataq      2543 Jun  9 17:46 Commands.md
-rw-rw-r-- 1 ezapataq ezapataq 105226710 Jun  9 17:19 datos.csv
-rw-rw-r-- 1 ezapataq ezapataq      1834 Jun  9 17:18 generate_large_csv.py
-rw-rw-r-- 1 ezapataq ezapataq       521 Jun  9 17:45 listado.txt
drwxrwxr-x 5 ezapataq ezapataq      4096 Jun  9 17:18 .venv
```

## <

``` bash
#
# Usa el contenido de un archivo como entrada
#
wc < listado.txt

18  148 1042  
# Num lines | Num words | Num characters
```

## |

``` bash
#
# Indica que la salida de un comando es la entrada del siguiente
# Cuenta cuantas palabras hay en el listado
#
ls -la | wc

9      74     521
```

## Ayuda

``` bash
#
# Se usa --help o -h
#
ls --help
```