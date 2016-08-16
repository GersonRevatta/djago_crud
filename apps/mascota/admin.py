from django.contrib import admin

from apps.mascota.models import Vacuna
from apps.mascota.models import Mascota


# Register your models here.

admin.site.register(Vacuna)
admin.site.register(Mascota)
