from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer, UserMediaSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework import generics
from .models import UserMedia
from django import http
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from rest_framework.decorators import permission_classes

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class UsersAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request):
       model = User.objects.all()
       serializer = UserSerializer(model, many=True)
       return Response(serializer.data)
    
class UserNameAPI(APIView):

  def get(self, request, pk):
    user = User.objects.get(pk=pk)
    return Response({'username': user.username})
  
class UserMediaAPI(APIView):

  @permission_classes([IsAuthenticated])
  def get_object(self, username):
    try:
      media = UserMedia.objects.get(user__username=username)
      return media
    except UserMedia.DoesNotExist:
      raise http.Http404


  def get(self, request, username):
    model = self.get_object(username)
    serializer = UserMediaSerializer(model)
    return Response(serializer.data, status=status.HTTP_200_OK)

  @permission_classes([IsAuthor])
  def patch(self, request, username):
    user_m = self.get_object(username)
    serializer = UserMediaSerializer(user_m, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

