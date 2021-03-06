# Generated by Django 2.0.4 on 2018-05-06 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20180507_0038'),
        ('SocialMedia', '0018_organisme'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionBenevole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_organisme', models.CharField(max_length=300)),
                ('nom_poste', models.CharField(max_length=300)),
                ('cause', models.TextField(blank=True, null=True)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('organisme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Organisme')),
                ('poste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Poste')),
                ('profil', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil')),
            ],
        ),
    ]
