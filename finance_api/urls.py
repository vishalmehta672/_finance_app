from django.urls import path,include
from .views import *


urlpatterns = [
    path('create_inventory_specific_contact/',create_inventory_specific_contact, name='create-contact'),
    path('create_inventory_specific_deal/',create_inventory_specific_deal, name='create-deal'),
    path('create_general_application_contact/',create_general_application_contact),
    path('create_general_application_deals/',create_general_application_deals),
    path('create_manual_application_contact/',create_manual_application_contact),
    path('create_manual_application_deals/',create_manual_application_deals)
]
