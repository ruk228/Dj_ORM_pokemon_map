# Generated by Django 3.1.14 on 2022-11-04 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20221101_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name_en',
            field=models.CharField(max_length=25, verbose_name='Английское имя'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_jp',
            field=models.CharField(max_length=25, verbose_name='Японское имя'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemons', to='pokemon_entities.pokemon', unique=True, verbose_name='Покемон'),
        ),
    ]
