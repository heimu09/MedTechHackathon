# Generated by Django 4.0.6 on 2022-12-03 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_mother_children_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='mother',
            name='age',
            field=models.IntegerField(default=18, verbose_name='Возраст'),
        ),
    ]
