# Generated by Django 5.0 on 2024-02-27 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_remove_tbl_user_district'),
        ('Merchant', '0014_tbl_ad'),
        ('User', '0025_delete_tbl_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.CharField(max_length=500)),
                ('review_content', models.CharField(max_length=500)),
                ('review_postdate', models.DateField(auto_now_add=True)),
                ('review_posttime', models.TimeField(auto_now_add=True)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Merchant.tbl_ad')),
                ('merchant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_merchant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
