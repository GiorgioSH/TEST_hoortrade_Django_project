# Generated by Django 2.2 on 2020-09-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200913_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='avis',
            field=models.CharField(choices=[('Excellent film, je recommende', 'Excellent film je recommande'), ('Je ne le reverrai pas une deuxième fois', 'Je ne le reverrai pas une deuxième fois'), ('Je ne le conseillerai pas', 'Je ne le conseillerai pas')], max_length=200, null=True),
        ),
    ]
