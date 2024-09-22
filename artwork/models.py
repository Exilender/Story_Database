from django.urls import reverse
from django.db import models


class Artwork(models.Model):
    """Storing all of the Artwork that can be linked to Stories or Characters"""

    image_link = models.ImageField(upload_to="images/")

    # Digital or Traditional?
    art_type_choices = (
        (1, "Digital"),
        (2, "Traditional"),
    )
    art_type = models.IntegerField(choices=art_type_choices, default=1)

    # How much of the drawing is finished?
    finish_level_choices = (
        (1, "Lined"),
        (2, "Flat"),
        (3, "Cel"),
        (4, "Painted"),
        (5, "Other"),
    )
    finish_level = models.IntegerField(choices=finish_level_choices, default=1)

    creator_name = models.CharField(
        max_length=100,
    )

    title = models.CharField(
        max_length=250,
    )

    image_description = models.TextField(blank=True, null=True)

    # Comment out these two fields to first makemigrations then run migrations, then uncomment to makemigrations and run migrations again.
    content_characters = models.ManyToManyField(
        "characters.Character",
        blank=True,
        through="characters.Character_character_content",
        related_name="content_characters",
    )
    content_stories = models.ManyToManyField("stories.Story", blank=True, related_name="content_stories")
    ####################################################

    # For including different versions of the same image together
    # image_version = models.ManyToManyField("ImageVersions", blank=True, related_name="image_version")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String method"""
        return self.title[:50]

    def get_absolute_url(self):
        """Method for getting the absolute URL of image detail"""
        character_reverse = reverse("artwork_detail", kwargs={"pk": self.pk})
        return character_reverse


class Document(models.Model):
    """Storing all of the Documents that can be linked to Stories or Characters"""

    document_link = models.FileField(upload_to="documents/")

    # document_image = models.ForeignKey(
    #     "artwork.Artwork",
    #     on_delete=models.PROTECT,
    #     related_name="document_image",
    #     blank=True,
    # )

    creator_name = models.CharField(
        max_length=100,
    )

    title = models.CharField(
        max_length=250,
    )

    document_description = models.TextField(blank=True, null=True)

    # Comment out these two fields to first makemigrations then run migrations, then uncomment to makemigrations and run migrations again.
    document_characters = models.ManyToManyField(
        "characters.Character",
        blank=True,
        through="characters.Character_character_document",
        related_name="document_characters",
    )
    document_stories = models.ManyToManyField(
        "stories.Story",
        blank=True,
        through="stories.Story_story_document",
        related_name="document_stories",
    )
    ####################################################

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String method"""
        return self.title[:50]

    def get_absolute_url(self):
        """Method for getting the absolute URL of image detail"""
        document_reverse = reverse("document_detail", kwargs={"pk": self.pk})
        return document_reverse
