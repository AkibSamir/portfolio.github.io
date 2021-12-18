# Generated by Django 3.2 on 2021-12-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('sub_title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('birthday', models.DateField()),
                ('age', models.IntegerField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('degree', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('freelace', models.CharField(blank=True, max_length=100)),
                ('extra_info', models.TextField(blank=True)),
            ],
        ),
    ]
