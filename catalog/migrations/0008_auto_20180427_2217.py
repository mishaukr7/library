# Generated by Django 2.0.4 on 2018-04-27 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20180426_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Country'),
        ),
    ]
