# Generated by Django 2.2.4 on 2023-01-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_remove_review_engineer'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='phoneNumber',
            field=models.IntegerField(null=True),
        ),
    ]
