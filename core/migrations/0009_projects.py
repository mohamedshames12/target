# Generated by Django 4.2 on 2023-04-17 03:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_profile_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='project_images')),
                ('name', models.CharField(max_length=100)),
                ('descriptoin', models.TextField(blank=True)),
            ],
        ),
    ]