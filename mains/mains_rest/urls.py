from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ImportClientsApiView

# router = DefaultRouter()
# router.register('xls-client', ImportClientsApiView, basename='excel client')

urlpatterns = [
    path('clients', ImportClientsApiView.as_view())
]
