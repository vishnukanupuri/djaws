from django.contrib import admin
from . import models
# Register your models here.
class guestAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Guests, guestAdmin)