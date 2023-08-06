from django.contrib import admin
from .models import Fertilizer, Fertilizer_Detail, Fertilizer_Element,Fertilizer_Amount,Fertilizer_Cost, UploadedImage



admin.site.register(Fertilizer)
admin.site.register(Fertilizer_Element)
admin.site.register(Fertilizer_Detail)
admin.site.register(Fertilizer_Amount)
admin.site.register(Fertilizer_Cost)
admin.site.register(UploadedImage)


admin.site.site_header = "FERTPPM"
admin.site.site_title = "FERTPPM ADMINSTARTION"
admin.site.index_title = "Welcome To Your Crop Nutrition Site"





