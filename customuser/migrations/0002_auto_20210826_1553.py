# Generated by Django 3.2.6 on 2021-08-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(default=113),
        ),
        migrations.AddField(
            model_name='myuser',
            name='display_name',
            field=models.CharField(default='Dude', max_length=30),
            preserve_default=False,
        ),
    ]
