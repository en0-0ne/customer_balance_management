from rest_framework import serializers
from .models import User, Account, Audit


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"


class AuditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audit
        fields = "__all__"