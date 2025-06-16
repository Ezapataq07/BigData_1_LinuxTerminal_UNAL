# Basic Operations Over Text Files

## Download file with wget
``` bash
wget https://raw.githubusercontent.com/jdvelasq/playground/master/datasets/orders.csv
iconv -f ISO-8859-1 -t utf-8 orders.csv -o orders1.csv
mv orders1.csv orders.csv
```

## head
``` bash
#
# Visualización de la cabecera del archivo
#
head orders.csv
```

``` bash
#
# Primeras 5 lineas del archivo
#
head -n 5 orders.csv
```

## tail
``` bash
#
# Visualización de la cola del archivo
#
tail orders.csv
```

``` bash
#
# Visualización de las últimas 3 lineas del archivo
#
tail -n 3 orders.csv
```

``` bash
#
# Visualización desde la linea 4115 hasta el final
#
tail +4115 orders.csv
```

## more y less
Unix también proporciona los comandos `more` (versión más antigua) y `less` para la visualización del contenido de archivos. Simplemente digite less ``nombrearchivo`` para iniciar la visualización.

* Use la tecla Space para avanzar una página.

* Use Ctrl-F (Forward) y Ctrl-B (Backward) para avanzar o retroceder una página.

* Use las teclas arriba y abajo para moverse una línea a la vez.

* Digite el número de línea y G (go to) para ir a una línea determinada.

* Digite q para salir de less


# nl 
``` bash
#
# Numeración de las lineas
#
nl orders.csv | tail -n 5
```

``` bash
#
# Visualización de las columnas del archivo
#
head -n 1 orders.csv | tr ';' '\n'
```

``` bash
# Conteo de la cantidad de columnas
head -n 1 orders.csv | tr ';' '\n' | wc -l
```

``` bash
#
# Obtención de un subconjunto de registros al inicio del archivo
#
head -n 11 orders.csv > orders-head.csv
cat orders-head.csv
```

``` bash
#
# Obtención de un subconjunto de registros al final del archivo
#
tail -n 10 orders.csv > orders-tail.csv
cat orders-tail.csv
```

``` bash
#
# Obtención de un subconjunto de registros en un punto intermedio
#
head -n 11 orders.csv | tail -n 6 > orders-med.csv
cat orders-med.csv
```

``` bash
#
# Obtención de un grupo de columnas con cut
#
cut -d";" -f2 orders-head.csv
```

``` bash
#
# Obtención de un grupo de columnas con cut
#
cut -d";" -f2,4-6 orders-head.csv
```

``` bash
#
# Ordenamiento de líneas
#
head -n 20 orders.csv | tail +2  | cut -d";" -f6 | sort
```

``` bash
#
# Obtención de líneas únicas (parte 1)
#
head -n 20 orders.csv | tail +2  | cut -d";" -f6
```

``` bash
#
# Obtención de líneas únicas (parte 2)
#
head -n 20 orders.csv | tail +2  | cut -d";" -f6 | uniq
```

``` bash
#
# Obtención de líneas únicas (parte 3)
#
head -n 20 orders.csv | tail +2  | cut -d";" -f6 | sort | uniq
```

``` bash
#
# Conteo de la cantidad de regiones
#
head -n 20 orders.csv | tail +2  | cut -d";" -f6 | sort | uniq | wc -l
```

``` bash
#
# Búsqueda de patrones con grep
#
grep 'Central'  orders.csv | head
```

``` bash
#
# Lineas que tengan Germany
#
cat orders.csv | grep Germany | head -n 5
```

``` bash
#
# Se desean ver las 3 lineas antes de la primera aparición de Germany
#
nl orders.csv | grep Germany | head -n 5
```

``` bash
#
# La primera aparición es en la línea 13, entonces se desean visualizar las
# lineas 10, 11 y 12
#
nl orders.csv | tail +10 | head -n 3
```