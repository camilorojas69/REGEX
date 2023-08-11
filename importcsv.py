import csv
import random
from faker import Faker

fake = Faker()

# Generar 10000 registros aleatorios
records = []
for _ in range(10000):
    record = [
        fake.country(),
        fake.random_int(min=2000, max=2023), 
        fake.random_int(min=1, max=12),
        fake.random_int(min=1, max=28),
        fake.name().upper(),'#',
        fake.email(),
        fake.random_int(min=0, max=5),
        fake.phone_number(),
        fake.company()
    ]
    records.append(record)

# Escribir los registros en un archivo CSV
with open('registros.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for record in records:
        writer.writerow(record)

print("Archivo 'registros.csv' generado exitosamente.")
