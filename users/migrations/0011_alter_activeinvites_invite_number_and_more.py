# Generated by Django 5.2.2 on 2025-07-10 12:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_activeinvites_invite_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeinvites',
            name='invite_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Инвайт'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activeinvites',
            name='invite_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='Инвайт URL'),
            preserve_default=False,
        ),
    ]
