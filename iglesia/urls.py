from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', lambda request: redirect('feligreses/', permanent=False)),
    path('admin/', admin.site.urls),
    path('feligreses/', include('feligreses.urls')),
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]

