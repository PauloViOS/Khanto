from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from imoveis.views import ImoveisViewset
from anuncios.views import AnunciosViewset


router = routers.DefaultRouter()
router.register('imoveis', ImoveisViewset)
router.register('anuncios', AnunciosViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
