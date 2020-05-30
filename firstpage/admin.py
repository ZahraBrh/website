from django.contrib import admin

from .models import Auteur
from .models import Articl
from .models import Ecrit

admin.site.register(Articl)
admin.site.register(Auteur)
admin.site.register(Ecrit)

