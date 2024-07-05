from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Student
from rest_framework.permissions import IsAuthenticated
from .serializers import SignupSerializer,LoginSerializer,StudentSerializer
class SignupAPIView(APIView):
    """This api will handle signup"""
    def post(self,request):
            serializer = SignupSerializer(data = request.data)
            if serializer.is_valid():
                    """If the validation success, it will created a new user."""
                    serializer.save()
                    res = { 'status' : status.HTTP_201_CREATED }
                    return Response(res, status = status.HTTP_201_CREATED)
            res = { 'status' : status.HTTP_400_BAD_REQUEST, 'data' : serializer.errors }
            return Response(res, status = status.HTTP_400_BAD_REQUEST)
class LoginAPIView(APIView):
    def post(self,request):
        data=LoginSerializer(data=request.data)
        if data.is_valid():
            username=data.validated_data['username']
            password=data.validated_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                token=Token.objects.get(user=user)
                response = {
                                 "status": status.HTTP_200_OK,
                                 "message": "success",
                                 "data": {
                                       "Token" : token.key
                                       }
                               }
                return Response(response, status = status.HTTP_200_OK)
            else:
                    response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Email or Password",
                               }
                    return Response(response, status = status.HTTP_401_UNAUTHORIZED)
        response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": data.errors
                 }
        return Response(response, status = status.HTTP_400_BAD_REQUEST)
            
            
class StudentAPIView(APIView):
    """This api will handle student"""
    permission_classes = [IsAuthenticated]
    def get(self,request):
            data = Student.objects.all()
            serializer = StudentSerializer(data, many = True)
            response = {
                   "status": status.HTTP_200_OK,
                   "message": "success",
                   "abhishek": serializer.data
                   }
            return Response(response, status = status.HTTP_200_OK)
