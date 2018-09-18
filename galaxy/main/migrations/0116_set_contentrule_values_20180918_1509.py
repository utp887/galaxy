# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 22:01
from __future__ import unicode_literals

from django.db import migrations


def set_initial_rule_severity(apps, schema_editor):
    LINTER_RULE_SEVERITY = [
        ('ansible-lint', 'E101', 3),
        ('ansible-lint', 'E102', 4),
        ('ansible-lint', 'E103', 5),
        ('ansible-lint', 'E104', 5),
        ('ansible-lint', 'E105GAL', 0),
        ('ansible-lint', 'E106GAL', 0),
        ('ansible-lint', 'E201', 0),
        ('ansible-lint', 'E202', 5),
        ('ansible-lint', 'E203GAL', 2),
        ('ansible-lint', 'E204GAL', 1),
        ('ansible-lint', 'E205GAL', 1),
        ('ansible-lint', 'E206GAL', 3),
        ('ansible-lint', 'E207GAL', 3),
        ('ansible-lint', 'E208GAL', 2),
        ('ansible-lint', 'E301', 4),
        ('ansible-lint', 'E302', 5),
        ('ansible-lint', 'E303', 4),
        ('ansible-lint', 'E304', 5),
        ('ansible-lint', 'E305', 4),
        ('ansible-lint', 'E306GAL', 0),
        ('ansible-lint', 'E401', 3),
        ('ansible-lint', 'E402', 3),
        ('ansible-lint', 'E403', 1),
        ('ansible-lint', 'E404GAL', 4),
        ('ansible-lint', 'E405GAL', 3),
        ('ansible-lint', 'E406GAL', 0),
        ('ansible-lint', 'E501', 5),
        ('ansible-lint', 'E502', 3),
        ('ansible-lint', 'E503', 3),
        ('ansible-lint', 'E504GAL', 3),
        ('ansible-lint', 'E601GAL', 4),
        ('ansible-lint', 'E602GAL', 4),
        ('yamllint', 'error', 0),
        ('yamllint', 'warning', 0),
    ]
    ContentRule = apps.get_model('main', 'ContentRule')
    for linter, rule, severity in LINTER_RULE_SEVERITY:
        c = ContentRule(
            linter_id=linter,
            rule_id=rule,
            severity=severity,
        )
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0115_content_scoring_20180918_1506'),
    ]

    operations = [
        migrations.RunPython(set_initial_rule_severity),
    ]
