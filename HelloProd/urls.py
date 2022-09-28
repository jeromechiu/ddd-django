from django.urls import path

from HelloProd.application.views import ProdApiView

urlpatterns = [path("", ProdApiView.as_view(), name="ProdMgt")]
