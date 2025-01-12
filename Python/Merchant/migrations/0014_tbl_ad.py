# Generated by Django 5.0 on 2024-02-27 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_remove_tbl_user_district'),
        ('Merchant', '0013_delete_tbl_ad'),
        ('Nadmin', '0017_delete_tb_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=500)),
                ('ad_description', models.CharField(max_length=500)),
                ('ad_image', models.FileField(upload_to='Assets/AdsImage/')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_merchant')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nadmin.tbl_place')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nadmin.tbl_subcat')),
            ],
        ),
    ]
