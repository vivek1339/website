# Generated by Django 2.1 on 2018-11-08 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0036_auto_20181108_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.seller'),
            preserve_default=False,
        ),
    ]
