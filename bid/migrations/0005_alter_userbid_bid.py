# Generated by Django 3.2.5 on 2021-08-09 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0001_initial'),
        ('bid', '0004_userbid_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbid',
            name='bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_login.bids', verbose_name='bid'),
        ),
    ]
