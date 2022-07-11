from django.urls import path

from .views import ImportClientsApiView, ImportBillsApiView

urlpatterns = [
    path('clients', ImportClientsApiView.as_view()),
    path('bills', ImportBillsApiView.as_view())
]
