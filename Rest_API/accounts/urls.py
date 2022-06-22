
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.ApiOverView),
    path('Emplist/',views.Emplist,name="Emplist")
    ]