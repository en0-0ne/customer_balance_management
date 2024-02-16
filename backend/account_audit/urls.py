from django.urls import path
from .views import UserListAPIView, UserCreateAPIView,UserDetailAPIView, AccountListAPIView, AccountCreateAPIView, AccountDetailAPIView, AuditListAPIView, AuditCreateAPIView, AuditDetailAPIView

urlpatterns = [
    # users
    path('users', UserListAPIView.as_view(), name="users"),
    path('users/create', UserCreateAPIView.as_view(), name="users"),
    path('users/<int:id>', UserDetailAPIView.as_view(), name="users"),

    # accounts
    path('accounts', AccountListAPIView.as_view(), name="accounts"),
    path('accounts/create', AccountCreateAPIView.as_view(), name="accounts"),
    path('accounts/<int:id>', AccountDetailAPIView.as_view(), name="accounts"),

    # audits
    path('audits', AuditListAPIView.as_view(), name="audits"),
    path('audits/create', AuditCreateAPIView.as_view(), name="audits"),
    path('audits/<int:id>', AuditDetailAPIView.as_view(), name="audits"),
]
