from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import process_client_org_xlsx, process_bills_xlsx

from .models import Clients, Organizations, Bills, add_client, add_organization, add_bill

from .serializers import ClientsSerializer, BillsSerializer


# Create your views here.

class ImportClientsApiView(APIView):

    def post(self, request):
        xls = request.FILES['filename']
        clients_to_add, organizations_to_add = process_client_org_xlsx(xls)
        add_client(clients_to_add)
        add_organization(organizations_to_add)

        return Response({'status': 'file received'}, status=status.HTTP_201_CREATED)


class ImportBillsApiView(APIView):

    def post(self, request):
        xls = request.FILES['filename']
        bills_to_add = process_bills_xlsx(xls)
        add_bill(bills_to_add)

        return Response({'status': 'file received'}, status=status.HTTP_201_CREATED)


class ClientsDetailsApiView(APIView):

    def get(self, request):
        clients = Clients.objects.all()
        serializer = ClientsSerializer(clients, many=True)

        for i in range(len(serializer.data)):
            org_count = Organizations.objects.filter(client_name=clients[i]).count()
            organizations_count = {'organizations count': org_count}
            serializer.data[i].update(organizations_count)

            bills_sum = Bills.objects.filter(client_name=clients[i]).aggregate(Sum('sum'))
            _, sum_value = bills_sum.popitem()
            client_sum = {'client organizations bills sum': sum_value}
            serializer.data[i].update(client_sum)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BillsDetails(APIView):

    def get(self, request):
        all_bills = Bills.objects.all()
        serializer = BillsSerializer(all_bills, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BillsDetailsByClient(APIView):

    def get(self, request, client_name):
        client = Clients.objects.get(name=client_name)
        bills_by_client = Bills.objects.filter(client_name=client.id)
        serializer = BillsSerializer(bills_by_client, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BillsDetailsByOrganization(APIView):

    def get(self, request, organization_name):
        organization = Organizations.objects.get(name=organization_name)
        bills_by_organization = Bills.objects.filter(client_org=organization.id)
        serializer = BillsSerializer(bills_by_organization, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
