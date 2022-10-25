# Generated by Django 4.0.6 on 2022-10-24 11:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='departament',
        ),
        migrations.AlterField(
            model_name='employee',
            name='Workplace',
            field=models.ForeignKey(blank=True, help_text='Выберете рабочее место', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workplace', verbose_name='Рабочее место'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeEmail',
            field=models.EmailField(blank=True, help_text='Введие e-mail', max_length=254, null=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='family',
            field=models.CharField(blank=True, help_text='Введите фамилию сотрудника', max_length=50, verbose_name='Фамилию сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, help_text='Введите имя сотрудника', max_length=50, verbose_name='Имя сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(blank=True, help_text='Выберете должность', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.post', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sername',
            field=models.CharField(blank=True, help_text='Введите отчество сотрудника', max_length=50, verbose_name='Отчество сотрудника'),
        ),
        migrations.AlterField(
            model_name='room',
            name='Building',
            field=models.CharField(blank=True, help_text='Введите название здания', max_length=25, verbose_name='Здание'),
        ),
        migrations.AlterField(
            model_name='room',
            name='Floor',
            field=models.CharField(blank=True, help_text='Введите номер этажа', max_length=25, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, help_text='Введите номер кабинета', max_length=15, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='Room',
            field=models.ForeignKey(blank=True, help_text='Выберете номер кабинета', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.room', verbose_name='Номер кабинета'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False, verbose_name='Введите уникальный UUID4)'),
        ),
    ]
