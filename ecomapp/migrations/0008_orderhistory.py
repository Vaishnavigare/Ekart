# Generated by Django 4.2 on 2023-05-29 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecomapp', '0007_alter_order_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=200, verbose_name='Order ID')),
                ('pay_id', models.CharField(max_length=200, verbose_name='Payment ID')),
                ('sign', models.CharField(max_length=200, verbose_name='Signature')),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
