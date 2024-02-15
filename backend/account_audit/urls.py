from django.urls import path
from .views import UserListAPIView, AccountListAPIView, AuditListAPIView

urlpatterns = [
    path('users', UserListAPIView.as_view(), name="users"),
    path('accounts', AccountListAPIView.as_view(), name="accounts"),
    path('audits', AuditListAPIView.as_view(), name="audits"),
]
