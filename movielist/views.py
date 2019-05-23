from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User

class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = UserSerializer



class queryMovie(APIView):

	def get(self,request,*args,**kwargs):
		page=self.request.query_params.get("page")
		query=self.request.query_params.get("query")
		query_result=get_query(page,query)
		return Response(query_result,status=status.HTTP_200_OK)
