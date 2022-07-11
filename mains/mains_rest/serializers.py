from rest_framework import serializers

from .models import Clients, Bills


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['name']


class BillsSerializer(serializers.ModelSerializer):

    client_name = serializers.StringRelatedField()
    client_org = serializers.StringRelatedField()

    class Meta:
        model = Bills
        fields = ['client_name', 'client_org', 'bill_number', 'sum', 'date', 'service', 'fraud_score', 'service_class',
                  'service_name']
