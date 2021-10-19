from django.contrib import admin
from .models import Consumer,Order
# Register your models here.
admin.site.register(Consumer)
admin.site.register(Order)
admin.site.site_header = 'Smart Restaurant'
admin.site.site_title = 'Smart Restaurant'
admin.site.index_title = 'All models'
