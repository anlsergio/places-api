# Generated by Django 2.1.7 on 2019-03-31 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190331_0014'),
        ('core', '0002_place_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='comments',
            field=models.ManyToManyField(to='comments.Comment'),
        ),
    ]