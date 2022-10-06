# Generated by Django 4.1.1 on 2022-10-05 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0015_remove_cafe_coffee_beans_remove_cafe_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='coffee_beans',
            field=models.ManyToManyField(to='main_app.coffeebean'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
