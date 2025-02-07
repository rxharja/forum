# Generated by Django 2.2.10 on 2020-03-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_auto_20200320_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('collection_id', models.IntegerField(null=True)),
                ('collection_name', models.CharField(blank=True, max_length=255, null=True)),
                ('game_id', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.CharField(blank=True, max_length=1000, null=True)),
                ('rating', models.CharField(blank=True, max_length=255, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection_has_games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('collection_id', models.IntegerField(null=True)),
                ('game_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Recommended',
        ),
    ]
