# Generated by Django 2.2.4 on 2022-12-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV_SHOWS_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='Release_date',
            field=models.DateField(),
        ),
    ]