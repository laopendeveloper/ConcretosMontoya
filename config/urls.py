from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('machines.urls', 'machines'), namespace='machines')),
    path('tools/', include(('tools.urls', 'tools'), namespace='tools')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
