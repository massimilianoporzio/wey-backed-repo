
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('api/', include('account.urls')),  # URL per la gestione degli utenti
    path('admin/', admin.site.urls),
    
]
