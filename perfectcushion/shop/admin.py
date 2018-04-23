from django.contrib import admin
from shop import models
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display=('name', 'slug', 'price')


admin.site.register(models.Product)
admin.site.register(models.Category)
