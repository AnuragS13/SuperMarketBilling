from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin

from .models import Item
from .resources import ItemResource


@admin.register(Item)
class UserAdmin(ImportExportModelAdmin, SearchAutoCompleteAdmin):
    resource_class = ItemResource
    search_fields = ['name', 'category', 'subcategory']
