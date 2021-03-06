# Generated by Django 2.1.3 on 2018-12-11 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complist', '0008_auto_20181211_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compdetails',
            old_name='time',
            new_name='competitor_name',
        ),
        migrations.AddField(
            model_name='compdetails',
            name='ORA',
            field=models.CharField(default='n/a', max_length=50),
        ),
        migrations.AddField(
            model_name='compdetails',
            name='ORS',
            field=models.CharField(default='n/a', max_length=50),
        ),
        migrations.AddField(
            model_name='compdetails',
            name='pb_average',
            field=models.CharField(default='DNF', max_length=50),
        ),
        migrations.AddField(
            model_name='compdetails',
            name='pb_single',
            field=models.CharField(default='DNF', max_length=50),
        ),
        migrations.AlterField(
            model_name='compdetails',
            name='competitor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complist.Comp'),
        ),
    ]
