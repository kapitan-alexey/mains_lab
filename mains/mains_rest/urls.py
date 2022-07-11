from django.urls import path

from .views import ImportClientsApiView, ImportBillsApiView, ClientsDetailsApiView, BillsDetails, BillsDetailsByClient, BillsDetailsByOrganization

urlpatterns = [
    path('api/xls-clients/', ImportClientsApiView.as_view()),
    path('api/xls-bills/', ImportBillsApiView.as_view()),
    path('api/clients/', ClientsDetailsApiView.as_view()),
    path('api/bills/', BillsDetails.as_view()),
    path('api/bills/client/<str:client_name>/', BillsDetailsByClient.as_view()),
    path('api/bills/organization/<str:organization_name>/', BillsDetailsByOrganization.as_view()),
]
