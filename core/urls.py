from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # admin panel django
    path('account/', include('account.urls')),  # app account
    path('product/', include('product.urls')),  # app product
    path('oauth/', include('social_django.urls', namespace='social'))  # login GitHub
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
