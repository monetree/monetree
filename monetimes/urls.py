from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from landing.views import landing
from django.conf.urls import handler404, handler500
from landing.views import error_404, error_500, error_404_demo, error_500_demo

urlpatterns = [
    path('', landing),
    path('error_404_demo/', error_404_demo, name='error_404_demo'),
    path('error_500_demo/', error_500_demo, name='error_500_demo'),
]

handler404 = error_404
handler500 = error_500

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
