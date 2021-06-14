# Generated by Django 3.0 on 2020-04-05 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0004_auto_20200405_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='success_story',
            name='motivate_notes',
            field=models.TextField(default='Not Writes', max_length=400),
        ),
        migrations.AddField(
            model_name='success_story',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pcapp.Student'),
        ),
        migrations.AddField(
            model_name='success_story',
            name='title',
            field=models.CharField(default='No title', max_length=100),
        ),
    ]