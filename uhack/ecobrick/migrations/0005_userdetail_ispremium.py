# Generated by Django 2.0.2 on 2018-06-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecobrick', '0004_userdetail_brickpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='isPremium',
            field=models.BooleanField(default=False),
        ),
    ]
