# Generated by Django 3.1.14 on 2022-10-25 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Русское имя')),
                ('name_en', models.CharField(max_length=25, unique=True, verbose_name='Английское имя')),
                ('name_jp', models.CharField(max_length=25, unique=True, verbose_name='Японское имя')),
                ('image', models.ImageField(blank=True, unique=True, upload_to='', verbose_name='Картинка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('progenitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progenitors', to='pokemon_entities.pokemon', verbose_name='Предшественник')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('low', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(null=True, verbose_name='Время включения')),
                ('disappeared_at', models.DateTimeField(null=True, verbose_name='Время отключения')),
                ('level', models.IntegerField(null=True, verbose_name='Уровень')),
                ('health', models.IntegerField(null=True, verbose_name='Здоровье')),
                ('strength', models.IntegerField(null=True, verbose_name='Прочность')),
                ('defencer', models.IntegerField(null=True, verbose_name='Защита')),
                ('stamina', models.IntegerField(null=True, verbose_name='стамина')),
                ('pokemon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemons', to='pokemon_entities.pokemon', verbose_name='Покемон')),
            ],
        ),
    ]
