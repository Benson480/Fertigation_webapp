from django.contrib import admin
from .models import Fertilizer, Fertilizer_Detail, Fertilizer_Element,Fertilizer_Amount



admin.site.register(Fertilizer)
admin.site.register(Fertilizer_Element)
admin.site.register(Fertilizer_Detail)
admin.site.register(Fertilizer_Amount)


