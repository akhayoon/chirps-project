from django.db import models

class Chirp(models.Model):
    text = models.CharField(max_length=140,null=True)