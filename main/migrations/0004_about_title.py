# Generated by Django 3.2 on 2021-12-17 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211218_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
