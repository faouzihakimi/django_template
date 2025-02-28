import os
import sys
import django

# Add the parent directory of the simple_app directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_app.settings')

# Setup Django
django.setup()

# Now you can access the settings module
from django.core.management import call_command
from home.models import CO2

# Create the database tables
call_command('makemigrations')
call_command('migrate')

# Import the data from the CSV file
import csv
from datetime import date
from itertools import islice



with open('../origin_data/co2_mm_mlo.csv', 'r') as file:
        reader = csv.DictReader(islice(file, 51, None)) #skip the first 51 lines that are not data
        for row in reader:
            dt = date(year=int(row['year']), month=int(row['month']), day=1)
            CO2.objects.get_or_create(date=dt, average = row['average'])