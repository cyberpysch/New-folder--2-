# Generated by Django 4.2.6 on 2023-10-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]