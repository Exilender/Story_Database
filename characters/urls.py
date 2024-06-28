from django.urls import path

from .views import CharacterList, CharacterDetail, AllCharacterContent, AllCharacterStories


urlpatterns = [
    path("character/", CharacterList.as_view(), name="character"),
    path("character/<int:pk>/", CharacterDetail.as_view(), name="character_detail"),
    path("character/<int:pk>/content/", AllCharacterContent.as_view(), name="all_character_content"),
    path("character/<int:pk>/stories/", AllCharacterStories.as_view(), name="all_character_stories"),
]
