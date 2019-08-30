from django.conf.urls import url, include
from .swagger_schema import SwaggerSchemaView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from demo import settings
from django.conf.urls.static import static

API_TITLE = 'Tipti API Documentation'
API_DESCRIPTION = 'A Web API for consulting information about API.  '
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cbv/', include('demo.cbv_demo.urls')),
    url(r'^fbv/', include('demo.fbv_demo.urls')),
    url(r'^swagger/', SwaggerSchemaView.as_view()),
    url(r'^doc/', schema_view),
    url(r'^docs/', include_docs_urls(API_TITLE, API_DESCRIPTION))
] + static(settings.STATIC_URL)
