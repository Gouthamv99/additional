# Generated by Django 5.0.4 on 2024-10-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_job_alter_comment_options_alter_comment_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='job',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]