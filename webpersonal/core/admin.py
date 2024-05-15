from django.contrib import admin
from core.models import Usuario
from core.models import Editorial
from core.models import Autor
from core.models import Genero
from core.models import Libro
from core.models import Prestamo
from core.models import Reserva

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Reserva)