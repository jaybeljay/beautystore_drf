from rest_framework import permissions, viewsets

from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
