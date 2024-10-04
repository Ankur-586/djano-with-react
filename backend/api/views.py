from .models import Note
from .serializers import UserSerializers, NoteSerilaizer

from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]

class CreateNoteView(generics.ListCreateAPIView): # read-write endpoints
    serializer_class = NoteSerilaizer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'detail': 'Note created successfully', 'note': serializer.data}, status=status.HTTP_201_CREATED)
        
class DeleteNoteView(generics.DestroyAPIView):
    serializer_class = NoteSerilaizer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # This retrieves the note instance based on the URL
        self.perform_destroy(instance)
        return Response({'detail': 'Note deleted successfully'}, status=status.HTTP_204_NO_CONTENT)