# Generated by Django 4.1 on 2023-01-12 12:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0011_remove_ups_accumulator1_remove_ups_accumulator2_and_more'),
        ('consumables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cassette',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите название модели', max_length=50, verbose_name='Модель')),
                ('serial', models.CharField(blank=True, help_text='Введите серийный номер', max_length=50, null=True, verbose_name='Серийный номер')),
                ('serialImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='gpu/serial/', verbose_name='Фото серийного номера')),
                ('invent', models.CharField(blank=True, help_text='Введите инвентарный номер', max_length=50, null=True, verbose_name='Инвентарный номер')),
                ('inventImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='gpu/invent/', verbose_name='Фото инвентарного номера')),
                ('power', models.CharField(blank=True, help_text='Укажите мощность', max_length=50, null=True, verbose_name='Мощность')),
                ('voltage', models.CharField(blank=True, help_text='Укажите напряжение', max_length=50, null=True, verbose_name='Напряжение')),
                ('current', models.CharField(blank=True, help_text='Укажите ток', max_length=50, null=True, verbose_name='Ток')),
                ('score', models.IntegerField(blank=True, help_text='Введите количество на складе', null=True, verbose_name='Остаток на складе')),
                ('accumulator1', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumables.accumulator', verbose_name='Аккумулятор № 1')),
                ('accumulator10', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 10')),
                ('accumulator2', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 2')),
                ('accumulator3', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 3')),
                ('accumulator4', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 4')),
                ('accumulator5', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 5')),
                ('accumulator6', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 6')),
                ('accumulator7', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 7')),
                ('accumulator8', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 8')),
                ('accumulator9', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 9')),
                ('manufacturer', models.ForeignKey(blank=True, help_text='Укажите производителя', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.manufacturer', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Кассета',
                'verbose_name_plural': 'Кассеты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ups',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите название модели', max_length=50, verbose_name='Модель')),
                ('serial', models.CharField(blank=True, help_text='Введите серийный номер', max_length=50, null=True, verbose_name='Серийный номер')),
                ('serialImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='gpu/serial/', verbose_name='Фото серийного номера')),
                ('invent', models.CharField(blank=True, help_text='Введите инвентарный номер', max_length=50, null=True, verbose_name='Инвентарный номер')),
                ('inventImg', models.ImageField(blank=True, help_text='прикрепите файл', null=True, upload_to='gpu/invent/', verbose_name='Фото инвентарного номера')),
                ('power', models.CharField(blank=True, help_text='Укажите мощность', max_length=50, null=True, verbose_name='Мощность')),
                ('voltage', models.CharField(blank=True, help_text='Укажите напряжение', max_length=50, null=True, verbose_name='Напряжение')),
                ('current', models.CharField(blank=True, help_text='Укажите ток', max_length=50, null=True, verbose_name='Ток')),
                ('score', models.IntegerField(blank=True, help_text='Введите количество на складе', null=True, verbose_name='Остаток на складе')),
                ('accumulator1', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumables.accumulator', verbose_name='Аккумулятор № 1')),
                ('accumulator2', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 2')),
                ('accumulator3', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 3')),
                ('accumulator4', models.ForeignKey(blank=True, help_text='Укажите аккумулятор', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='consumables.accumulator', verbose_name='Аккумулятор № 4')),
                ('cassette1', models.ForeignKey(blank=True, help_text='Укажите кассету', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ups.cassette', verbose_name='Кассета № 1')),
                ('cassette2', models.ForeignKey(blank=True, help_text='Укажите кассету', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ups.cassette', verbose_name='Кассета № 2')),
                ('cassette3', models.ForeignKey(blank=True, help_text='Укажите кассету', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ups.cassette', verbose_name='Кассета № 3')),
                ('cassette4', models.ForeignKey(blank=True, help_text='Укажите кассету', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ups.cassette', verbose_name='Кассета № 4')),
                ('manufacturer', models.ForeignKey(blank=True, help_text='Укажите производителя', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.manufacturer', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'ИБП',
                'verbose_name_plural': 'ИБП',
                'ordering': ['name'],
            },
        ),
    ]