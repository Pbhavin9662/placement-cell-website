# Generated by Django 3.0 on 2020-04-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0008_auto_20200413_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_vaccancy',
            name='apply_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
