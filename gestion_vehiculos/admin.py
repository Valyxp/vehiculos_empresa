from django.contrib import admin
from .models import Chofer, Vehiculo, RegistroContabilidad


class VehiculoAdmin(admin.ModelAdmin):
    list_display = (
        "patente",
        "marca",
        "modelo",
        "year",
        "activo",
    )
    search_fields = ("patente", "marca", "modelo")


class RegistroContabilidadAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_compra", "valor", "vehiculo")
    search_fields = ("vehiculo__patente", "fecha_compra")


admin.site.register(Chofer)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(RegistroContabilidad, RegistroContabilidadAdmin)
