# Generated by Django 2.0.4 on 2018-05-06 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20180504_1726'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SocialMedia', '0011_auto_20180504_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil')),
            ],
        ),
        migrations.CreateModel(
            name='OffreEmploi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5555)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='statut',
            new_name='is_read',
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='liked_by',
        ),
        migrations.RemoveField(
            model_name='statut',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='reseausocialfile',
            name='comment',
            field=models.ManyToManyField(to='SocialMedia.Commentaire'),
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_user', to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='groupe',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createur', to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='reseausocialfile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='statut',
            name='mur_groupe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Groupe'),
        ),
        migrations.AlterField(
            model_name='statut',
            name='mur_profil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mur_profil', to='main_app.Profil'),
        ),
        migrations.AlterField(
            model_name='statut',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='main_app.Profil'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='likes',
            field=models.ManyToManyField(to='SocialMedia.Like'),
        ),
        migrations.AddField(
            model_name='reseausocialfile',
            name='likes',
            field=models.ManyToManyField(to='SocialMedia.Like'),
        ),
        migrations.AddField(
            model_name='statut',
            name='likes',
            field=models.ManyToManyField(to='SocialMedia.Like'),
        ),
    ]