# Generated by Django 4.1.5 on 2023-01-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_SITE_URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.CharField(max_length=50)),
            ],
        ),
    ]
