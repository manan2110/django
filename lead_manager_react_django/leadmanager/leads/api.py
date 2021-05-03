from leads.models import *
from rest_framework import viewsets, permissions
from .serializers import *

# Lead Viewset helps us create full crud api without having to specify explicit methods for the functionality


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
