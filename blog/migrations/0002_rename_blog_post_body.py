# Generated by Django 5.0.7 on 2024-08-04 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blog',
            new_name='body',
        ),
    ]