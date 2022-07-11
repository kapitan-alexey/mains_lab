from django.urls import path

from .views import ImportClientsApiView, ImportBillsApiView, ClientsDetailsApiView, BillsDetails, BillsDetailsByClient, BillsDetailsByOrganization

urlpatterns = [
    path('xls-clients/', ImportClientsApiView.as_view()),
    path('xls-bills/', ImportBillsApiView.as_view()),
    path('clients/', ClientsDetailsApiView.as_view()),
    path('bills/', BillsDetails.as_view()),
    path('bills/client/<str:client_name>/', BillsDetailsByClient.as_view()),
    path('bills/organization/<str:organization_name>/', BillsDetailsByOrganization.as_view()),
]
