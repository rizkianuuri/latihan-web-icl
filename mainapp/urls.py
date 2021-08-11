from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('count/<int:angka/', views.count),
    path('sapa/<str:nama>', views.sapa),
    path('example/', views.example),
    path('shop/', views.shop),
    path('home/', views.home),
    path('profile/', views.profile),
    path('second/', views.second_page),
    path('', views.landing_page),
]