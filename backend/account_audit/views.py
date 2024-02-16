from django.shortcuts import render
from rest_framework import generics, response, status
from .models import User, Account, Audit
from .serializers import UserSerializer, AccountSerializer, AuditSerializer



# ====================================================================
# |                         USER                                     |
# ====================================================================
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    
class UserDetailAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    
    def get(self, request, id):
        query_set = User.objects.filter(id=id).first()
        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)

    

# ====================================================================
# |                         ACCOUNT                                  |
# ====================================================================
class AccountListAPIView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()

class AccountCreateAPIView(generics.CreateAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()
    
class AccountDetailAPIView(generics.GenericAPIView):
    serializer_class = AccountSerializer
    
    def get(self, request, id):
        query_set = Account.objects.filter(id=id).first()
        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)
    

# ====================================================================
# |                         AUDIT                                    |
# ====================================================================
class AuditListAPIView(generics.ListAPIView):
    serializer_class = AuditSerializer

    def get_queryset(self):
        return Audit.objects.all()

class AuditCreateAPIView(generics.CreateAPIView):
    serializer_class = AuditSerializer

    def get_queryset(self):
        return Audit.objects.all()
    
class AuditDetailAPIView(generics.GenericAPIView):
    serializer_class = AuditSerializer
    
    def get(self, request, id):
        query_set = Audit.objects.filter(id=id).first()
        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)