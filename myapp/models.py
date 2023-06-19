from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.functions import Coalesce

# Create your models here.


class Fertilizer(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
            return f"{self.name}"

class Fertilizer_Element(models.Model):
    Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
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
        return str(self.Fertilizer)
        
class Fertilizer_Detail(models.Model):
    Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    registeredDate = models.DateField(null=True, db_index=True, blank=True)
    price_USD= models.FloatField(null=True, db_index=True, blank=True)
    supplier = models.CharField(max_length=200, null=True, db_index=True, blank=True)
    fertilizer_info = models.URLField(max_length=200, db_index=True, blank=True)

    def __str__(self):
        return str(self.Fertilizer)


class Fertilizer_Price(models.Model):
    Date = models.DateField(null=True,db_index=True)
    Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    price_Usd = models.FloatField(blank=True, db_index=True, null=True, default=0)

    def __str__(self):
        return str(self.Fertilizer)

class Fertilizer_Amount(models.Model):
    Date = models.DateField(null=True,db_index=True)
    Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    Amount = models.FloatField(null=True,db_index=True,blank=True, default=0)
    Area_Ha = models.FloatField(null=True,db_index=True,blank=True)
    H2O_m3_Per_Ha = models.FloatField(null=True,db_index=True)
    UV_percent = models.FloatField(null=True,db_index=True)
    Injection_Ratio = models.FloatField(null=True,db_index=True)
    Grams_Per_m3 = models.FloatField(null=True,db_index=True)

    # Fertilizers_Cost_USD = models.FloatField(null=True,db_index=True)
    MEDIA_CHOICES = (
    ("HYDROPONICS", "HYDROPONICS"),
    ("SOIL", "SOIL"),
    )
    Media = models.CharField(max_length=255,
                  choices=MEDIA_CHOICES
                  )
    
    def __str__(self):
        return str(self.Fertilizer)

    @property
    def total_cost(self):
        getprice = Fertilizer_Price.objects.all()
        for a in getprice:
            if a.Fertilizer == self.Fertilizer:
                # updated_price = a.price_Usd[:-1]
                fertcost = a.price_Usd * self.Amount
                return str(fertcost)
            

    @property
    def Grams_Per_m3(self):
        Grams_Converter = 1000
        Grams = self.Amount * Grams_Converter
        Cubic_Meters = self.Area_Ha * self.H2O_m3_Per_Ha
        Grams_per_m3 = Grams / Cubic_Meters
        Uv_Recycle = self.UV_percent / 100
        getelements = Fertilizer_Element.objects.all()
        for a in getelements:
            if a.Fertilizer == self.Fertilizer:
                # updated_price = a.price_Usd[:-1]
                fertppm = a.composition1 * Grams_per_m3 / 100
                print(fertppm)
                return str(fertppm)
      

#Testing Models
class Fertilizer_Cost(models.Model):
    ...   
    # Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    # getamount = Fertilizer_Amount.objects.all()
    # getprice = Fertilizer_Price.objects.all()
    # for a in getamount:
    #     for p in getprice:
    #         if p.price_Usd == None:
    #             p.price_Usd = 0
    #             fertcost = a.amount * p.price_Usd
    
    # @property
    # def total_cost(self):
    #     if self.fertcost == None:
    #         self.fertcost = 0
    #         return str(0)
    #     return str(self.fertcost)