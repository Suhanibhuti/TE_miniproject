# Generated by Django 5.0.1 on 2024-01-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_pdm_mn_alter_pdm_mn1_alter_pdm_mn2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='attM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=122)),
                ('percentage', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=122)),
            ],
        ),
    ]
