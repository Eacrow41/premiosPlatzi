# Generated by Django 4.1.7 on 2023-02-15 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_rename_choices_choice"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice", old_name="choise_text", new_name="choice_text",
        ),
    ]
