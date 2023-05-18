from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework import generics

from .models import User,Author
from .serializer import UserSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


