from django.urls import path
from .views import UserListAPIView, UserCreateAPIView,UserDetailAPIView, AccountListAPIView, AuditListAPIView

urlpatterns = [
    path('users', UserListAPIView.as_view(), name="users"),
    path('users/create', UserCreateAPIView.as_view(), name="users"),
    path('user/<int:id>', UserDetailAPIView.as_view(), name="user"),
    path('accounts', AccountListAPIView.as_view(), name="accounts"),
    path('audits', AuditListAPIView.as_view(), name="audits"),
]
