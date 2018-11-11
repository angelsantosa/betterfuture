# Generated by Django 2.1.3 on 2018-11-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0002_auto_20181111_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='eth_per_token',
            field=models.FloatField(verbose_name='ETH per Token'),
        ),
        migrations.AlterField(
            model_name='tokentransactions',
            name='eth',
            field=models.FloatField(verbose_name='Sent ETH'),
        ),
        migrations.AlterField(
            model_name='tokentransactions',
            name='gas',
            field=models.FloatField(verbose_name='Gas'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tokens_value',
            field=models.FloatField(verbose_name='Tokens'),
        ),
    ]