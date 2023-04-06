from django.shortcuts import render
from .serializers import *
from .models import VCard
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
class VCardView(APIView):
    vcard = VCard.objects.all()
    serializer=VCardSericlizer(vcard,many=True)
    def get(self,req):
        return Response(self.serializer.data,status=200)
    def post(self,req):
        data={
            "name":req.POST.get("name"),
            "contact":req.POST.get("contact")
        }
        serializer =VCardSericlizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)

class VCardDetails(generics.GenericAPIView):
    serializer_class=VCardSericlizer
    
    def get(self,req,id=None):
        singleVCard=VCard.objects.get(id=id)
        serializer=VCardSericlizer(singleVCard)
        return Response(serializer.data,status=200)
    
    def delete(self,req,id=None):
        singleVCard =VCard.objects.get(id=id)
        singleVCard.delete()
        return Response(statuse=200)
    
    def patch(self,req,id=None):
        singleVCard=VCard.objects.get(id=id)
        serializer=VCardSericlizer(singleVCard,data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response({"msg":"record not updated","error":serializer.errors})

class MyTockenObjectPaieView(TokenObtainPairView):
    permission_classes=(AllowAny,)
    serializer_class=MyTockenObjectPaieSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class=RegisterSerializer