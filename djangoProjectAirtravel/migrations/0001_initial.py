# Generated by Django 4.1.7 on 2023-03-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traveller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=20)),
                ('phone', models.IntegerField(blank=True, max_length=20)),
                ('origin', models.CharField(blank=True, max_length=20)),
                ('destination', models.CharField(blank=True, max_length=20)),
                ('payment', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]