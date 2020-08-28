from rest_framework import serializers
from weatherapp.models import User_list

class UserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_list
        fields = '__all__'