# Generated by Django 5.0.1 on 2024-01-10 05:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='comapany_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='contact',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(default='vendor', max_length=255, null=True),
        ),
    ]