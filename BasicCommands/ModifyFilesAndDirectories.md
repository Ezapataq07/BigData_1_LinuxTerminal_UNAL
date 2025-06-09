# Modificación de archivos y directorios

## Creación de archivos con cat
``` bash
#
# Creación de archivos con cat
#
cat > hola.txt
hola mundo cruel
```

``` bash
#
# Archivos en la carpeta actual que terminan en '.txt'
#
ls *.txt

hola.txt  listado.txt
```

``` bash
#
# Impresión del contenido del archivo
#
cat hola.txt

hola mundo cruel
```

``` bash
#
# Adicion de contenido con cat
#
cat >> hola.txt
Esta es la segunda linea del archivo

#hola.txt
hola mundo cruel
Esta es la segunda linea del archivo
```

``` bash
cat > hola.txt <<EOF
hola
mundo
cruel
EOF

#hola.txt
hola
mundo
cruel
```

``` bash
#
# Archivo sobreescrito
#
cat > hola.txt
Esta es la primera linea del archivo

#hola.txt
Esta es la primera linea del archivo
```

## touch
``` bash
#
# Creación del archivo con touch (vacio)
#
touch newfile
```

## mkdir
``` bash
#
# Creación de un directorio
#
mkdir newdirectory

-rw-rw-r-- 1 ezapataq ezapataq  9574885 Jun  9 17:31  2015.csv
-rw-rw-r-- 1 ezapataq ezapataq     4100 Jun  9 18:00  BasicCommands.md
-rw-rw-r-- 1 ezapataq ezapataq 70162382 Jun  9 18:26  datos.csv
-rw-rw-r-- 1 ezapataq ezapataq     1834 Jun  9 18:26  generate_large_csv.py
-rw-rw-r-- 1 ezapataq ezapataq       37 Jun  9 18:39  hola.txt
-rw-rw-r-- 1 ezapataq ezapataq     1042 Jun  9 17:46  listado.txt
-rw-rw-r-- 1 ezapataq ezapataq      826 Jun  9 18:41  ModifyFilesAndDirectories.md
drwxrwxr-x 2 ezapataq ezapataq     4096 Jun  9 18:44  newdirectory
-rw-rw-r-- 1 ezapataq ezapataq        0 Jun  9 18:42  newfile ###
-rw-rw-r-- 1 ezapataq ezapataq     2132 Jun  9 18:17  SearchCommands.md
```

## cp
``` bash
#
# Copia el archivo
#
cp newfile newdirectory/newfile_copy
cd newdirectory/
ls

newfile_copy
```

## mv
``` bash
#
# Se usa para mover o renombrar un archivo
#
mv newfile_copy newfile2
ls

newfile2
```

## rm
``` bash
#
# Borra archivos
#
rm newfile2
ls

(empty)
```

## rmdir
``` bash
rmdir newdirectory
ls -l

-rw-rw-r-- 1 ezapataq ezapataq  9574885 Jun  9 17:31 2015.csv
-rw-rw-r-- 1 ezapataq ezapataq     4100 Jun  9 18:00 BasicCommands.md
-rw-rw-r-- 1 ezapataq ezapataq 70162382 Jun  9 18:26 datos.csv
-rw-rw-r-- 1 ezapataq ezapataq     1834 Jun  9 18:26 generate_large_csv.py
-rw-rw-r-- 1 ezapataq ezapataq       37 Jun  9 18:39 hola.txt
-rw-rw-r-- 1 ezapataq ezapataq     1042 Jun  9 17:46 listado.txt
-rw-rw-r-- 1 ezapataq ezapataq     1813 Jun  9 18:52 ModifyFilesAndDirectories.md
-rw-rw-r-- 1 ezapataq ezapataq        0 Jun  9 18:42 newfile
-rw-rw-r-- 1 ezapataq ezapataq     2132 Jun  9 18:17 SearchCommands.md
```

``` bash
#
# Cuando el directorio tiene contenido se debe borrar con rm -r
#
rm -r newdirectory
ls
```