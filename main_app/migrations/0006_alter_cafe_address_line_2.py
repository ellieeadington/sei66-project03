# Generated by Django 4.1.1 on 2022-10-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_cafe_address_line_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
