# Generated by Django 4.0.6 on 2022-12-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_mother_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mother',
            name='age',
        ),
        migrations.AddField(
            model_name='mother',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Возраст'),
        ),
    ]
