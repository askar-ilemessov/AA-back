# Generated by Django 4.0 on 2021-12-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='cat',
            field=models.TextField(choices=[('Toys', 'Toys')], max_length=100, null=True),
        ),
    ]