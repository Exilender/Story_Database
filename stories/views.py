from django.views.generic import ListView, DetailView
from .models import Story
from utils.mixins import AllStoryContentMixin


class StoryList(ListView):
    """Story list view"""

    model = Story
    template_name = "story_list.html"


class StoryDetail(AllStoryContentMixin, DetailView):
    """Story Detail View"""

    model = Story
    template_name = "story_detail.html"
    context_object_name = "story"



class AllStoryContent(AllStoryContentMixin, DetailView):
    """All Content in a Story View"""

    model = Story
    template_name = "extra_details/all_story_content.html"
    context_object_name = "story"


class AllStoryCharacters(DetailView):
    """All Characters in a Story View"""

    model = Story
    template_name = "extra_details/all_story_characters.html"
