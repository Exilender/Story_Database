from django.urls import reverse
from django.db import models

import math


class Character(models.Model):
    """Defining the individual characters that may be linked to Stories or Content"""

    char_icon = models.ForeignKey(
        "artwork.Artwork",
        on_delete=models.PROTECT,
        related_name="char_icon",
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    # This is in whole number years
    age = models.IntegerField()

    gender_choices = ((1, "Male"), (2, "Female"), (3, "Non-Binary"))
    gender = models.IntegerField(choices=gender_choices, default=3)

    species_choices = (
        (1, "Deity"),
        (2, "Guardian"),
        (3, "Human"),
        (4, "Umbra"),
        (5, "Underland"),
        (6, "Xerioplatis"),
        (7, "Numen"),
        (8, "Familiar"),
    )
    species = models.IntegerField(choices=species_choices, default=1)

    # This is describing the appearance of the character
    species_desc = models.CharField(max_length=100)

    # data should look like: 5'7
    height_ft = models.CharField(max_length=5)

    # data should look like: 170
    height_cm = models.IntegerField(editable=False)

    # Water, Earth, Fire, etc.. are types of magic
    fighting_style_choices = (
        (1, "Doesnt fight"),
        (2, "Physical fighter"),
        (3, "Water"),
        (4, "Earth"),
        (5, "Fire"),
        (6, "Electricity"),
        (7, "Wind"),
        (8, "Arcane"),
        (9, "Ancient Magic"),
    )
    fighting_style = models.IntegerField(choices=fighting_style_choices, default=1)

    # Describing the unique fighting style of the charater; aka what their ability does
    fighting_style_desc = models.CharField(max_length=500)

    # Anything unique to the character
    char_notes = models.TextField(blank=True, null=True)

    # Comment out these two fields to first makemigrations then run migrations, then uncomment to makemigrations and run migrations again.
    character_stories = models.ManyToManyField("stories.Story", blank=True, related_name="character_stories")
    character_content = models.ManyToManyField("artwork.Artwork", blank=True, related_name="character_content")
    character_document = models.ManyToManyField("artwork.Document", blank=True, related_name="character_document")
    ####################################################

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String method"""
        return self.first_name[:50]

    def get_absolute_url(self):
        """Method for getting the absolute URL of project detail"""
        character_reverse = reverse("character_detail", kwargs={"pk": self.pk})
        return character_reverse

    def save(self, *args, **kwargs):
        # Calculate the value before saving to the database
        # expected data 5'7

        delimeters = "'"

        for delimeter in delimeters:
            input = " ".join(self.height_ft.split(delimeter))

        list_items = input.split()

        # converting to cm
        ft_to_cm = float(list_items[0]) * 30.48
        in_to_cm = float(list_items[1]) * 2.54

        self.height_cm = math.ceil(ft_to_cm + in_to_cm)
        super(Character, self).save(*args, **kwargs)
