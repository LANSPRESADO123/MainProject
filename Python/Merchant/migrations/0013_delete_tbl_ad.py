# Generated by Django 5.0 on 2024-02-27 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Merchant', '0012_tbl_ad'),
        ('User', '0024_remove_tbl_review_ad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_ad',
        ),
    ]
