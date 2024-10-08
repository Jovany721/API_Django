from app.models import tabla_user
from app.api.serializer import convertidor_jso
from rest_framework import viewsets

class vista_tabla(viewsets.ModelViewSet):

    queryset = tabla_user.objects.all()
    serializer_class= convertidor_jso


    