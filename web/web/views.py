from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from web.web.urls import UserSerializer


def home(request, template="home.html"):
    return render(request, template)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer