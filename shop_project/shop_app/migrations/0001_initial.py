# Generated by Django 5.1.2 on 2024-10-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('image_source', models.CharField(max_length=20)),
            ],
        ),
    ]
