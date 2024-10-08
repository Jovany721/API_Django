from django.urls import include, path
from app.api.views import vista_tabla
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register('consulta', vista_tabla)
urlpatterns= router.urls