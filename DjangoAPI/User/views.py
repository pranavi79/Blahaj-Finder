from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from User.models import Blahaj,Users
from User.serializers import BlahajSerializer,UsersSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def blahajApi(request,id=0):
    if request.method=='GET':
        blahaj = Blahaj.objects.all()
        blahaj_serializer=BlahajSerializer(blahaj,many=True)
        return JsonResponse(blahaj_serializer.data,safe=False)
    elif request.method=='POST':
        blahaj_data=JSONParser().parse(request)
        blahaj_serializer=BlahajSerializer(data=blahaj_data)
        if blahaj_serializer.is_valid():
            blahaj_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        blahaj_data=JSONParser().parse(request)
        blahaj=Blahaj.objects.get(BlahajId=blahaj_data['BlahajId'])
        blahaj_serializer=BlahajSerializer(blahaj,data=blahaj_data)
        if blahaj_serializer.is_valid():
            blahaj_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        blahaj=Blahaj.objects.get(BlahajId=id)
        blahaj.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def usersApi(request,id=0):
    if request.method=='GET':
        users = Users.objects.all()
        users_serializer=UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method=='POST':
        users_data=JSONParser().parse(request)
        users_serializer=UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        users_data=JSONParser().parse(request)
        user=Users.objects.get(UsersId=users_data['UsersId'])
        users_serializer=UsersSerializer(user,data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        user=Users.objects.get(UsersId=id)
        user.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)