from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin de Django
    path('feligreses/', include('feligreses.urls')),  # URLs de la app feligreses
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),  # Logout con redirección al login
    path('accounts/', include('django.contrib.auth.urls')),  # Login y autenticación de Django
    path('', lambda request: redirect('feligreses/')),  # Redirigir la raíz al módulo de feligreses
]
