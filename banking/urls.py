
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('auth/', include("authentication.urls"))
    #ath('admin/', admin.site.urls),
    path("auth/", include("authentication.urls", namespace="authentication_app")),
    
]


