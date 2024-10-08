# Generated by Django 5.0.4 on 2024-09-24 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artwork", "0005_rename_image_title_artwork_title_and_more"),
        ("stories", "0004_story_story_document"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="icon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="icon",
                to="artwork.artwork",
            ),
        ),
    ]
