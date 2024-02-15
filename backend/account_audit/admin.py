from django.contrib import admin
from .models import User, Account, Audit

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Audit)