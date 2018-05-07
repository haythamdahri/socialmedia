# Generated by Django 2.0.4 on 2018-05-06 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20180507_0038'),
        ('SocialMedia', '0016_ecole'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_formation', models.CharField(blank=True, max_length=300, null=True)),
                ('nom_ecole', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('nom_formation', models.CharField(max_length=300, null=True)),
                ('domaine', models.CharField(blank=True, max_length=300, null=True)),
                ('resultat_obtenu', models.CharField(blank=True, max_length=300, null=True)),
                ('activite_et_associations', models.TextField(blank=True, null=True)),
                ('annee_debut', models.DateField()),
                ('annee_fin', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('ecole', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Ecole')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profil')),
            ],
        ),
    ]