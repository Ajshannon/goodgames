# Generated by Django 2.1.4 on 2018-12-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodgames', '0004_auto_20181219_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
