from django.contrib import admin
from .models import Food,Number

admin.site.register(Food)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'number']
    search_fields = ['username']
    list_per_page = 4

admin.site.register(Number, PeopleAdmin)