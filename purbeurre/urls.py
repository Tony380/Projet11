from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('legal', views.legal, name='legal'),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('users/', include('users.urls')),
]

handler404 = views.my_404_view
handler500 = views.my_500_view

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)
