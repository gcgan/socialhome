# Generated by Django 2.0.8 on 2018-09-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_populate_profile_fid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
