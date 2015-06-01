# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='db',
            name='language',
            field=models.CharField(default='unknown', max_length=50, choices=[(b'C', b'C'), (b'C++', b'C++'), (b'Python', b'Python'), (b'Ruby', b'Ruby'), (b'Java', b'Java')]),
            preserve_default=False,
        ),
    ]
