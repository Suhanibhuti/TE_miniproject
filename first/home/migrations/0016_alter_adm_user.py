# Generated by Django 5.0.1 on 2024-02-25 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_adm_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adm',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pdm'),
        ),
    ]
