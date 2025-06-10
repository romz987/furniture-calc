from django.contrib import admin
from users.models import User

# model registration in admin panel

# method one: common
# admin.site.register(User)

# method two: detailed 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'pk')
    list_filter = ('last_name', )
