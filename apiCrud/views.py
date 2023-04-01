from django.shortcuts import render
from .serializers import VCardSericlizer
from .models import VCard
from rest_framework.views import APIView
from rest_framework.response import Response

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