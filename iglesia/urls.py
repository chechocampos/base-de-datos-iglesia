from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin de Django
    path('feligreses/', include('feligreses.urls')),  # URLs de feligreses
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),  # Logout redirige a login
    path('accounts/', include('django.contrib.auth.urls')),  # Agregar autenticación de Django

    # Redirección protegida al listado de feligreses
    path('', login_required(RedirectView.as_view(url='/feligreses/', permanent=False))),
]

