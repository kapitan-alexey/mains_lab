from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import import_xls_clients

from .models import Clients, create_client, create_organization


# Create your views here.

class ImportClientsApiView(APIView):

    def get(self, request):
        return Response({'status': 'ok'}, status.HTTP_200_OK)

    def post(self, request):
        xls = request.FILES['filename']

        clients_to_create, organizations_to_create = import_xls_clients(xls)

        create_client(clients_to_create)
        create_organization(organizations_to_create)

        print(Clients.objects.all())

        return Response({'status': 'file received'}, status=status.HTTP_201_CREATED)
