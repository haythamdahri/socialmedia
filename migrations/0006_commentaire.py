# Generated by Django 2.0.4 on 2018-05-06 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20180507_0038'),
        ('SocialMedia', '0005_statut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=6000)),
                ('date_commentaire', models.DateField()),
                ('have_image', models.BooleanField(default=False)),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Image')),
                ('likes', models.ManyToManyField(to='SocialMedia.Like')),
                ('statut', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Statut')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_user', to='main_app.Profil')),
            ],
        ),
    ]
