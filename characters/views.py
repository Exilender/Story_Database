from django.views.generic import TemplateView, ListView, DetailView
from artwork.models import Artwork, Document
from .models import Character

from stories.models import Story


class CharacterList(ListView):
    """Character list view"""

    model = Character
    template_name = "character_list.html"


class CharacterDetail(DetailView):
    """Character Detail View"""

    model = Character
    template_name = "character_detail.html"


class AllCharacterContent(DetailView):
    """All Content for a Character View"""

    model = Character
    template_name = "extra_details/all_character_content.html"
    context_object_name = "character"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artwork"] = self.object.artwork.all()
        context["documents"] = self.object.documents.all()
        return context


class AllCharacterStories(DetailView):
    """All Stories associated with a Character View"""

    model = Character
    template_name = "extra_details/all_character_stories.html"
