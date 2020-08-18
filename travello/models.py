from django.db import models

# Create your models here.

class Bureau(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    year = models.TextField()
    link = models.TextField(default = '')

class DBTable(models.Model):
    crime_name = models.TextField()
    date_reported = models.TextField()
    Time_reported = models.TextField()
    name_reporter = models.TextField()
    phone_reporter = models.TextField()
    email_reporter = models.TextField()
    address_reporter = models.TextField()
    date_crime = models.TextField()
    time_crime = models.TextField()
    place_offence = models.TextField()
    description = models.TextField()


