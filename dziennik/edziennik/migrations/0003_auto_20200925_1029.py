# Generated by Django 3.1.1 on 2020-09-25 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edziennik', '0002_osoba_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'permissions': (('per_u', 'per_n'),)},
        ),
    ]