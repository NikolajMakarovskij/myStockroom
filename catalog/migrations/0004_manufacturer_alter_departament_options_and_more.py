# Generated by Django 4.0.6 on 2022-10-25 06:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_departament_name_alter_employee_employeeemail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='manufacturer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите наименование производителя', max_length=150, verbose_name='Производитель')),
                ('country', models.CharField(help_text='Введите название страны', max_length=150, verbose_name='Страна')),
                ('production', models.CharField(help_text='Введите страну производства', max_length=150, verbose_name='Страна производства')),
            ],
            options={
                'verbose_name_plural': 'Производитель',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='departament',
            options={'ordering': ['name'], 'verbose_name_plural': 'Отдел'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['name'], 'verbose_name_plural': 'Должность'},
        ),
        migrations.AlterModelOptions(
            name='software',
            options={'ordering': ['name', 'workstation'], 'verbose_name_plural': 'ПО'},
        ),
        migrations.RemoveField(
            model_name='software',
            name='Employee',
        ),
        migrations.AddField(
            model_name='software',
            name='bitDepth',
            field=models.CharField(blank=True, help_text='Укажите разрядность', max_length=200, null=True, verbose_name='разрядность'),
        ),
        migrations.AddField(
            model_name='software',
            name='version',
            field=models.CharField(blank=True, help_text='Укажите версию', max_length=200, null=True, verbose_name='Версию'),
        ),
        migrations.AlterField(
            model_name='software',
            name='licenseKeyFile',
            field=models.FileField(blank=True, help_text='прикрепите файл', null=True, upload_to='soft/', verbose_name='Файл лицензии'),
        ),
        migrations.AlterField(
            model_name='software',
            name='licenseKeyImg',
            field=models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='soft/', verbose_name='Фото ключа'),
        ),
        migrations.AlterField(
            model_name='software',
            name='licenseKeyText',
            field=models.CharField(blank=True, help_text='Введите лицензтонный ключ', max_length=50, null=True, verbose_name='Введите ключ'),
        ),
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(help_text='Введите название ПО', max_length=50, verbose_name='Програмное обеспечение'),
        ),
        migrations.AlterField(
            model_name='software',
            name='workstation',
            field=models.ForeignKey(blank=True, help_text='Укажите рабочую станцию', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workstation', verbose_name='Рабочая станция'),
        ),
        migrations.AlterField(
            model_name='software',
            name='manufacturer',
            field=models.ForeignKey(blank=True, help_text='Укажите производителя', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.manufacturer', verbose_name='Производитель'),
        ),
    ]
