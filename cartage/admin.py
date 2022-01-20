from django.contrib import admin

from .models import User, Trip, Address

admin.site.register(User)
admin.site.register(Trip)
admin.site.register(Address)
