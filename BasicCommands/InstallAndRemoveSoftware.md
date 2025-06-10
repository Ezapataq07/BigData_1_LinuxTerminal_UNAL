# Install and Remove Software

``` bash
#
# Búsqueda de un paquete
#
apt-cache search python3 | head

alembic - lightweight database migration tool for SQLAlchemy
brltty - Access software for a blind person using a braille display
debian-goodies - Small toolbox-style utilities for Debian systems
devscripts - scripts to make the life of a Debian Package maintainer easier
libcrack2-dev - pro-active password checker library - development files
libpython3-all-dbg - package depending on all supported Python 3 debugging packages
libpython3-all-dev - package depending on all supported Python 3 development packages
libpython3-dbg - debug build of the Python 3 Interpreter (version 3.12)
libpython3-dev - header files and a static library for Python (default)
libpython3-stdlib - interactive high-level object-oriented language (default python3 version)
```

``` bash
#
# Actualización de paquetes
#
apt-get update
```

``` bash
#
# Instalación
#
apt-get install -y vim
```

``` bash
#
# Remoción de software (Paso 1)
#
apt-get remove -y vim
```

``` bash
#
# Remoción de software (Paso 2)
#
apt-get purge -y vim
```

``` bash
#
# Remoción de software y dependencias
#
apt autoremove -y vim
```