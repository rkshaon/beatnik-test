from django.db import models

class Team(models.Model):
    full_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    image = models.ImageField(upload_to='static/photo')

class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/portfolio')

class Blog(models.Model):
    topic = models.CharField(max_length=15)
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=1000)