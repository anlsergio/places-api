# Generated by Django 2.1.7 on 2019-03-31 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='vuser',
            new_name='user',
        ),
    ]
