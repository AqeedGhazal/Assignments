# Generated by Django 2.2.4 on 2022-12-16 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_remove_ninja_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default=' old dojo', max_length=45),
        ),
    ]