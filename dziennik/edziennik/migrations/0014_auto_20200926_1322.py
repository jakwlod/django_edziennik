# Generated by Django 3.1.1 on 2020-09-26 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edziennik', '0013_plan_przedmiot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocena',
            name='id_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='edziennik.plan'),
        ),
    ]
