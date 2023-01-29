from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("iainteractive.apps.common.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    staticpatterns = static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    mediapatterns = static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    debugpatterns = [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns = staticpatterns + mediapatterns + debugpatterns + urlpatterns