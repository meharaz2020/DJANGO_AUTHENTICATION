 
from django.contrib import admin
from django.urls import path, include
# from Login_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Login_app.urls')),
]
