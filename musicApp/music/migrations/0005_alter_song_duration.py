# Generated by Django 5.1.3 on 2024-11-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_listeninghistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.FloatField(),
        ),
    ]
