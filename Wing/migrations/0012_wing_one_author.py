# Generated by Django 5.1.1 on 2024-10-03 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wing', '0011_alter_wing_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='wing_one',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Wing.wing'),
        ),
    ]
