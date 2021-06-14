# Generated by Django 3.0 on 2020-04-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0003_auto_20200312_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Success_Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/')),
            ],
        ),
        migrations.AlterField(
            model_name='add_vaccancy',
            name='apply_date',
            field=models.DateField(default='15/03/19'),
        ),
        migrations.AlterField(
            model_name='add_vaccancy',
            name='last_date',
            field=models.DateField(default='20/02/20'),
        ),
    ]
