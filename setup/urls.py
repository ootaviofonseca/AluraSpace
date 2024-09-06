
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.galeria.urls')),
    path('usuarios/',include('apps.usuarios.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #adiciona a url de media para que as imagens possam ser acessadas
