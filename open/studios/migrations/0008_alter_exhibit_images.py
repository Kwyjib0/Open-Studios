# Generated by Django 4.0 on 2021-12-10 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0007_alter_exhibit_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='images',
            field=models.ForeignKey(default=int, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='exhibit', to='studios.image'),
        ),
    ]
