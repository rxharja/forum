# Generated by Django 2.2.10 on 2020-03-22 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0008_auto_20200322_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='collection_id',
        ),
    ]
