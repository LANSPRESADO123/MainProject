# Generated by Django 5.0 on 2024-02-11 21:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nadmin', '0009_tbl_department_tbl_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=30)),
                ('employee_contact', models.CharField(max_length=30)),
                ('employee_email', models.CharField(max_length=30)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nadmin.tbl_department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nadmin.tbl_designation')),
            ],
        ),
    ]
