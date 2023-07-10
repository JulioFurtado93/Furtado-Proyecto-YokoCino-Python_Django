from django.contrib import admin
from .models import *
from Accounts.models import *

# Register your models here.

admin.site.register(Blog)

admin.site.register(Avatar)