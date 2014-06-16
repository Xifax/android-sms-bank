from django.contrib import admin
from models import (
    Device,
    Profile
)

admin.site.register([Device, Profile])
