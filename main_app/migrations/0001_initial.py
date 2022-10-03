
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrewingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brewing_method', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe_name', models.CharField(max_length=250)),
                ('cafe_bio', models.CharField(max_length=2500)),
                ('date_founded', models.DateField()),
                ('address_line_1', models.CharField(max_length=250)),
                ('address_line_2', models.CharField(max_length=250)),
                ('address_city', models.CharField(max_length=250)),
                ('address_county', models.CharField(max_length=250)),
                ('address_country', models.CharField(max_length=250)),
                ('address_postcode', models.CharField(max_length=10)),
                ('cafe_image', models.ImageField(default='no image uploaded', upload_to='main_app/static/uploads')),
                ('menu_image', models.ImageField(default='no image uploaded', upload_to='main_app/static/uploads')),
                ('cafe_website', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CafeOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday_open', models.CharField(max_length=250)),
                ('open_from', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeBean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee_bean_name', models.CharField(max_length=250)),
                ('coffee_bean_variety', models.CharField(choices=[('A', 'Arabica'), ('R', 'Robusta'), ('L', 'Liberica'), ('E', 'Excelsa')], default='A', max_length=1000)),
                ('coffee_bean_description', models.CharField(max_length=2000)),
                ('roastery_name', models.CharField(max_length=250)),
                ('date_harvested', models.CharField(max_length=250)),
                ('coffee_bean_image', models.ImageField(default='no image uploaded', upload_to='main_app/static/uploads')),
                ('coffee_bean_location', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('stars', models.CharField(choices=[('5', '★★★★★'), ('4', '★★★★'), ('3', '★★★'), ('2', '★★'), ('1', '★')], default='5', max_length=2)),
                ('review_title', models.CharField(max_length=250)),
                ('review_body', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=250)),
                ('event_description', models.CharField(max_length=1000)),
                ('event_weekday', models.CharField(max_length=20)),
                ('event_time_from', models.TimeField()),
                ('event_time_to', models.TimeField()),
                ('event_image', models.CharField(max_length=1000)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.cafe')),
            ],
        ),
    ]
