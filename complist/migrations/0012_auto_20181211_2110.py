# Generated by Django 2.1.3 on 2018-12-12 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complist', '0011_auto_20181211_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compdetails',
            name='BN',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='GN',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='ORA',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='ORN',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='ORS',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='RRN',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='SN',
        ),
        migrations.RemoveField(
            model_name='compdetails',
            name='SRN',
        ),
        migrations.AddField(
            model_name='comp',
            name='BN',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='comp',
            name='GN',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='comp',
            name='ORA',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='comp',
            name='ORN',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='comp',
            name='ORS',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='comp',
            name='RRN',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='comp',
            name='SN',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='comp',
            name='SRN',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='compdetails',
            name='competitor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complist.Comp'),
        ),
    ]
