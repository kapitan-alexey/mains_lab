from django.db import models


# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


def create_client(clients_list):
    for client in clients_list:
        Clients.objects.create(name=client)


class Organizations(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    client_name = models.ForeignKey(Clients, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'client_name'),)

    def __str__(self):
        return self.name


def create_organization(organizations):
    clients = Clients.objects.all()
    clients_dict = {}
    for client in clients:
        clients_dict[client.name] = client.id

    for organization in organizations:
        Organizations.objects.create(
            name=organization[1],
            address=organization[2],
            client_name_id=clients_dict[organization[0]]
        )
