# Generated by Django 2.0.2 on 2018-04-15 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180415_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydata',
            name='Med_1',
            field=models.CharField(max_length=120),
        ),
    ]
