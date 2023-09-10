from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
class DesignsListAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        artist = request.GET.get('artist')
        query = request.GET.get('query')
        fav = request.GET.get('fav')

        if artist:
            designs = Design.objects.filter(artist__username=artist)
        elif query:
            designs = Design.objects.filter(title__icontains=query)
        elif fav:
            designs = Design.objects.filter(design__liked_by=fav)
        

        else:
            designs = Design.objects.all()
            
        serializer = DesignSerializer(designs, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DesignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response( {'err': 'invalid data'},status=status.HTTP_400_BAD_REQUEST)
    
class DesignAPI(APIView):

    def get_object(self, uuid):
        try:
            return Design.objects.get(uuid=uuid)
        except Design.DoesNotExist:
            raise Http404
        
    def get(self, request, uuid):
        design = self.get_object(uuid)
        serializer = DesignSerializer(design)
        return Response(serializer.data)
    
    def put(self, request, uuid):
        design = self.get_object(uuid)
        serializer = DesignSerializer(design, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, uuid):
        design = self.get_object(uuid)
        design.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LoveAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.GET.get('user')
            design = request.GET.get('design')
            model = Like.objects.get(liked_by=user, design=design)
            return Response(status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"msg":"not found"},status=status.HTTP_200_OK)
        
    
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user = request.GET.get('user')
        design = request.GET.get('design')
        like = Like.objects.get(liked_by=user, design=design)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
