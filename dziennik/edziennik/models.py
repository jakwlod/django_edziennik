from django.db import models
from django.contrib.auth.models import User


class Osoba(models.Model):
    imie=models.CharField(max_length=15)
    nazwisko=models.CharField(max_length=30)
    pesel=models.CharField(max_length=9)
    user= models.ForeignKey(User, on_delete=models.CASCADE )
    class Meta:
        permissions=(("nauczyciel","nauczyciel v 2.0"),)




class Klasa(models.Model):
    klasa= models.CharField(max_length=3)

class Listaklasy(models.Model):
    id_k=models.ForeignKey(Klasa, on_delete=models.DO_NOTHING)
    id_u=models.ForeignKey(Osoba, on_delete=models.DO_NOTHING)

class Plan(models.Model) :
    id_k= models.ForeignKey(Klasa, on_delete=models.CASCADE)
    id_n= models.ForeignKey(Osoba, on_delete=models.CASCADE)
    przedmiot= models.CharField(max_length=30)


class Ocena(models.Model):
    id_u=models.ForeignKey(Osoba, on_delete=models.CASCADE)
    ocena = models.IntegerField()
    waga=models.IntegerField()
    id_n=models.ForeignKey(Plan, on_delete=models.DO_NOTHING)
    przedmiot= models.CharField(max_length=30)
    opis=models.CharField(max_length=100)
