# Generated by Django 5.0.4 on 2024-11-06 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_forum_total_views_forumcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumcomment',
            name='rating',
        ),
    ]