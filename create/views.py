from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from stories.models import Story
from characters.models import Character
from artwork.models import Artwork, Document


class AddNew(LoginRequiredMixin, TemplateView):
    """Renders the template for the '+ New' page"""

    template_name = "add_new.html"


class AddStory(LoginRequiredMixin, CreateView):
    """Renders the template for the 'Add Story' page"""

    model = Story
    template_name = "create/add_story.html"
    fields = [
        "icon",
        "title",
        "description",
        "story_characters",
        "story_content",
    ]
    # success_url = reverse_lazy("story")

    def form_valid(self, form):
        """Auto setting the creator"""
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditStory(LoginRequiredMixin, UpdateView):
    """Renders the template for the 'Edit Story' page"""

    model = Story
    template_name = "create/edit_story.html"
    fields = [
        "icon",
        "title",
        "description",
        "story_characters",
        "story_content",
    ]
    # success_url = reverse_lazy("story")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class DeleteStory(LoginRequiredMixin, DeleteView):
    """Renders the template for the 'Delete Story' page"""

    model = Story
    template_name = "create/delete_story.html"
    success_url = reverse_lazy("story")


class AddCharacter(LoginRequiredMixin, CreateView):
    """Renders the template for the 'Add Character' page"""

    model = Character
    template_name = "create/add_character.html"
    fields = [
        "char_icon",
        "first_name",
        "last_name",
        "age",
        "gender",
        "species",
        "species_desc",
        "body_type",
        "height_ft",
        "fighting_style",
        "fighting_style_desc",
        "char_notes",
        "character_stories",
        "character_content",
    ]
    # success_url = reverse_lazy("character")

    def form_valid(self, form):
        """Auto setting the creator"""
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditCharacter(LoginRequiredMixin, UpdateView):
    """Renders the template for the 'Edit Character' page"""

    model = Character
    template_name = "create/edit_character.html"
    fields = [
        "char_icon",
        "first_name",
        "last_name",
        "age",
        "gender",
        "species",
        "species_desc",
        "body_type",
        "height_ft",
        "fighting_style",
        "fighting_style_desc",
        "char_notes",
        "character_stories",
        "character_content",
    ]
    # success_url = reverse_lazy("character")

    def form_valid(self, form):
        """Auto setting the creator"""
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DeleteCharacter(LoginRequiredMixin, DeleteView):
    """Renders the template for the 'Delete Character' page"""

    model = Character
    template_name = "create/delete_character.html"
    success_url = reverse_lazy("character")


class AddContent(LoginRequiredMixin, TemplateView):
    """Renders the template for the 'Add Content' page"""

    template_name = "create/add_content.html"


class AddArtwork(LoginRequiredMixin, CreateView):
    """Renders the template for the 'Add Artwork' page"""

    model = Artwork
    template_name = "create/add_artwork.html"
    fields = [
        "image_link",
        "creator_name",
        "title",
        "art_type",
        "finish_level",
        "image_description",
        "content_characters",
        "content_stories",
    ]
    # success_url = reverse_lazy("artwork")

    def form_valid(self, form):
        """Auto setting the creator"""
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditArtwork(LoginRequiredMixin, UpdateView):
    """Renders the template for the 'Edit Artwork' page"""

    model = Artwork
    template_name = "create/edit_artwork.html"
    fields = [
        "image_link",
        "creator_name",
        "title",
        "art_type",
        "finish_level",
        "image_description",
        "content_characters",
        "content_stories",
    ]
    # success_url = reverse_lazy("artwork")

    def form_valid(self, form):
        """Auto setting the creator"""
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DeleteArtwork(LoginRequiredMixin, DeleteView):
    """Renders the template for the 'Delete Content' page"""

    model = Artwork
    template_name = "create/delete_artwork.html"
    success_url = reverse_lazy("artwork")


class AddDocument(LoginRequiredMixin, CreateView):
    """Renders the template for the 'Add Document' page"""

    model = Document
    template_name = "create/add_document.html"
    fields = [
        "document_link",
        "creator_name",
        "title",
        "document_description",
        "document_characters",
        "document_stories",
    ]
    success_url = reverse_lazy("artwork")

    def form_valid(self, form):
        """Auto setting the creator"""
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditDocument(LoginRequiredMixin, UpdateView):
    """Renders the template for the 'Edit Document' page"""

    model = Document
    template_name = "create/edit_document.html"
    fields = [
        "document_link",
        "creator_name",
        "title",
        "document_description",
        "document_characters",
        "document_stories",
    ]
    #
    # success_url = reverse_lazy("artwork")

    def form_valid(self, form):
        """Auto setting the creator"""
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DeleteDocument(LoginRequiredMixin, DeleteView):
    """Renders the template for the 'Delete Document' page"""

    model = Document
    template_name = "create/delete_document.html"
    success_url = reverse_lazy("artwork")
