from django.urls import path

from .views import (
    AddNew,
    AddStory,
    EditStory,
    DeleteStory,
    AddCharacter,
    EditCharacter,
    DeleteCharacter,
    AddContent,
    AddArtwork,
    EditArtwork,
    DeleteArtwork,
    AddDocument,
    EditDocument,
    DeleteDocument,
)

urlpatterns = [
    path("new/", AddNew.as_view(), name="add_new"),
    path("new/story/", AddStory.as_view(), name="add_story"),
    path("edit/story/<int:pk>/", EditStory.as_view(), name="edit_story"),
    path("delete/story/<int:pk>/", DeleteStory.as_view(), name="delete_story"),
    path("new/character/", AddCharacter.as_view(), name="add_character"),
    path("edit/character/<int:pk>/", EditCharacter.as_view(), name="edit_character"),
    path("delete/character/<int:pk>/", DeleteCharacter.as_view(), name="delete_character"),
    path("new/content/", AddContent.as_view(), name="add_content"),
    path("new/content/artwork/", AddArtwork.as_view(), name="add_artwork"),
    path("edit/content/artwork/<int:pk>/", EditArtwork.as_view(), name="edit_artwork"),
    path("delete/content/artwork/<int:pk>/", DeleteArtwork.as_view(), name="delete_artwork"),
    path("new/content/document/", AddDocument.as_view(), name="add_document"),
    path("edit/content/document/<int:pk>/", EditDocument.as_view(), name="edit_document"),
    path("delete/content/document/<int:pk>/", DeleteDocument.as_view(), name="delete_document"),
]
