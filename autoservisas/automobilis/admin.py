from django.contrib import admin

from automobilis.models import Automobilis, Automobilio_modelis
from uzsakymas.models import Uzsakymas, Paslauga, Uzsakymo_eilute


# Register your models here.

class Automobilis_Admin(admin.ModelAdmin):
    list_display = [
        'Valstybinis_NR',
        'VIN_kodas',
        'klientas',
        'Automobilio_modelis_id'
    ]
    fieldsets = [
        ("Automobilio informacija", {
            'fields': (
                'Automobilio_modelis_id',
                'VIN_kodas',
                'Valstybinis_NR',
                'klientas'
            ),
        }),

    ]
    list_filter = ('klientas', 'Automobilio_modelis_id')
    search_fields = ('Valstybinis_NR', 'VIN_kodas')
class Automobilio_modelisAdmin(admin.ModelAdmin):
    list_display = ['Marke',
                    'Modelis']
    fieldsets = [
        ("Markės informacija", {
            'fields': (
                'Marke',
                'Modelis'
            ),
        }),

    ]
    list_filter = ('Marke',
                    'Modelis')
    search_fields = ('Marke',
                    'Modelis')


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ['data',
                    'automobilis_id',
                    'suma'
                    ]


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ['pavadinimas',
                    'kaina']


class Uzsakymo_eiluteAdmin(admin.ModelAdmin):
    list_display = ['Paslauga',
                    'Uzsakymas',
                    'Kiekis',
                    'Kaina']


admin.site.register(Automobilis, Automobilis_Admin)
admin.site.register(Automobilio_modelis, Automobilio_modelisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymo_eilute, Uzsakymo_eiluteAdmin)
