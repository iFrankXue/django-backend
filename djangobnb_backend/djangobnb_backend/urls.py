from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/properties/', include('property.urls')),
    path('api/auth/', include('useraccount.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/properties/', include('property.urls'))    
# ] 

# urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
