# Generated by Django 2.2.10 on 2020-03-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='genera',
            new_name='genre',
        ),
        migrations.AddField(
            model_name='game',
            name='complexity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
