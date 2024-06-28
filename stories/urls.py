from django.urls import path

from .views import StoryList, StoryDetail, AllStoryContent, AllStoryCharacters


urlpatterns = [
    path("", StoryList.as_view(), name="story"),
    path("story/<int:pk>/", StoryDetail.as_view(), name="story_detail"),
    path("story/<int:pk>/content/", AllStoryContent.as_view(), name="all_story_content"),
    path("story/<int:pk>/characters/", AllStoryCharacters.as_view(), name="all_story_characters"),
]
