# Generated by Django 2.1 on 2018-11-08 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0037_cart_sid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('bid', 'pid', 'sid', 'created_at')},
        ),
    ]
