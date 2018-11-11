# Generated by Django 2.1.3 on 2018-11-11 06:21

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eth_address', models.CharField(max_length=42, verbose_name='Core ETH address')),
                ('eth_per_token', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='ETH per Token')),
            ],
        ),
        migrations.CreateModel(
            name='TokenTransactions',
            fields=[
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('address_from', models.CharField(blank=True, max_length=42, verbose_name='ETH address FROM')),
                ('address_to', models.CharField(blank=True, max_length=42, verbose_name='ETH address TO')),
                ('contract', models.CharField(blank=True, max_length=42, verbose_name='Contract address')),
                ('gas', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Gas')),
                ('eth', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Sent ETH')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('tokens_value', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Tokens')),
            ],
        ),
    ]