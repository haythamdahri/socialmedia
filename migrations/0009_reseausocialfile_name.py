# Generated by Django 2.0.4 on 2018-05-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0008_auto_20180504_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseausocialfile',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
