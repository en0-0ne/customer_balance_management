from django.contrib import admin
from .models import User, Account, Audit

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone', 'access_type')
    search_fields = ('name', 'email')
    list_per_page = 20

admin.site.register(User, UserModelAdmin)
admin.site.register(Account)
admin.site.register(Audit)