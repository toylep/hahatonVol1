# Generated by Django 5.0 on 2023-12-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_delete_tgtoken_delete_tguser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]