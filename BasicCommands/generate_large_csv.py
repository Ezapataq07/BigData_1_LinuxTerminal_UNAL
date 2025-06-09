import csv
import random
import string
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    """Genera una fecha aleatoria entre start_date y end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def random_placa():
    """Genera una placa aleatoria en formato AAA999."""
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=3))
    return letras + numeros

def generar_registros_csv(filename, n_registros):
    ciudades = [
        'Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena',
        'Cúcuta', 'Bucaramanga', 'Pereira', 'Santa Marta', 'Manizales',
        'Ibagué', 'Pasto', 'Montería', 'Neiva', 'Palmira',
        'Valledupar', 'Armenia', 'Sincelejo', 'Popayán', 'Villavicencio'
    ]

    fecha_inicio = datetime(2010, 1, 1)
    fecha_fin    = datetime(2020, 12, 31)  # o datetime.today()

    seen = set()  # para asegurar unicidad de (placa, ciudad)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escribir cabecera
        writer.writerow(['fecha', 'placa', 'ciudad', 'valor'])

        while len(seen) < n_registros:
            placa = random_placa()
            ciudad = random.choice(ciudades)
            key = (placa, ciudad)
            if key in seen:
                continue
            seen.add(key)

            fecha = random_date(fecha_inicio, fecha_fin).strftime('%Y-%m-%d')
            valor = random.randint(1, 500_000)

            writer.writerow([fecha, placa, ciudad, valor])

if __name__ == '__main__':
    generar_registros_csv('datos.csv', 2_000_000)
    print("¡Archivo 'datos.csv' generado con 3 000 000 registros!")
