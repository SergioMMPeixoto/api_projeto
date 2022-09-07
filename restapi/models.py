from django.db import models

#Ementa terá nome, dia no qual será confecionada e os alimentos que a constituem em lista
class Meal(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    ingredients = models.CharField(max_length=250)

#Os alimentos terão nome, data de validade e quantidade no inventário.
#Os alimentos podem ter o mesmo nome mas validades diferentes, pois podem chegar em espaços de tempo diferentes
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    expire_date = models.DateField()
    stock = models.IntegerField()

class DayData(models.Model):
    date = models.DateField()
    foodConsumed = models.FloatField()
    foodWasted = models.FloatField()
    clients = models.IntegerField()
    absences = models.IntegerField()

class Orders(models.Model):
    orderID = models.CharField(max_length=50)
    suplier = models.CharField(max_length=100)
    ammount = models.FloatField()
    item = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    statusBg = models.CharField(max_length=20, default="#FEC90F") 
    image = models.CharField(max_length=50)
