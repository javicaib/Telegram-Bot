# Generated by Django 4.1.1 on 2022-09-09 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_game_mesureunit_plataform_delete_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesureunit',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='plataform',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
