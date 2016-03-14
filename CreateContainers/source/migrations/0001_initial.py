# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name_container', models.CharField(max_length=50)),
                ('name_owner', models.CharField(max_length=50)),
                ('ssh_key', models.CharField(max_length=200)),
            ],
        ),
    ]
