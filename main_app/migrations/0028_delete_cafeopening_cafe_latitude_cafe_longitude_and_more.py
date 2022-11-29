# Generated by Django 4.1.1 on 2022-11-29 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0027_alter_cafe_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CafeOpening',
        ),
        migrations.AddField(
            model_name='cafe',
            name='latitude',
            field=models.DecimalField(decimal_places=25, max_digits=250, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='longitude',
            field=models.DecimalField(decimal_places=25, max_digits=250, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address_city',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address_country',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address_county',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address_line_1',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address_line_2',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address_postcode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='cafe_bio',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='cafe_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='coffee_beans',
            field=models.ManyToManyField(null=True, to='main_app.coffeebean'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='date_founded',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]