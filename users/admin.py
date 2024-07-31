from django.contrib import admin
from users.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'pic', 'bio')
    search_fields = ('user__username', 'name')

# Register your models here.
admin.site.register(CustomUser)
