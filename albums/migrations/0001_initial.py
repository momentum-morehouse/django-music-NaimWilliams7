# Generated by Django 3.1.2 on 2020-10-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('artist', models.CharField(blank=True, max_length=255, null=True)),
                ('year_released', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
