from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app.views import ColourTypesViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Swatches API",
        default_version='v1',
        description="API for Kanopi Swatches Assessment",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('colour_types/', ColourTypesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('generate_colours', ColourTypesViewSet.as_view({'get': 'generate_colours'}))
]
