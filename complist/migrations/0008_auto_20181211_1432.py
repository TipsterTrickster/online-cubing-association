# Generated by Django 2.1.3 on 2018-12-11 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complist', '0007_auto_20181211_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compdetails',
            name='compcomp',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='compcountry',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='compgender',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='compsolves',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='compstate',
        ),
        migrations.AddField(
            model_name='comp',
            name='compcomp',
            field=models.CharField(default='DEFAULT VALUE', max_length=100000),
        ),
        migrations.AddField(
            model_name='comp',
            name='compcountry',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
        migrations.AddField(
            model_name='comp',
            name='compgender',
            field=models.CharField(default='DEFAULT VALUE', max_length=10),
        ),
        migrations.AddField(
            model_name='comp',
            name='compsolves',
            field=models.CharField(default='DEFAULT VALUE', max_length=1000000),
        ),
        migrations.AddField(
            model_name='comp',
            name='compstate',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
        migrations.AlterField(
            model_name='compdetails',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complist.Comp'),
        ),
    ]
