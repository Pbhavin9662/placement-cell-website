# Generated by Django 3.0 on 2020-04-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0007_auto_20200406_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='profile_pic',
            field=models.ImageField(blank=True, default='basicpic.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, default='basicpic.png', null=True, upload_to=''),
        ),
    ]
