from django.contrib import admin
from .models import Owner, Book

# Register your models here.
admin.site.register([Owner, Book])
