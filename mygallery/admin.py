from django.contrib import admin
from .models import Location, Category, Image, AboutMe

# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(AboutMe)
