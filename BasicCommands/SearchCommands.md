# Search commands

## locate

``` bash
# apt update
# apt install mlocate
```

``` bash
#
# Busca en todo el sistema cualquier ocurrencia de la palabra indicada
#
locate apache

/snap/dbeaver-ce/379/usr/share/dbeaver-ce/plugins/org.apache.httpcomponents.core5.httpcore5_5.3.2.v20250110-0800.jar
/snap/dbeaver-ce/379/usr/share/dbeaver-ce/plugins/org.apache.xmlgraphics_2.10.0.v20241009-1200.jar
/snap/snapd/23771/usr/lib/snapd/apparmor.d/abstractions/apache2-common
/snap/snapd/24505/usr/lib/snapd/apparmor.d/abstractions/apache2-common
```

## whereis

``` bash
#
# Busca archivos binarios incluyendo la ubicación, el fuente y la ayuda
#
whereis python3

python3: /usr/bin/python3 /usr/lib/python3 /etc/python3 /usr/share/python3 /usr/share/man/man1/python3.1.gz
```

## which
``` bash
#
# Busca archivos binarios en la variable PATH
#
which python3

/usr/bin/python3
```

## find
``` bash
# Busca indicando el directorio para iniciar la búsqueda, el tipo de archivo y
# el nombre del archivo
find / -type f -name apache2

# / indicates root directory
# -name searchs for the exact same name, case sensitive
# types: f (regular file, /home/user/file.txt) | d (directory, /etc/apache2) | l (symbolic link, /usr/bin/python -> /usr/bin/python3.10) | c (character device, /dev/tty0) | b (block device, /dev/sda) | p (named pipe, /tmp/my_fifo) | s (socket, /run/docker.sock)
```

## grep
``` bash
#
# Procesos ejecutandose en el sistema
#
ps aux

ezapataq   23176  0.5  0.3 851528 54992 ?        Ssl  18:03   0:02 /usr/libexec/gnome-terminal-server
ezapataq   23187  0.0  0.0  19932  5456 pts/0    Ss   18:03   0:00 bash
ezapataq   23637  0.0  0.0 166380  3308 ?        SLsl 18:04   0:00 /usr/bin/gpg-agent --supervised
root       23707  0.0  0.0      0     0 ?        I    18:04   0:00 [kworker/u32:0-flush-259:0]
root       23865  0.0  0.0      0     0 ?        I    18:05   0:00 [kworker/7:0]
ezapataq   27265  0.0  0.0  17812  2224 pts/0    S+   18:15   0:00
```

``` bash
#
# Procesos que contengan apache2
#
ps aux | grep apache2

ezapataq   27265  0.0  0.0  17812  2224 pts/0    S+   18:15   0:00 grep --color=auto apache2
```

