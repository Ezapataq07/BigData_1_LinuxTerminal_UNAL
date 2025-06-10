# Basic Commands

## echo
``` bash
#
# echo
#
echo hola     mundo   cruel!

hola mundo cruel!
```

``` bash
#
# echo
#
echo "hola
mundo
cruel"

hola
mundo
cruel
```

``` bash
#
# El caracter \ indica continuación y debe ser el último caracter de la línea
#
echo linea 1 \
linea 2 \
linea 3

linea 1 linea 2 linea 3
```

``` bash
#
# Retorno de carro "\n"
#
echo -e "linea 1\nlinea 2\nlinea 3"

linea 1
linea 2
linea 3
```

## printf
``` bash
#
# Impresión con printf:
#   * `%s` indica cadena de caracteres.
#   * `%f` indica un número en punto flotante.
#   * `%i` indica un número entero.
#
printf '%s ---- %f ---- %g' 'hola mundo'  1.23456789 1.23456789

hola mundo ---- 1.234568 ---- 1
```

``` bash
#
# Impresion con formato
#
printf '%15s --- %8.2f'  hola   1.23456789

           hola ---     1.23
```

## seq
``` bash
#
# seq se usa para imprimir secuencias de números.
#
seq 5
```

``` bash
#
# String con formato.
#
seq -f"linea %g" 5

linea 1
linea 2
linea 3
linea 4
linea 5
```

``` bash
#
# -s permite especificar el separador
# En este ejmplo el separador es la coma
#
seq -s, 2 2 10

2,4,6,8,10
```

``` bash
#
# La opción `-w` permite especificar formato.
# Valor inicial, incremento y valor final
#
seq 0 .05 .1

0.00
0.05
0.10
```

``` bash
seq -w 0 .05 .1

0.00
0.05
0.10
```

## sort
``` bash
#
# Ordenamiento con sort
#
seq -f'linea %g' 3 > out.1
cat out.1 out.1 out.1 | sort

linea 1
linea 1
linea 1
linea 2
linea 2
linea 2
linea 3
linea 3
linea 3
```

## uniq
``` bash
#
# Obtención de valores únicos con uniq
#
seq -f'linea %g' 3 > out.1 # genera el primer archivo de datos
seq -f'linea %g' 3 > out.2 # genera el segundo archivo de datos
cat out.1 out.2 out.1 out.2 | uniq

linea 1
linea 2
linea 3
linea 1
linea 2
linea 3
linea 1
linea 2
linea 3
linea 1
linea 2
linea 3
```

``` bash
#
# Obtención de valores únicos con uniq
#
cat out.1 out.2 out.1 out.2 | sort | uniq

linea 1
linea 2
linea 3
```

## wc
``` bash
#
# El comando `wc` permite contar líneas, palabras, caracteres y bytes
# de un archivo. La opción `-l` cuenta líneas,  `-m` caracteres y `-w`
# palabras.
#
wc -l out.1 out.2 # número de líneas

 3 out.1
 3 out.2
 6 total
```

``` bash
#
# Número de caracteres
#
wc -m out.1 out.2

24 out.1
24 out.2
48 total
```

``` bash
#
# Número de palabras
#
wc -w out.1 out.2

 6 out.1
 6 out.2
12 total
```

``` bash
#
# Conteo de lineas, palabras y caracteres
#
wc out.1 out.2

 3  6 24 out.1
 3  6 24 out.2
 6 12 48 total
```

# grep
``` bash
#
# Números entre el 1 y el 20 que conienen el número 1
#
seq 20 | grep 1

1
10
11
12
13
14
15
16
17
18
19
```

``` bash
#
# Lineas que conienen el número 1
#
seq -f'linea %g' 20 > out.1
grep 1 out.1

linea 1
linea 10
linea 11
linea 12
linea 13
linea 14
linea 15
linea 16
linea 17
linea 18
linea 19
```

``` bash
#
# El símbolo `$` indica que la cadena de texto debe aparecer
# al final de la línea. El símbolo `^` indica que la cadena
# de texto debe aparecer al principio de la línea.
#
# Imprime los números del 1 al 100 que finalizan con 1.
#
seq 100 | grep 1$

1
11
21
31
41
51
61
71
81
91
```

``` bash
#
# imprime los números del 1 al 100 que empiezan con 1.
#
seq 100 | grep ^1

1
10
11
12
13
14
15
16
17
18
19
100
```

``` bash
#
# Cantidad de lineas entre el 1 y el 20 que contienen el número 1
#
seq 20 | grep 1 | wc -l

11
```

## tr
``` bash
#
# Borra los caracteres '-'.
#
echo 'h-o-l-a- -m-u-n-d-o' > out.1
tr -d '-'  < out.1

hola mundo
```

``` bash
#
# Cambia el caracter '-' por '='.
#
echo 'h-o-l-a- -m-u-n-d-o' > out.1
tr '-'  '=' < out.1  #  '-' por '='.

h=o=l=a= =m=u=n=d=o
```

``` bash
#
# Cambia las letras minúsculas por mayúsculas.
#
echo 'h-o-l-a- -m-u-n-d-o' > out.1
tr '[:lower:]'  '[:upper:]' < out.1

H-O-L-A- -M-U-N-D-O
```

## cut
``` bash
#
# Se genera un archivo de prueba y se extraen los caracteres
# de la posición 3 a la 5.
#
echo "123456790
abcdefghi
jklmnopqr" > out.1
cut -c3-5 out.1

345
cde
lmn
```

``` bash
#
# Caracteres en las posiciones 2 y 5 a 7 de cada línea de un archivo.
#
cut -c2,5-7 out.1

2567
befg
knop
```

``` bash
#
# cut permite manejar archivos delimitados
#
cat > out.1 <<EOF
FieldA, FieldD, FieldE
   2, X, 2X
   3, Y, 3Y
   4, Z, 4Z
EOF
```

``` bash
#
# archivo delimitado por comas del que se extrae la segunda columna
#
cut -d, -f2 out.1

 FieldD
 X
 Y
 Z
```

``` bash
#
# Extrae las columnas 1 y 3
#
cut -d, -f1,3 out.1

FieldA, FieldE
   2, 2X
   3, 3Y
   4, 4Z
```

``` bash
#
# archivo de prueba
#
echo "Bash is a Unix shell and command language
written by Brian Fox for the
GNU Project as a free software
replacement for the Bourne shell." > out.1
```

``` bash
#
# El delimitador es el espacio en blanco
#
cut -d' ' -f2 out.1

is
by
Project
for
```

## colrm

``` bash
#
# Archivo de prueba
#
echo "123456790
abcdefghi
jklmnopqr" > out.1
#
# Se borran las columnas de la 3 a la 5
#
colrm 3 5 < out.1

126790
abfghi
jkopqr
```

## join
``` bash
cat > out.1 <<EOF
key, F1, F2
  1, 11, 12
  2, 21, 22
  4, 41, 42
EOF
#
# La primera columna es la clave; los valores de los campos
# corresponden a la posición del elemento, es decir, el valor
# `13` corresponde al registro `1` y al campo `3`.
#
cat > out.2 <<EOF
key, F3, F4
  1, 13, 14
  2, 23, 24
  3, 33, 34
EOF
#
# El comando `join` permite unir las líneas de ambos archivos
# usando el campo designado como clave. `join` no agrega el
# último registro de `out.1`, ya que no existe este registro
# en el archivo `out.2`.
#
# Agrega out.2 a out.1 usando como clave el primer campo (por defecto)
#
join -t, out.1 out.2

key, F1, F2, F3, F4
  1, 11, 12, 13, 14
  2, 21, 22, 23, 24
```

``` bash
# INNER
# Adicionalmente, se pueden indicar los campos de salida con la
# opción `-o`. En el siguiente ejemplo, `1.2` representa el
# campo 2 del archivo 1.
#
join -t, -o1.2,2.3 out.1 out.2

 F1, F4
 11, 14
 21, 24
```

``` bash
join -t, -o'0,1.2,2.3' out.1 out.2

key, F1, F4
  1, 11, 14
  2, 21, 24
```

``` bash
# LEFT ANTI
# El siguiente comando imprime los registros de `out.1` cuya
# clave no aparece en `out.2`:
#
# La opción `-v` se usa para que `join` imprima los registros
# que solo aparecen en uno solo de los archivos.
#
join -t, -v 1 out.1 out.2
  
  4, 41, 42
```

``` bash
# RIGHT ANTI
# De forma equivalente, los registros de `out.2`
# que no están en `out.1` se obtienen con:
#
join -t, -v 2 out.1 out.2

  3, 33, 34
```

``` bash
# LO DE AFUERITA (UNION - INNER)
# Los registros que no están en ambos archivos se obtienen con:
#
join -t, -v 1 -v 2 out.1 out.2

  3, 33, 34
  4, 41, 42
```

``` bash
# LEFT
# Para que en la combinación se incluyan los registros sin
# clave en alguno de los archivo se usa la opción `-a`. Por
# ejemplo:
#
join -a 1 -t, out.1 out.2

key, F1, F2, F3, F4
  1, 11, 12, 13, 14
  2, 21, 22, 23, 24
  4, 41, 42
```

``` bash
# RIGHT
join -a 2 -t, out.1 out.2

key, F1, F2, F3, F4
  1, 11, 12, 13, 14
  2, 21, 22, 23, 24
  3, 33, 34
```

``` bash
#
# La opción `-e` se usa para indicar la cadena de texto que se
# agrega a los campos de los registros para los cuales no hay valores.
#
join -a 1 -a 2 -e NA -t,   out.1 out.2

key, F1, F2, F3, F4
  1, 11, 12, 13, 14
  2, 21, 22, 23, 24
  3, 33, 34
  4, 41, 42
```

## paste
``` bash
#
# El comando `paste` permite pegar un archivo con otro,
# uniendo la primera linea de ambos archivos, luego la
# segunda y así sucesivamente.
#
seq -f'linea %g' 5 > out.1; cat out.1

linea 1
linea 2
linea 3
linea 4
linea 5
```

``` bash
seq -f'linea %g' 6 1 10 > out.2; cat out.2

linea 6
linea 7
linea 8
linea 9
linea 10
```

``` bash
paste -d'-' out.1 out.2

linea 1-linea 6
linea 2-linea 7
linea 3-linea 8
linea 4-linea 9
linea 5-linea 10
```