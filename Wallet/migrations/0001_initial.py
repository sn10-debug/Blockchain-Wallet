# Generated by Django 4.0.3 on 2022-05-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Password', models.CharField(default='', max_length=8)),
                ('Common_Public_Key', models.CharField(default='', max_length=64)),
                ('Network_Public_keys', models.JSONField(default={'Solana': 'cbe46c8697f2ed0954c0b66d047ac73a387e8e0e6adbf9ea6ccacf6396d8cf9d'})),
            ],
        ),
    ]