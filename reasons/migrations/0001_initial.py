# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-15 11:00
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, verbose_name='Number')),
                ('name', models.CharField(blank=True, max_length=80, null=True, verbose_name='Reason name')),
                ('nameFontSize', models.IntegerField(blank=True, default=173, null=True, verbose_name='Font Size')),
                ('nameLetterSpacing', models.IntegerField(blank=True, default=34, null=True, verbose_name='Letter Spacing')),
                ('linkText', models.CharField(blank=True, default='Read more', max_length=80, null=True, verbose_name='Link text')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='reasons', verbose_name='Banner image')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Reason description')),
            ],
            options={
                'ordering': ['number'],
                'verbose_name_plural': 'Reasons',
                'verbose_name': 'Reason',
            },
        ),
    ]