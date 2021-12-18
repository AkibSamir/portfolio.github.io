# Generated by Django 3.2 on 2021-12-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=200)),
                ('period', models.CharField(blank=True, max_length=200)),
                ('institute', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]