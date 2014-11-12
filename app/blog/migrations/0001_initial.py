# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True, null=True)),
                ('pub_date', models.DateTimeField()),
                ('excerpt', models.TextField(null=True)),
                ('text', models.TextField()),
                ('header_image', models.FileField(null=True, upload_to=b'blog/%Y/%m/%d', blank=True)),
                ('post_color', models.CharField(max_length=20, null=True)),
                ('tags', models.CharField(max_length=80, blank=True)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
