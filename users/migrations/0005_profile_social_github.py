# Generated by Django 3.1.6 on 2021-08-10 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_github',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]