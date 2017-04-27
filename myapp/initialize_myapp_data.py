import os
import random

import django
import sys

from django.db.models import Max
from django.utils.dateparse import parse_datetime, parse_date
from math import floor

print('Python %s on %s' % (sys.version, sys.platform))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Leaderboards.settings')
django.setup()
print('Django version %s' % django.get_version())

from myapp.models import Animal


Animal.objects.all().delete()

a = Animal(name="Bugs Bunny", sound="Ha ha ha")
a.save()

print(Animal.objects.count())