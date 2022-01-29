from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import auth_login as login, auth_logout as logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('app.urls')),
                  path('chat/', include('chat.urls')),
                  path('accounts/login/', login),
                  path('accounts/logout/', logout),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
