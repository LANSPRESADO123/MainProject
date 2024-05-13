# Generated by Django 5.0 on 2024-02-27 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_remove_tbl_user_district'),
        ('Merchant', '0015_delete_tbl_event'),
        ('Nadmin', '0017_delete_tb_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=500)),
                ('event_description', models.CharField(max_length=500)),
                ('event_fromdate', models.DateField()),
                ('event_todate', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_status', models.IntegerField(default='0')),
                ('event_location', models.CharField(max_length=500)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_merchant')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nadmin.tbl_place')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nadmin.tbl_subcat')),
            ],
        ),
    ]