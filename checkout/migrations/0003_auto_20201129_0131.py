# Generated by Django 3.1.2 on 2020-11-29 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20201120_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=1.23, editable=False, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(default=6, max_length=50),
            preserve_default=False,
        ),
    ]