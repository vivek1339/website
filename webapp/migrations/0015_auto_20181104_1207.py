# Generated by Django 2.1 on 2018-11-04 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.buyer')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('pid', 'bid')},
        ),
    ]