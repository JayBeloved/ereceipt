# Generated by Django 4.2.6 on 2023-10-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Amount',
            field=models.FloatField(blank=True, max_length=40, null=True, verbose_name='Amount Paid'),
        ),
    ]
