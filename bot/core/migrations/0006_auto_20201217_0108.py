# Generated by Django 3.1.3 on 2020-12-16 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201217_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='default_img_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.file'),
        ),
    ]
