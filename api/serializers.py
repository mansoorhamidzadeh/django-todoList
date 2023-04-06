from rest_framework import serializers
from base.models import  Task
class TaskSerializer(serializers.ModelSerializer):
    # detail=serializers.HyperlinkedIdentityField(
    #     view_name='todoListDetailApiView',)


    class Meta:
        model=Task
        fields=[
            'id',

            'title',
            'description',
            'completed',
            'created',
        ]