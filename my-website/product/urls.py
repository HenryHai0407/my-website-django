from django.urls import path

from . import views

app_name = "product"
urlpatterns = [
    path("", views.product, name="list"),
    path("<int:id>", views.detail, name="detail"),
]
