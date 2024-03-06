# Generated by Django 4.2.3 on 2024-03-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_rename_year_of_passin_hsec_employeeeducation_year_of_passing_hsec_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
