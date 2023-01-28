# Generated by Django 2.2.4 on 2023-01-22 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0007_auto_20230122_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='engineer',
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='product_app.User'),
        ),
    ]
