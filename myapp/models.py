from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Fertilizer(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
            return f"{self.name}"

class Fertilizer_Element(models.Model):
    container = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    element1       = models.CharField(max_length=200, null=True, db_index=True, blank=True)
    composition1     = models.FloatField(null=True, db_index=True, blank=True)
    element2       = models.CharField(max_length=200, null=True, db_index=True, blank=True)
    composition2     = models.FloatField(null=True, db_index=True, blank=True)
    element3       = models.CharField(max_length=200, null=True, db_index=True,default=None, blank=True)
    composition3     = models.FloatField(null=True, db_index=True,default=None, blank=True)
    element4       = models.CharField(max_length=200, null=True, db_index=True, default=None, blank=True)
    composition4     = models.FloatField(null=True, db_index=True, default=None, blank=True)
    element5       = models.CharField(max_length=200, null=True, db_index=True, default=None, blank=True)
    composition5     = models.FloatField(null=True, db_index=True, default=None, blank=True)
    def __str__(self):
        return str(self.container)
        
class Fertilizer_Detail(models.Model):
    container = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    registeredDate = models.DateField(null=True, db_index=True, blank=True)
    price_USD= models.FloatField(null=True, db_index=True, blank=True)
    supplier = models.CharField(max_length=200, null=True, db_index=True, blank=True)
    fertilizer_info = models.URLField(max_length=200, db_index=True, blank=True)

    def __str__(self):
        return str(self.container)
    
class Fertilizer_Amount(models.Model):
    Date = models.DateField(null=True,db_index=True)
    Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    amount = models.FloatField(null=True,db_index=True)
    Water_Volume_m3 = models.FloatField(null=True,db_index=True)
    UV_percent = models.FloatField(null=True,db_index=True)
    Injection_Ratio = models.FloatField(null=True,db_index=True)
    
    def __str__(self):
        return str(self.Fertilizer)