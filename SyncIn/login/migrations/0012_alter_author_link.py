# Generated by Django 4.0.1 on 2022-05-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_song_feats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
