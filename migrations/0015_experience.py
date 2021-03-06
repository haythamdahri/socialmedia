# Generated by Django 2.0.4 on 2018-05-06 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20180507_0038'),
        ('SocialMedia', '0014_offreemploi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_entreprise', models.CharField(max_length=300)),
                ('nom_poste', models.CharField(max_length=300)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('actuel', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
                ('entreprise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Entreprise')),
                ('poste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Poste')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil')),
            ],
        ),
    ]
