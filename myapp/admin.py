from django.contrib import admin
from .models import Fertilizer, Fertilizer_Detail, Fertilizer_Element,Fertilizer_Amount,Fertilizer_Cost



admin.site.register(Fertilizer)
admin.site.register(Fertilizer_Element)
admin.site.register(Fertilizer_Detail)
admin.site.register(Fertilizer_Amount)
admin.site.register(Fertilizer_Cost)


admin.site.site_header = "your Admin name "
admin.site.site_title = "Your Admin Portal"
admin.site.index_title = "Welcome to YOur Researcher Portal"



