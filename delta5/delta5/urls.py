from django.contrib import admin
from django.urls import path, include  # <--- DODAJ 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delta_app.urls')), # <--- DOPISZ TĘ LINIJKĘ
]