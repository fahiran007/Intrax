# Generated by Django 4.0.6 on 2022-09-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timefrom', models.CharField(max_length=50)),
                ('timeTo', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('Minutes', models.CharField(max_length=50)),
                ('dateToday', models.CharField(max_length=50)),
                ('ListingDate', models.CharField(max_length=50)),
            ],
        ),
    ]
