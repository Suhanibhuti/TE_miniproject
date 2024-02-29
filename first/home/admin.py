from django.contrib import admin
from home.models import pdM
from home.models import attM
from home.models import adM
from home.models import cocuM
from home.models import excoM
from home.models import plcM

# Register your models here.
admin.site.register(pdM)
admin.site.register(attM)
admin.site.register(adM)
admin.site.register(cocuM)
admin.site.register(excoM)
admin.site.register(plcM)
