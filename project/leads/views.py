# from django.shortcuts import render
from leads.serializers import LeadSerializer
from rest_framework import generics
from .models import Lead

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
