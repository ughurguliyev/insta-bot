# Generated by Django 3.1.3 on 2020-12-16 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201217_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Note'),
        ),
    ]
