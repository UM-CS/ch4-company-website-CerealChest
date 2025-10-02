from django.urls import path

from .views import home_page_view, AboutPageView, ProductsView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("products/", ProductsView.as_view(), name="products"),
    path("", home_page_view, name="home"),
]