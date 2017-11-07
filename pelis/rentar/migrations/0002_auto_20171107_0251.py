# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alquiler',
            old_name='actor',
            new_name='usuario',
        ),
    ]
