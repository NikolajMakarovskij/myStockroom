# Generated by Django 4.0.5 on 2022-07-30 04:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Building')),
            ],
            options={
                'verbose_name_plural': 'Здание',
            },
        ),
        migrations.CreateModel(
            name='cartridge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите название модели', max_length=50, verbose_name='Модель')),
                ('manufactured', models.CharField(blank=True, help_text='Введите название производителя', max_length=50, null=True, verbose_name='Производитель')),
                ('serial', models.CharField(blank=True, help_text='Введите серийный номер', max_length=50, null=True, verbose_name='Серийный номер')),
                ('serialImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='printer/cartridge/', verbose_name='Серийный номер')),
                ('buhCode', models.CharField(help_text='Введите код по бухгалтерии', max_length=50, verbose_name='Код в бухгалтерии')),
                ('score', models.IntegerField(blank=True, help_text='Введите количество на складе', null=True, verbose_name='Остаток на складе')),
            ],
            options={
                'verbose_name_plural': 'картридж',
            },
        ),
        migrations.CreateModel(
            name='departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название отдела', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Отдел',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите ФИО сотрудника', max_length=50, verbose_name='ФИО сотрудника')),
            ],
            options={
                'verbose_name_plural': 'Сотрудник',
                'ordering': ['name', '-Workplace'],
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите номер этажа', max_length=15)),
                ('Building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.building')),
            ],
            options={
                'verbose_name_plural': 'Этаж',
            },
        ),
        migrations.CreateModel(
            name='monitor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите Название модели', max_length=50, verbose_name='Модель')),
                ('manufacturer', models.CharField(blank=True, help_text='Введите Название производителя', max_length=50, null=True, verbose_name='Производитель')),
                ('serial', models.CharField(blank=True, help_text='Введите серийный номер', max_length=50, null=True)),
                ('serialImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='monitor/serial/')),
                ('invent', models.CharField(blank=True, help_text='Введите инвентаризационный номер', max_length=50, null=True)),
                ('inventImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='monitor/invent/')),
            ],
            options={
                'verbose_name_plural': 'Монитор',
            },
        ),
        migrations.CreateModel(
            name='motherboard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите Название модели', max_length=50)),
                ('manufacturer', models.CharField(blank=True, help_text='Введите Название производителя', max_length=50, null=True, verbose_name='Производитель')),
                ('serial', models.CharField(blank=True, help_text='Введите серийный номер', max_length=50, null=True)),
                ('serialImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='motherboard/')),
                ('invent', models.CharField(blank=True, help_text='Введите серийный номер', max_length=50, null=True)),
                ('inventImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='motherboard/')),
                ('CPUSoket', models.TextField(blank=True, help_text='Описание сокета', max_length=200, null=True, verbose_name='CPU Soket')),
                ('RAMSlot', models.TextField(blank=True, help_text='Описание RAM', max_length=200, null=True, verbose_name='RAM Slot')),
                ('USBPort', models.TextField(blank=True, help_text='Введите количество и тип', max_length=200, null=True, verbose_name='USB Port')),
                ('COMPort', models.TextField(blank=True, help_text='Введите количество', max_length=200, null=True, verbose_name='COM Port')),
                ('PCI_E', models.TextField(blank=True, help_text='Введите количество', max_length=200, null=True, verbose_name='PCI Express')),
                ('PCI', models.TextField(blank=True, help_text='Введите количество и тип', max_length=200, null=True, verbose_name='PCI')),
                ('VGA', models.TextField(blank=True, help_text='Введите количество', max_length=200, null=True)),
                ('SATA', models.TextField(blank=True, help_text='Введите количество', max_length=200, null=True)),
                ('HDMI', models.TextField(blank=True, help_text='Введите количество', max_length=200, null=True)),
                ('DispayPort', models.TextField(blank=True, help_text='Введите количество', max_length=200, null=True)),
                ('powerSupply', models.TextField(blank=True, help_text='Введите конфигурацию', max_length=200, null=True, verbose_name='Питание материнской платы')),
                ('powerSupplyCPU', models.TextField(blank=True, help_text='Введите конфигурацию', max_length=200, null=True, verbose_name='Питание CPU')),
            ],
            options={
                'verbose_name_plural': 'Материнская плата',
            },
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите Название ОС', max_length=50, verbose_name='Название')),
                ('manufacturer', models.CharField(blank=True, help_text='Описание производителя', max_length=200, null=True, verbose_name='Производитель')),
                ('licenseKeyText', models.CharField(blank=True, help_text='Введите лицензтонный ключ', max_length=50, null=True)),
                ('licenseKeyImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='OS/')),
                ('licenseKeyFile', models.FileField(blank=True, help_text='прикрепите файл', null=True, upload_to='soft/')),
            ],
            options={
                'verbose_name_plural': 'ОС',
            },
        ),
        migrations.CreateModel(
            name='paper',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите название модели', max_length=50, verbose_name='Название')),
                ('manufactured', models.CharField(blank=True, help_text='Введите название производителя', max_length=50, null=True, verbose_name='Производитель')),
                ('paperFormat', models.CharField(choices=[('A4', 'A4'), ('A3', 'A3'), ('A2', 'A2'), ('A1', 'A1'), ('A0', 'A0'), ('A5', 'A5')], default='A4', help_text='Укажите формат', max_length=5, verbose_name='Формат')),
                ('score', models.IntegerField(blank=True, help_text='Введите количество на складе', null=True, verbose_name='Остаток на складе')),
            ],
            options={
                'verbose_name_plural': 'Бумага',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите номер кабинета', max_length=15)),
                ('Building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.building')),
                ('Floor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.floor')),
            ],
            options={
                'verbose_name_plural': 'Кабинет',
                'ordering': ['Building', 'Floor', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите номер рабочего места', max_length=50, verbose_name='Рабочее место')),
                ('Building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.building', verbose_name='Здание')),
                ('Floor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.floor', verbose_name='Этаж')),
                ('Room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.room', verbose_name='Номер кабинета')),
            ],
            options={
                'verbose_name_plural': 'Рабочее место',
                'ordering': ['-Building', '-Floor', 'Room'],
            },
        ),
        migrations.CreateModel(
            name='workstation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите номер станции', max_length=50, verbose_name='Рабочая станция')),
                ('manufacturer', models.CharField(blank=True, help_text='Описание производителя', max_length=200, null=True, verbose_name='Производитель')),
                ('modelComputer', models.CharField(blank=True, help_text='Введите название модели', max_length=200, null=True, verbose_name='модель')),
                ('serial', models.CharField(blank=True, help_text='Введите серийный номер', max_length=50, null=True)),
                ('serialImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='workstation/serial/')),
                ('invent', models.CharField(blank=True, help_text='Введите инвентаризационный номер', max_length=50, null=True)),
                ('inventImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='workstation/invent/')),
                ('CPU', models.TextField(blank=True, help_text='Описание CPU', max_length=200, null=True)),
                ('GPU', models.TextField(blank=True, help_text='Описание GPU', max_length=200, null=True)),
                ('RAM', models.TextField(blank=True, help_text='Описание RAM', max_length=200, null=True)),
                ('SSD', models.TextField(blank=True, help_text='Описание SSD', max_length=200, null=True)),
                ('HDD', models.TextField(blank=True, help_text='Описание HDD', max_length=200, null=True)),
                ('DCPower', models.TextField(blank=True, help_text='Описание блока питания', max_length=200, null=True, verbose_name='Блок питания')),
                ('keyBoard', models.TextField(blank=True, help_text='Описание клавиатуры', max_length=200, null=True, verbose_name='Клавиатура')),
                ('mouse', models.TextField(blank=True, help_text='Описание мыши', max_length=200, null=True, verbose_name='Мышь')),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.employee')),
                ('OS', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.os')),
                ('Workplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workplace')),
                ('monitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.monitor')),
                ('motherboard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.motherboard')),
            ],
            options={
                'verbose_name_plural': 'Рабочая станция',
                'ordering': ['Employee', 'name', 'Workplace'],
            },
        ),
        migrations.CreateModel(
            name='software',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='ВВедите название ПО', max_length=50)),
                ('manufacturer', models.CharField(blank=True, help_text='Описание производителя', max_length=200, null=True)),
                ('licenseKeyText', models.CharField(blank=True, help_text='Введите лицензтонный ключ', max_length=50, null=True)),
                ('licenseKeyImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='soft/')),
                ('licenseKeyFile', models.FileField(blank=True, help_text='прикрепите файл', null=True, upload_to='soft/')),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.employee')),
                ('workstation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workstation')),
            ],
            options={
                'verbose_name_plural': 'ПО',
                'ordering': ['Employee', 'name'],
            },
        ),
        migrations.CreateModel(
            name='printer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите название модели', max_length=50, verbose_name='Модель')),
                ('manufactured', models.CharField(blank=True, help_text='Введите название производителя', max_length=50, null=True, verbose_name='Производитель')),
                ('serial', models.CharField(blank=True, help_text='Введите серийный номер', max_length=50, null=True, verbose_name='Серийный номер')),
                ('serialImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='motherboard/soft/', verbose_name='Серийный номер')),
                ('invent', models.CharField(blank=True, help_text='Введите инвентаризационный номер', max_length=50, null=True, verbose_name='Инвентарный номер')),
                ('inventImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='workstation/invent/', verbose_name='Инвентарный номер')),
                ('USBPort', models.TextField(blank=True, help_text='Введите количество и тип', max_length=200, null=True, verbose_name='USB')),
                ('LANPort', models.TextField(blank=True, help_text='Введите количество', max_length=200, null=True, verbose_name='LAN')),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.employee', verbose_name='Сотрудник')),
                ('Workplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workplace', verbose_name='Рабочее место')),
                ('cartridge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cartridge', verbose_name='Картридж')),
                ('paper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.paper', verbose_name='Бумага')),
                ('workstation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workstation', verbose_name='Рабочая станция')),
            ],
            options={
                'verbose_name_plural': 'Принтер',
                'ordering': ['Employee', 'name'],
            },
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите должность', max_length=50)),
                ('departament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.departament')),
            ],
            options={
                'verbose_name_plural': 'Должность',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='Workplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workplace'),
        ),
        migrations.AddField(
            model_name='employee',
            name='departament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.departament', verbose_name='Отдел'),
        ),
        migrations.AddField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.post', verbose_name='Должность'),
        ),
        migrations.CreateModel(
            name='digitalSignature',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Введите номер ключа', max_length=50, null=True, verbose_name='Ключ')),
                ('licenseKeyText', models.CharField(blank=True, help_text='Введите лицензионный ключ', max_length=50, null=True)),
                ('licenseKeyImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='OS/')),
                ('licenseKeyFile', models.FileField(blank=True, help_text='прикрепите файл', null=True, upload_to='soft/')),
                ('validityPeriod', models.DateField(blank=True, null=True)),
                ('employeeEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.employee', verbose_name='Сотрудник')),
                ('Workplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workplace', verbose_name='Рабочее место')),
                ('workstation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.workstation', verbose_name='Рабочая станция')),
            ],
            options={
                'verbose_name_plural': 'ЭЦП',
                'ordering': ['validityPeriod'],
            },
        ),
    ]
