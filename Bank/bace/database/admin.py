from django.contrib import admin
from .models import Number

class ModalAdmin(admin.ModelAdmin):
    list_display = ('username', 'number')
    search_fields = ['name']
    list_per_page = 4


admin.site.register(Number, ModalAdmin)