# Generated by Django 5.0.6 on 2024-08-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/portfolio')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='We_do',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/we_do')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
            ],
        ),
    ]
