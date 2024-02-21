from django.contrib import admin
from .models import Account, Audit, UserProfile


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

class AccountModelAdmin(admin.ModelAdmin):
    list_display = ('account_no', 'name', 'balance')
    search_fields = ('name', 'account_no')

class AuditModelAdmin(admin.ModelAdmin):
    list_display = ('reference', 'old_balance', 'new_balance', 'action', 'state')
    search_fields = ('reference', 'account_ids')

admin.site.register(UserProfile, UserProfileModelAdmin)
admin.site.register(Account, AccountModelAdmin)
admin.site.register(Audit, AuditModelAdmin)