from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from . models import SchemaDetails

from .models import SchemaDetails

class dataMain(serializers.Serializer):
    bank = serializers.CharField(max_length = 10)
    action = serializers.CharField(max_length = 20)
    id = serializers.CharField(max_length = 50, required=False)
    acc_no = serializers.CharField(max_length = 50, required=False)
    username = serializers.CharField(max_length = 50, required=False)
    password = serializers.CharField(max_length = 50, required = False)
    pin = serializers.IntegerField(max_length = 10, required = False)
    amount = serializers.IntegerField(max_length = 100, required = False)
    email = serializers.CharField(max_length = 50, required = False)

def addBankSerializer(serializers.Serialzer):
    bank = serializers.CharField(max_length = 10)


def addBankFuncSerializer(serializers.Serialzer):
    bank = serializers.CharField(max_length = 10)
    action = serializers.CharField(max_length = 20)
    schema = serializers.CharField(max_length = 1000)
