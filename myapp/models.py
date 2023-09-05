from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.functions import Coalesce
from django.template.defaultfilters import wordwrap
import textwrap

# Create your models here.


class Fertilizer(models.Model):
    name = models.CharField(max_length=255)
    Date = models.DateField(null=True,db_index=True)
    Supplier = models.CharField(max_length=255, null=True, db_index=True)
    def __str__(self):
            return f"{self.name}"
    

class Fertilizer_Element(models.Model):
    ELEMENT_CHOICES = (
        ("Nitrate", "Nitrate [NO3N]"),
        ("Phosphorus", "Phosphorus [P]"),
        ("Potassium", "Potassium [K]"),
        ("Calcium", "Cacium [Ca]"),
        ("Magnesium",  "Magnesium [Mg]"),
        ("Sulphur", "Sulphur [S]"),
        ("Ammoniacal N", "Ammoniacal N [NH4N]"),
        ("Iron", "Iron [Fe]"),
        ("Manganese", "Manganese [Mn]"),
        ("Copper", "Copper [Cu]"),
        ("Boron", "Boron [B]"),
        ("Zinc", "Zinc [Zn]"), 
        ("Molybdenum", "Molybdenum [Mo]"),
        )
    Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    Date = models.DateField(null=True,db_index=True)
    Element_1       = models.CharField(max_length=200, choices=ELEMENT_CHOICES,db_index=True,null=True,blank=True)
    Composition_1     = models.FloatField(max_length=200, db_index=True,null=True,blank=True)
    Element_2       = models.CharField(max_length=200, choices=ELEMENT_CHOICES, db_index=True,null=True,blank=True)
    Composition_2     = models.FloatField(max_length=200, db_index=True,null=True,blank=True)
    Element_3       = models.CharField(max_length=200, choices=ELEMENT_CHOICES, db_index=True,null=True,blank=True)
    Composition_3     = models.FloatField(max_length=200, db_index=True,null=True,blank=True)
    Element_4       = models.CharField(max_length=200, choices=ELEMENT_CHOICES, db_index=True,null=True,blank=True)
    Composition_4     = models.FloatField(max_length=200, db_index=True,null=True,blank=True, default=0)
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
    Unit_Of_Measure_Choices = (
    ("Kg", "Kg"),
    ("Ltr", "Ltr"),
    ("Bag", "Bag"),
    ("Pcs", "Pcs"),
    ("Carton", "Carton"),
    ("Pkt", "Pkt"),
    ("Tons", "Tons"),
    ("Bottles", "Bottles"),
    ("Dose", "Dose"),
    )
    Unit_Of_Measure = models.CharField(max_length=255,null=True,db_index=True,
                  choices=Unit_Of_Measure_Choices
                  )
    price_Usd = models.FloatField(blank=True, db_index=True, null=True, default=0)

    def __str__(self):
        return str(self.Fertilizer)


class Fertilizer_Recycle(models.Model):
    Date = models.DateField(null=True,db_index=True)
    ELEMENT_CHOICES = (
        ("Nitrate", "Nitrate [NO3N]"),
        ("Phosphorus", "Phosphorus [P]"),
        ("Potassium", "Potassium [K]"),
        ("Calcium", "Cacium [Ca]"),
        ("Magnesium",  "Magnesium [Mg]"),
        ("Sulphur", "Sulphur [S]"),
        ("Ammoniacal N", "Ammoniacal N [NH4N]"),
        ("Iron", "Iron [Fe]"),
        ("Manganese", "Manganese [Mn]"),
        ("Copper", "Copper [Cu]"),
        ("Boron", "Boron [B]"),
        ("Zinc", "Zinc [Zn]"), 
        ("Molybdenum", "Molybdenum [Mo]"),
        )
    Uv_Element       = models.CharField(max_length=200, choices=ELEMENT_CHOICES,db_index=True,null=True,blank=True)
    Uv_PPM     = models.FloatField(max_length=200, db_index=True,null=True,blank=True)

    @property
    def UvElements(self):
        getUvPercent = Fertilizer_Amount.objects.all()
        UvPercent = 0  # Initialize UvPercent outside the loop
        for elements in getUvPercent:
            percentConstant = 100
            UvPercent = round(self.Uv_PPM * elements.UV_percent / percentConstant, 2)
        return UvPercent


class Fertilizer_Amount(models.Model):
    Date = models.DateField(null=True,db_index=True)
    Fertilizer = models.ForeignKey(Fertilizer,on_delete=models.CASCADE, db_index=True)
    Fertilizer_Amount = models.FloatField(null=True,db_index=True,blank=True, default=0)
    Area_Ha = models.FloatField(null=True,db_index=True,blank=True)
    H2O_m3_Per_Ha = models.FloatField(null=True,db_index=True)
    UV_percent = models.FloatField(null=True,db_index=True)
    Tank_mix_Volume = models.FloatField(null=True,db_index=True)
    Observation = models.TextField(max_length=255, null=True, blank=True)
    Fertigation_line_choices = (
    ("Line 01", "Line 01"),
    ("Line 02", "Line 02"),
    ("Line 03", "Line 03"),
    ("Line 04", "Line 04"),
    ("Line 05", "Line 05"),
    ("Line 06", "Line 06"),
    )
    Fertigation_line = models.CharField(max_length=255,null=True,db_index=True,
                  choices=Fertigation_line_choices
                  )
    

    # Fertilizers_Cost_USD = models.FloatField(null=True,db_index=True)
    MEDIA_CHOICES = (
    ("Hydroponics", "Hydroponics"),
    ("Soil", "Soil"),
    )
    Media = models.CharField(max_length=255,
                  choices=MEDIA_CHOICES
                  )
    
    def get_date_and_fertilizer(self):
        return f"{self.Date.strftime('%d/%m/%Y')}, {self.Fertilizer}"
    
    def __str__(self):
        return str(self.Fertilizer)


    @property
    def total_cost(self):
        getprice = Fertilizer_Price.objects.all()
        for a in getprice:
            if a.Fertilizer == self.Fertilizer:
                # updated_price = a.price_Usd[:-1]
                fertcost = round(a.price_Usd * self.Fertilizer_Amount,2)
                return str(fertcost)
    @property
    def UnitOfMeasure(self):
        getUnitOfMeasure = Fertilizer_Price.objects.all()
        for uom in getUnitOfMeasure:
            if uom.Fertilizer == self.Fertilizer:
                # updated_price = a.price_Usd[:-1]
                return str(uom.Unit_Of_Measure)
    @property
    def Grams_Per_m3(self):
        Grams_Converter = 1000
        Litres_To_M3 = 1000
        Number_of_Tanks = 1
        Grams = self.Fertilizer_Amount * Grams_Converter
        Cubic_Meters = self.Area_Ha * self.H2O_m3_Per_Ha
        Grams_per_m3 = Grams / Cubic_Meters
        Uv_Recycle = self.UV_percent / 100
        Dilution_ratio = round(Number_of_Tanks * (Cubic_Meters * Litres_To_M3) / self.Tank_mix_Volume, 0)
        Injection_ratio = round(self.Tank_mix_Volume / Cubic_Meters, 2)
        getelements = list(Fertilizer_Element.objects.all())

        # Initialize a dictionary to store ppm values for each element
        element_ppm = {}

        for e in getelements:
            element_composition = {
                e.Element_1: e.Composition_1,
                e.Element_2: e.Composition_2,
                e.Element_3: e.Composition_3,
                e.Element_4: e.Composition_4
            }

            for key, value in element_composition.items():
                if key is not None and value is not None and self.Fertilizer == e.Fertilizer:
                    freshFertPpm = round((value or 0) * Grams_per_m3 / 100, 2)

                    # Check if the element already exists in the dictionary
                    if key in element_ppm:
                        element_ppm[key] += freshFertPpm
                    else:
                        element_ppm[key] = freshFertPpm

        # Calculate the total sum of "Nitrate" values
        nitrate_sum = 0.0
        if "Nitrate" in element_ppm:
            nitrate_sum = element_ppm["Nitrate"]
        sum1 = 0
        print("Sum of Nitrate is", nitrate_sum)
        sum1 = nitrate_sum
        print(sum1)
        



        # Print the result dictionary
                    # print(result)
            # if element == "Nitrate":
            #     print("Sum of ppm for", element, "is", ppm_sum)











        all_fertilizer_recycles = Fertilizer_Recycle.objects.all()
        # for items in getelements:
        #     pass

        # Iterate through all Fertilizer_Recycle objects
        # for index, fertilizer_recycle in enumerate(all_fertilizer_recycles):
        #     if index == 0:
        #         uv_element = fertilizer_recycle.Uv_Element
        #         uv_ppm = fertilizer_recycle.Uv_PPM
        #         calculated_Uv = fertilizer_recycle.UvElements
        #         # print("Index:", index, "Element:", uv_element, "calculated:", calculated_Uv)

        # element_sum = {}  # Dictionary to store the sum of values for each element key

        # for e in getelements:
        #     element_composition = {
        #         e.Element_1: e.Composition_1,
                # e.Element_2: e.Composition_2,
                # e.Element_3: e.Composition_3,
                # e.Element_4: e.Composition_4
        #     }
        # counter = 0
        # for key, value in element_composition.items():
        #     if key == "Calcium":  # Check for None values and key "Nitrate"
        #         fertppm1 = round((value or 0) * Grams_per_m3 / 100, 2)
                # print(fertppm1)
                # print(key, value)
                # break  # Exit the loop after processing the "Nitrate" element

            # Print only the last value of fertppm1 after the loop completes
                






                # if key == "Nitrate":
                #     fertppm1 = round((value or 0) * Grams_per_m3 / 100, 2) #+ uv_elements_total.get('Element_1', 0)
                #     print(key, fertppm1)
            #         fertppm2 = round((e.Composition_2 or 0) * Grams_per_m3 / 100, 2) #+ uv_elements_total.get('Element_2', 0)
            #         fertppm3 = round((e.Composition_3 or 0) * Grams_per_m3 / 100, 2) #+ uv_elements_total.get('Element_3', 0)
            #         fertppm4 = round((e.Composition_4 or 0) * Grams_per_m3 / 100, 2) #+ uv_elements_total.get('Element_4', 0)
            #         if fertppm1 == 0:
            #             fertppm1 = ""
            #         if fertppm2 == 0:
            #             fertppm2 = ""
            #         if fertppm3 == 0:
            #             fertppm3 = ""
            #         if fertppm4 == 0:
            #             fertppm4 = ""
            #         return {
            #             'element_1': e.Element_1,
            #             'element_2': e.Element_2,
            #             'element_3': e.Element_3,
            #             'element_4': e.Element_4,
            #             'grams_per_m3': Grams_per_m3,
            #             'fertppm1': fertppm1,
            #             'fertppm2': fertppm2,
            #             'fertppm3': fertppm3,
            #             'fertppm4': fertppm4,
            #             'Injection_ratio': Injection_ratio,
            #         }

            # return {
            #     'element_1': 'N/A',
            #     'element_2': 'N/A',
            #     'element_3': 'N/A',
            #     'element_4': 'N/A',
            #     'grams_per_m3': Grams_per_m3,
            #     'fertppm1': 'N/A',
            #     'fertppm2': 'N/A',
            #     'fertppm3': 'N/A',
            #     'fertppm4': 'N/A',
            #     'Injection_ratio': 'N/A',
            # }
        



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

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, null=True, db_index=True, blank=True)
    about_Image = models.TextField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Wrap the about_Image text before saving
        if self.about_Image:
            self.about_Image = textwrap.fill(self.about_Image, width=40)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"