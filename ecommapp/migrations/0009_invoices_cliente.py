# Generated by Django 3.1.1 on 2020-09-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0008_auto_20200922_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='cliente',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
