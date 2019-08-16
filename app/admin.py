from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(user_role)
admin.site.register(azure_key)
admin.site.register(application)