from django.contrib import admin
from django.urls import path, include
from dados.views import ClienteViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register('Cliente', ClienteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('dados.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
