from django.shortcuts import render
from rest_framework import generics
from .models import User, Account, Audit
from .serializers import UserSerializer, AccountSerializer, AuditSerializer

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    

class AccountListAPIView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()
    

class AuditListAPIView(generics.ListAPIView):
    serializer_class = AuditSerializer

    def get_queryset(self):
        return Audit.objects.all()