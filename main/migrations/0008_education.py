# Generated by Django 3.2 on 2021-12-17 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211218_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=200)),
                ('period', models.CharField(blank=True, max_length=200)),
                ('institute', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
