# Generated by Django 4.2.10 on 2024-02-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_email_profile_facebook_profile_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=254, unique=True),
        ),
    ]
