from django.views.generic import ListView, DetailView
from .models import Story


class StoryList(ListView):
    """Story list view"""

    model = Story
    template_name = "story_list.html"


class StoryDetail(DetailView):
    """Story Detail View"""

    model = Story
    template_name = "story_detail.html"

    # def get_context_data(self, *args, **kwargs):
    # # Getting all the stories a character is in

    #     context = super().get_context_data()

    #     # OMG this works?!
    #     story_character_is_in = CharacterImageLink.objects.filter(
    #         story_character_is_in=self.kwargs["pk"]
    #     )

    #     context.update(
    #         {
    #             "artwork_for_story": story_character_is_in,
    #         }
    #     )
    #     return context


class AllStoryContent(DetailView):
    """All Content in a Story View"""

    model = Story
    template_name = "extra_details/all_story_content.html"


class AllStoryCharacters(DetailView):
    """All Characters in a Story View"""

    model = Story
    template_name = "extra_details/all_story_characters.html"
