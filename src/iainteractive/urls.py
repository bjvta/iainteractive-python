from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from iainteractive.apps.api.router import urlpatterns as api_urls


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path("", include("iainteractive.apps.common.urls")),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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