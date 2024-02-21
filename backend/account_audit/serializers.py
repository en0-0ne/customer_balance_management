from rest_framework import serializers
from .models import Account, Audit, UserProfile
from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        depth = 1


class AuditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audit
        fields = "__all__"
        depth = 1