from django.urls import path
from .views import CreateNoteView, DeleteNoteView

urlpatterns = [
    path('create_note/',CreateNoteView.as_view(),name='create-note'),
    path('delete_note/<int:pk>/',DeleteNoteView.as_view(),name='delete-note'),
]
