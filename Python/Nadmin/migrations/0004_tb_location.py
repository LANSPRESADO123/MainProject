# Generated by Django 5.0 on 2024-02-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nadmin', '0003_tbl_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=20)),
                ('location_pin', models.CharField(max_length=20)),
            ],
        ),
    ]
