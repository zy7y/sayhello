"""say URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import include, path
from rest_framework import routers, permissions
from sayHello import views

# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'message', views.TextViewSet)


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
    permission_classes=(permissions.AllowAny,),
)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        '',
        include(
            router.urls)),
    path(
        'api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework')),
    path(
        'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0),
        name='schema-swagger-ui'),
    path(
        'redoc/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0),
        name='schema-redoc'),
]
