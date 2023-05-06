from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CarType)
admin.site.register(CarVarient)
admin.site.register(Brand)
admin.site.register(CarEngineAndTransmission)
admin.site.register(Fuel)
admin.site.register(Exterior)
admin.site.register(Car)

