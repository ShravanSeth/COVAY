# Generated by Django 3.2 on 2021-04-26 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('just_co_away', '0013_alter_listing_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='date_verified_on',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]