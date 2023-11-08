from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('', views.index),
    path('members', views.members_only),
    path('register', views.register),
    path('login/', TokenObtainPairView.as_view()),
    path('products', views.Product_view.as_view()),
    path('categories', views.Category_view.as_view())

]
