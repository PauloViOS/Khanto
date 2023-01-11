from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from imoveis.views import ImoveisViewset

router = routers.DefaultRouter()
router.register('imoveis', ImoveisViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
