from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),             
    path('guides/', include('guides.urls')),       
    path('catalog/', include('catalog.urls')),     
    path('contacto/', include('interaction.urls')),
]
