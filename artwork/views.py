from django.views.generic import TemplateView, ListView, DetailView
from .models import Artwork, Document
from itertools import chain
from operator import attrgetter


class ContentList(TemplateView):
    """Content list view"""

    template_name = "artwork_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artwork = Artwork.objects.all().filter(is_default=False)
        documents = Document.objects.all()

        content_list = sorted(chain(artwork, documents), key=attrgetter("created"), reverse=True)
        context["content_list"] = content_list

        return context


# class ArtworkList(ListView):
#     """Artwork list view"""

#     model = Artwork
#     template_name = "artwork_list.html"


class ArtworkDetail(DetailView):
    """Artwork Detail View"""

    model = Artwork
    template_name = "artwork_detail.html"


class AllArtworkCharacters(DetailView):
    """All Content for a Artwork View"""

    model = Artwork
    template_name = "extra_details/all_artwork_characters.html"


class AllArtworkStories(DetailView):
    """All Stories associated with a Artwork View"""

    model = Artwork
    template_name = "extra_details/all_artwork_stories.html"


class DocumentDetail(DetailView):
    """Document Detail View"""

    model = Document
    template_name = "document_detail.html"


class AllDocumentCharacters(DetailView):
    """All Content for a Document View"""

    model = Document
    template_name = "extra_details/all_document_characters.html"


class AllDocumentStories(DetailView):
    """All Stories associated with a Document View"""

    model = Document
    template_name = "extra_details/all_document_stories.html"
