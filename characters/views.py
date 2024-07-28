from django.views.generic import TemplateView, ListView, DetailView
from artwork.models import Artwork, Document
from .models import Character
from utils.mixins import AllCharacterContentMixin

from stories.models import Story


class CharacterList(ListView):
    """Character list view"""

    model = Character
    template_name = "character_list.html"


class CharacterDetail(AllCharacterContentMixin, DetailView):
    """Character Detail View"""

    model = Character
    template_name = "character_detail.html"
    context_object_name = "character"


class AllCharacterContent(AllCharacterContentMixin, DetailView):
    """All Content for a Character View"""

    model = Character
    template_name = "extra_details/all_character_content.html"
    context_object_name = "character"



class AllCharacterStories(DetailView):
    """All Stories associated with a Character View"""

    model = Character
    template_name = "extra_details/all_character_stories.html"
