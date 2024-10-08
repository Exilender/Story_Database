from django.db import models
from django.urls import reverse

from artwork.models import Artwork


class Story(models.Model):
    """Defining a Story's table"""

    # Icon is a piece of artwork already uploaded
    icon = models.ForeignKey("artwork.Artwork", on_delete=models.PROTECT, related_name="icon", blank=True, null=True)

    title = models.CharField(max_length=100)

    creator = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="creator",
    )

    description = models.TextField()

    # Comment out these two fields to first makemigrations then run migrations, then uncomment to makemigrations and run migrations again.
    story_characters = models.ManyToManyField(
        "characters.Character",
        blank=True,
        through="characters.Character_character_stories",
        related_name="story_characters",
    )
    story_content = models.ManyToManyField(
        "artwork.Artwork",
        blank=True,
        through="artwork.Artwork_content_stories",
        related_name="story_content",
    )
    story_document = models.ManyToManyField("artwork.Document", blank=True, related_name="story_document")
    ####################################################

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Set a default image based on body_type if no image is provided
        if not self.icon:
            self.icon = self.get_default_artwork("Icon Story")

        super(Story, self).save(*args, **kwargs)

    def get_default_artwork(self, artwork_type):
        # Look up default Artwork by type
        return Artwork.objects.filter(title=artwork_type).first()

    def __str__(self):
        """String method"""
        return self.title[:50]

    def get_absolute_url(self):
        """Method for getting the absolute URL of story detail"""
        story_reverse = reverse("story_detail", kwargs={"pk": self.pk})
        return story_reverse
