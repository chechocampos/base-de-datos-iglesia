from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin de Django
    path('feligreses/', include('feligreses.urls')),  # URLs de feligreses
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),  # Logout redirige a login
    path('accounts/', include('django.contrib.auth.urls')),  # Agregar autenticación de Django
]
