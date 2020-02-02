from django.db import models
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Banners(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Inmuebles(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    def __str__(self):
        return self.name
