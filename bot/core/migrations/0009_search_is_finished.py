# Generated by Django 3.1.3 on 2020-12-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='is_finished',
            field=models.BooleanField(null=True, verbose_name='Finished'),
        ),
    ]