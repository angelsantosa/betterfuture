# Generated by Django 2.1.3 on 2018-11-11 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tokens', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user_footprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserFootPrint'),
        ),
        migrations.AddField(
            model_name='tokentransactions',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokens.Transaction'),
        ),
    ]