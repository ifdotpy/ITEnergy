# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0009_deliveryorder_date_ordered'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Элемент корзины', 'verbose_name_plural': 'Элементы корзины'},
        ),
        migrations.AddField(
            model_name='item',
            name='total_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Общая сумма'),
            preserve_default=False,
        ),
    ]