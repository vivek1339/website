# Generated by Django 2.1 on 2018-11-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0040_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='name_on_card',
        ),
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
