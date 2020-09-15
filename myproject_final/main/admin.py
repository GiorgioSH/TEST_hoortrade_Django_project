from django.contrib import admin

# Register your models here.

from .models import Acteur
from .models import Realisateur
from .models import Film

admin.site.register(Acteur)
admin.site.register(Realisateur)
admin.site.register(Film)