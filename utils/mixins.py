"""Creating custom mixins to reuse the same query for multiple views"""

from artwork.models import Artwork, Document

from itertools import chain
from operator import attrgetter


class AllCharacterContentMixin:
    """For the list of all content on the Character Detail page"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artwork = Artwork.objects.filter(content_characters=self.object)
        documents = Document.objects.filter(document_characters=self.object)

        content_list = sorted(chain(artwork, documents), key=attrgetter("created"), reverse=True)
        context["content_list"] = content_list
        return context


class AllStoryContentMixin:
    """For the list of all content on the Story Detail page"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artwork = Artwork.objects.filter(story_content=self.object)
        documents = Document.objects.filter(story_document=self.object)

        content_list = sorted(chain(artwork, documents), key=attrgetter("created"), reverse=True)
        context["content_list"] = content_list
        return context