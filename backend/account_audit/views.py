from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Account, Audit, UserProfile
from .serializers import GroupSerializer, UserSerializer, UserProfileSerializer, AccountSerializer, AuditSerializer
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets


# ====================================================================
# |                            USER                                  |
# ====================================================================
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


# ====================================================================
# |                           GROUP                                  |
# ====================================================================
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# ====================================================================
# |                           ACCOUNT                                |
# ====================================================================
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


# ====================================================================
# |                           AUDIT                                  |
# ====================================================================
class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [permissions.IsAuthenticated]