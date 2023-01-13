# Generated by Django 4.1 on 2023-01-13 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counterparty', '0001_initial'),
        ('ups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cassette',
            name='manufacturer',
            field=models.ForeignKey(blank=True, help_text='Укажите производителя', null=True, on_delete=django.db.models.deletion.SET_NULL, to='counterparty.manufacturer', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='ups',
            name='manufacturer',
            field=models.ForeignKey(blank=True, help_text='Укажите производителя', null=True, on_delete=django.db.models.deletion.SET_NULL, to='counterparty.manufacturer', verbose_name='Производитель'),
        ),
    ]
