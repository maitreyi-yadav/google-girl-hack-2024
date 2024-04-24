import os
import django
import random

# this file was used to populate the database with doctor entries, taken from official hospital websites
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DiseasePredictor.settings')
django.setup()

import pandas as pd
from django.contrib.auth.models import User
from api.models.hospital import *
time = [
    "11:00 AM to 1:00 PM",
    "1:00 PM to 3:00 PM",
    "3:00 PM to 5:00 PM",
    "5:00 PM to 7:00 PM",
]

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Monday-Friday",
    "Saturday",
    "Monday, Wednesday, Friday"
]
csv_file_path = './datasets/max_shalimarBagh.csv'
df = pd.read_csv(csv_file_path)

hosp = Hospital.objects.create(name="Max Hospital",address= "Shalimar Bagh, Delhi-110088")
hosp.save()
for index, row in df.iterrows():
    speciality, created = Specialty.objects.get_or_create(
        name_of_specialty=row['Specialty'],
    )
    day_av = days[random.randint(0,7)]
    time_av = time[random.randint(0,3)]
    # Create the Product instance
    doctor = Doctor(
        name=row['Name'],
        experience=row['Experience'],
        hospital=hosp,
        specialty=speciality,
        time_available = time_av,
        days_available = day_av
    )
    #to save the current product
    doctor.save()

csv_file_path = './datasets/ActionBalaji_PaschimVihar.csv'
df = pd.read_csv(csv_file_path)

hosp = Hospital.objects.create(name="Action Balaji Cancer Institute",address= "Paschim Vihar, Delhi-110087")
hosp.save()
for index, row in df.iterrows():
    speciality, created = Specialty.objects.get_or_create(
        name_of_specialty=row['Specialty'],
    )
    day_av = days[random.randint(0,7)]
    time_av = time[random.randint(0,3)]
    # Create the Product instance
    doctor = Doctor(
        name=row['Name'],
        experience=f'{row["Experience"]}+ years',
        hospital=hosp,
        specialty=speciality,
        time_available = time_av,
        days_available = day_av
    )
    #to save the current product
    doctor.save()

print("CSV data has been loaded into the Django database.")