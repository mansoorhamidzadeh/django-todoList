from django.contrib.auth.models import User
from rest_framework import serializers
from base.models import  Task



class UserSerializer(serializers.ModelSerializer):
    taskuser=serializers.PrimaryKeyRelatedField(
        many=True,queryset=Task.objects.all()
    )
    class Meta:
        model = User
        fields = ("id", "username",'taskuser')


class TaskSerializer(serializers.ModelSerializer):
    # detail=serializers.HyperlinkedIdentityField(
    #     view_name='todoListDetailApiView',)

    def username(self,obj):
        return obj.user.username
    user=serializers.SerializerMethodField('username')
    # detail=serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(),many=True)


    class Meta:
        model=Task
        fields=[
            'id',
            'user',
            'title',
            'description',
            'completed',
            'created',
        ]

