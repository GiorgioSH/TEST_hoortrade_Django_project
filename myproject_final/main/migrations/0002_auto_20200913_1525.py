# Generated by Django 2.2 on 2020-09-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acteur',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='realisateur',
            name='prenom',
        ),
        migrations.AlterField(
            model_name='acteur',
            name='age',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='acteur',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='acteur',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='Date_de_sortie',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='realisateur',
            name='age',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='realisateur',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='realisateur',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
