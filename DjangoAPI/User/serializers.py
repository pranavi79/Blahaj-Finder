from rest_framework import serializers
from User.models import Blahaj,Users

class BlahajSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blahaj 
        fields=('BlahajId','BlahajName')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users 
        fields=('UserId','UserName','Blahaj','DateOfJoining','PhotoFileName')