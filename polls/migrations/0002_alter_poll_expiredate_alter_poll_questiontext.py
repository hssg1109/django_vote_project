# Generated by Django 5.0.3 on 2024-04-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='expireDate',
            field=models.DateField(blank=True, db_column='expireDate', null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='questionText',
            field=models.CharField(blank=True, db_column='questionText', max_length=200),
        ),
    ]
