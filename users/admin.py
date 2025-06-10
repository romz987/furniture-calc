from django.contrib import admin
from users.models import User

# model registration in admin panel
admin.site.register(User)
