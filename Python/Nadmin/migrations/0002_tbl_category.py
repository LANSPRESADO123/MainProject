# Generated by Django 5.0 on 2024-01-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
    ]