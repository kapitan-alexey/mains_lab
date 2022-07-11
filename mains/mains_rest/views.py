from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import process_client_org_xlsx, process_bills_xlsx

from .models import add_client, add_organization, add_bill


# Create your views here.

class ImportClientsApiView(APIView):

    def get(self, request):
        return Response({'status': 'ok'}, status.HTTP_200_OK)

    def post(self, request):
        xls = request.FILES['filename']

        clients_to_add, organizations_to_add = process_client_org_xlsx(xls)

        add_client(clients_to_add)
        add_organization(organizations_to_add)

        return Response({'status': 'file received'}, status=status.HTTP_201_CREATED)


class ImportBillsApiView(APIView):

    def get(self, request):
        return Response({'status': 'ok'}, status.HTTP_200_OK)

    def post(self, request):
        xls = request.FILES['filename']

        bills_to_add = process_bills_xlsx(xls)

        add_bill(bills_to_add)

        return Response({'status': 'file received'}, status=status.HTTP_201_CREATED)