# Generated by Django 4.0.3 on 2022-04-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0004_alter_image_upload_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='upload',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
