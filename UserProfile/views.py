from django.shortcuts import render
from rest_framework import viewsets
from UserProfile.models import Profile
from UserProfile.serializers import ProfileSerializer
# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer