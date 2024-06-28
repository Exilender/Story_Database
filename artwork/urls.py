from django.urls import path

from .views import (
    ContentList,
    ArtworkDetail,
    AllArtworkCharacters,
    AllArtworkStories,
    DocumentDetail,
    AllDocumentCharacters,
    AllDocumentStories,
)


urlpatterns = [
    # path("artwork/", ArtworkList.as_view(), name="artwork"),
    path("artwork/", ContentList.as_view(), name="artwork"),
    path("artwork/<int:pk>/", ArtworkDetail.as_view(), name="artwork_detail"),
    path("artwork/<int:pk>/characters/", AllArtworkCharacters.as_view(), name="all_artwork_characters"),
    path("artwork/<int:pk>/stories/", AllArtworkStories.as_view(), name="all_artwork_stories"),
    path("document/<int:pk>/", DocumentDetail.as_view(), name="document_detail"),
    path("document/<int:pk>/characters/", AllDocumentCharacters.as_view(), name="all_document_characters"),
    path("document/<int:pk>/stories/", AllDocumentStories.as_view(), name="all_document_stories"),
]
