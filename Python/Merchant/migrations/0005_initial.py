# Generated by Django 5.0 on 2024-02-20 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0008_remove_tbl_user_district'),
        ('Merchant', '0004_delete_tbl_ad'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=500)),
                ('ad_description', models.CharField(max_length=500)),
                ('ad_image', models.FileField(upload_to='Assets/AdsImage/')),
                ('merchant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_merchant')),
            ],
        ),
    ]
