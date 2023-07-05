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
    Element_1       = models.CharField(max_length=200, db_index=True,null=True,blank=True)
    Composition_1     = models.CharField(max_length=200, db_index=True,null=True,blank=True)
    Element_2       = models.CharField(max_length=200, db_index=True,null=True,blank=True)
    Composition_2     = models.FloatField(max_length=200, db_index=True,null=True,blank=True)
    Element_3       = models.CharField(max_length=200, db_index=True,null=True,blank=True)
    Composition_3     = models.FloatField(max_length=200, db_index=True,null=True,blank=True)
    Element_4       = models.CharField(max_length=200, db_index=True,null=True,blank=True)
    Composition_4     = models.FloatField(max_length=200, db_index=True,null=True,blank=True)
    def __str__(self):
        return str(self.Fertilizer)
    
        
class Fertilizer_Detail(models.Model):
    Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    registeredDate = models.DateField(null=True, db_index=True, blank=True)
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
    Tank_mix_Volume = models.FloatField(null=True,db_index=True)
    

    # Fertilizers_Cost_USD = models.FloatField(null=True,db_index=True)
    MEDIA_CHOICES = (
    ("HYDROPONICS", "HYDROPONICS"),
    ("SOIL", "SOIL"),
    )
    Media = models.CharField(max_length=255,
                  choices=MEDIA_CHOICES
                  )
    
    def get_date_and_fertilizer(self):
        return f"{self.Date.strftime('%d/%m/%Y')}, {self.Fertilizer}"


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
        Litres_To_M3 = 1000
        Number_of_Tanks = 1
        Grams = self.Amount * Grams_Converter
        Cubic_Meters = self.Area_Ha * self.H2O_m3_Per_Ha
        Grams_per_m3 = Grams / Cubic_Meters
        Uv_Recycle = self.UV_percent / 100
        Injection_Ratio = round(Number_of_Tanks*(Cubic_Meters*Litres_To_M3)/self.Tank_mix_Volume,0)
        getelements = Fertilizer_Element.objects.all()
        for e in getelements:
            print(e.element1)
            if e.Fertilizer == self.Fertilizer:
                # updated_price = a.price_Usd[:-1]
                fertppm = e.composition1 * Grams_per_m3 / 100
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