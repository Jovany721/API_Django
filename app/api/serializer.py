from rest_framework import serializers
from app.models import tabla_user



class convertidor_jso(serializers.ModelSerializer):

    class Meta:
        model = tabla_user
        fields ='__all__'