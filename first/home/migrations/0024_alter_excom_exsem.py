# Generated by Django 5.0.1 on 2024-02-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_excom_exsem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excom',
            name='exsem',
            field=models.CharField(max_length=20),
        ),
    ]