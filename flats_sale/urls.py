from django.urls import path

from flats_sale.views import SaleListView

app_name = "flats_sale"
urlpatterns = [
    path('sale/', SaleListView.as_view(), name = "sale"),
]