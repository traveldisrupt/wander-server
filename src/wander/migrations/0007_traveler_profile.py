# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wander', '0006_auto_20160911_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveler',
            name='profile',
            field=models.URLField(default='https://scontent-sjc2-1.xx.fbcdn.net/v/t1.0-9/12688174_10207842733043301_2986078780578216664_n.jpg?oh=8c537cad4e8cb989e42a718cdea69eb2&oe=58481E5B'),
        ),
    ]