# Generated by Django 3.1.1 on 2020-09-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edziennik', '0015_auto_20200926_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocena',
            name='opis',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]