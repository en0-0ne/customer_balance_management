from django.contrib import admin
from .models import User, Account, Audit

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone', 'access_type')
    search_fields = ('name', 'email')
    list_per_page = 20


class AccountModelAdmin(admin.ModelAdmin):
    list_display = ('account_no', 'name', 'customer_id', 'balance')
    search_fields = ('name', 'account_no', 'customer_id__name')
    list_per_page = 20

class AuditModelAdmin(admin.ModelAdmin):
    list_display = ('reference', 'old_balance', 'new_balance', 'action', 'state')
    search_fields = ('reference', 'account_ids')
    list_per_page = 20

admin.site.register(User, UserModelAdmin)
admin.site.register(Account, AccountModelAdmin)
admin.site.register(Audit, AuditModelAdmin)