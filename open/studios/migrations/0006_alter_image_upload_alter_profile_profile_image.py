# Generated by Django 4.0.3 on 2022-04-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0005_alter_image_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='upload',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profiles/user-default.png', null=True, upload_to='images/profiles/'),
        ),
    ]
