# Generated by Django 4.2.3 on 2023-07-28 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_rename_compamy2name_employeeexperience_company2name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='year_of_passin_hsec',
            new_name='year_of_passing_hsec',
        ),
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='year_of_passin_sec',
            new_name='year_of_passing_sec',
        ),
    ]
