# Generated by Django 2.0.4 on 2018-05-04 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0006_auto_20180504_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reseausocialfile',
            old_name='fichier_album',
            new_name='album',
        ),
    ]
