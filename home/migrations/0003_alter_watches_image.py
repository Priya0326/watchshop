# Generated by Django 5.1.2 on 2024-11-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_watches_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watches',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='picture'),
        ),
    ]