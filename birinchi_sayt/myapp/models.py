from django.db import models

# Create your models here.
class Kitob(models.Model):
    nomi = models.CharField(max_length=150)
    betlari_soni = models.IntegerField()
    yili = models.DateField()
    muallifi = models.CharField(max_length=150)
    janr = models.CharField(max_length=150)
    haqida = models.TextField()
    rasmi = models.ImageField(upload_to='kitob_rasmlari/')

    def __str__(self):
        return f"{self.nomi} - kitobi"
