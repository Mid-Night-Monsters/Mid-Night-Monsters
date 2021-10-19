from django.contrib import admin
from .models import Consumer,Order
# Register your models here.
admin.site.register(Consumer)
admin.site.register(Order)
admin.site.site_header = 'Consumer Admin'
admin.site.site_title = 'Consumer Admin'