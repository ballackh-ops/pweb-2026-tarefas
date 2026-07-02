from django.db import models

class Dever(models.Model):
    nome = models.CharField(max_length=100),
    status = models.DateField(auto_now=True),
    prazo = models.DateField(),