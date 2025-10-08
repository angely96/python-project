from django.urls import path
from . import views

app_name = "authentication_app"

urlpatterns=[
    path("",views.index,name="index"),
    #path("countries",views.countries,name="countries"),
    #path("depart",views.depart,name="departments"),
    #path("cities",views.cities,name="cities")
    path("countries/", views.country_list, name="country_list"),
    path("countries/<int:pk>/edit/", views.country_edit, name="country_edit"),
    path('countries/delete/<int:pk>/', views.country_delete, name='country_delete'),

]

