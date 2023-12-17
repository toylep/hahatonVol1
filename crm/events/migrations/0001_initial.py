# Generated by Django 5.0 on 2023-12-17 03:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DevEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('users', models.ManyToManyField(related_name='devevents', to=settings.AUTH_USER_MODEL)),
                ('event_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.eventtype')),
            ],
        ),
    ]