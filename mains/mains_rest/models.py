from django.db import models

from .services import fraud_detector, service_classification, address_correction

from enum import Enum


# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


def add_client(clients_list: list):
    for client in clients_list:
        Clients.objects.create(name=client)


class Organizations(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    client_name = models.ForeignKey(Clients, on_delete=models.CASCADE)
    fraud_weight = models.IntegerField(default=0)

    class Meta:
        unique_together = (('name', 'client_name'),)

    def __str__(self):
        return self.name


def add_organization(organizations: list):
    clients = Clients.objects.all()
    clients_dict = {}
    for client in clients:
        clients_dict[client.name] = client.id

    for organization in organizations:
        name = organization[1]
        address = address_correction(organization[2])
        client_name_id = clients_dict[organization[0]]

        Organizations.objects.create(
            name=name,
            address=address,
            client_name_id=client_name_id,
        )


class FraudValues(Enum):
    fraud_score_bound = 0.9


def fraud_score_increase(client, organization):
    fraud_bill_organization = Organizations.objects.get(client_name=client, name=organization)
    fraud_bill_organization.fraud_weight += 1
    fraud_bill_organization.save(update_fields=['fraud_weight'])


class Bills(models.Model):
    client_name = models.ForeignKey(Clients, on_delete=models.CASCADE)
    client_org = models.ForeignKey(Organizations, on_delete=models.CASCADE)

    number = models.IntegerField()
    sum = models.FloatField()
    date = models.DateField()
    service = models.CharField(max_length=128)

    fraud_score = models.FloatField()

    service_class = models.IntegerField()
    service_name = models.CharField(max_length=64)

    class Meta:
        unique_together = (('client_org', 'number'),)

    def __str__(self):
        return f'{self.client_org}: #{self.number}'


def add_bill(bills: list):
    for bill in bills:
        client = Clients.objects.get(name=bill[0])
        client_org = Organizations.objects.get(client_name=client.id, name=bill[1])
        number = bill[2]
        bill_sum = bill[3]
        date = bill[4]
        service = bill[5]
        fraud_score = fraud_detector(bill[5])
        service_classification_data = service_classification(bill[5])
        service_class = service_classification_data['service_class']
        service_name = service_classification_data['service_name']

        Bills.objects.create(
            client_name=client,
            client_org=client_org,
            number=number,
            sum=bill_sum,
            date=date,
            service=service,
            fraud_score=fraud_score,
            service_class=service_class,
            service_name=service_name,
        )

        if fraud_score >= FraudValues.fraud_score_bound.value:
            fraud_score_increase(client, client_org)
