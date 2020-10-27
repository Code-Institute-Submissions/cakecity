# Generated by Django 3.1.2 on 2020-10-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20201026_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(choices=[('Drip Cake Collection', 'Drip Cake Collection'), ('Birthday Cakes', 'Birthday Cakes'), ('Kids Birthday Cakes', 'Kids Birthday Cakes'), ('Christening Cakes', 'Christening Cakes'), ('Communion and Confirmation Cakes', 'Communion and Confirmation Cakes'), ('Anniversary and Occasional Cakes', 'Anniversary and Occasional Cakes'), ('Novelty Cupcakes', 'Novelty Cupcakes'), ('The Buttercream Collection', 'The Buttercream Collection'), ('Wedding Cake Tables and Wedding Cupcake Dispalys', 'Wedding Cake Tables and Wedding Cupcake Dispalys'), ('Novelty Style Wedding Cakes and Wedding Cakes with Cake Toppers', 'Novelty Style Wedding Cakes and Wedding Cakes with Cake Toppers'), ('Classic Wedding Cakes', 'Classic Wedding Cakes'), ('Elegance and Simplicity', 'Elegance and Simplicity'), ('Vintage Romantic Wedding Cakes', 'Vintage Romantic Wedding Cakes'), ('Corporate Cakes', 'Corporate Cakes'), ('Branded Cupcakes', 'Branded Cupcakes')], default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cakecategory',
            name='category',
            field=models.CharField(choices=[('0', 'Uncategorized'), ('novelty-cakes', 'Novelty Cakes'), ('wedding-cakes', 'Wedding Cakes'), ('corporate-cakes', 'Corporate Cakes')], default='0', max_length=120),
        ),
        migrations.AlterField(
            model_name='cakecategory',
            name='category_slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
