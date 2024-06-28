# Generated by Django 5.0.4 on 2024-05-19 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artwork", "0002_artwork_content_characters_artwork_content_stories"),
        ("stories", "0002_story_story_characters_story_story_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="icon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="icon",
                to="artwork.artwork",
            ),
        ),
    ]