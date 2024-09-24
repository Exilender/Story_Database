from django.core.management.base import BaseCommand
from artwork.models import Artwork

import shutil


class Command(BaseCommand):
    help = "Creates default Artwork"

    def handle(self, *args, **kwargs):
        # Create or update the default Artwork entries

        # copies the source images from static to media regardless if the files already exist
        shutil.copytree("static/images/", "media/images/", dirs_exist_ok=True)

        default_images = [
            {
                "image_link": "images/Icon_Story.png",
                "art_type": 1,
                "finish_level": 5,
                "creator_name": "Exilender",
                "title": "Icon Story",
                "image_description": "Default Story Icon",
                "is_default": True,
            },
            {
                "image_link": "images/Icon_Document.png",
                "art_type": 1,
                "finish_level": 5,
                "creator_name": "Exilender",
                "title": "Icon Document",
                "image_description": "Default Document Icon",
                "is_default": True,
            },
            {
                "image_link": "images/Icon_Animal.png",
                "art_type": 1,
                "finish_level": 5,
                "creator_name": "Exilender",
                "title": "Icon Animal",
                "image_description": "Default Animal Icon",
                "is_default": True,
            },
            {
                "image_link": "images/Icon_Anthro.png",
                "art_type": 1,
                "finish_level": 5,
                "creator_name": "Exilender",
                "title": "Icon Anthro",
                "image_description": "Default Anthro Icon",
                "is_default": True,
            },
            {
                "image_link": "images/Icon_Human.png",
                "art_type": 1,
                "finish_level": 5,
                "creator_name": "Exilender",
                "title": "Icon Human",
                "image_description": "Default Human Icon",
                "is_default": True,
            },
        ]

        for image in default_images:
            artwork, created = Artwork.objects.update_or_create(
                title=image["title"],
                defaults={
                    "image_link": image["image_link"],
                    "art_type": image["art_type"],
                    "finish_level": image["finish_level"],
                    "creator_name": image["creator_name"],
                    "image_description": image["image_description"],
                    "is_default": image["is_default"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created {artwork.title}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Updated {artwork.title}"))

        self.stdout.write(self.style.SUCCESS("Default artworks created or updated successfully."))
