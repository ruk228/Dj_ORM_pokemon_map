from email.base64mime import header_length
from django.db import models
from django.forms.models import model_to_dict
from django.utils.timezone import localtime


class Pokemon(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='Русское имя')
    name_en = models.CharField(blank=True, max_length=25, verbose_name='Английское имя')
    name_jp = models.CharField(blank=True, max_length=25, verbose_name='Японское имя')
    image = models.ImageField(blank=True, unique=True, verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Описание')
    progenitor = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Предшественник', related_name='next_evolutions')

    def __str__(self):
        return self.name


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, null=True, on_delete=models.CASCADE, related_name='entities', verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    low = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(null=True, verbose_name='Время включения')
    disappeared_at = models.DateTimeField(null=True, verbose_name='Время отключения')
    level = models.IntegerField(null=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, verbose_name='Прочность')
    defencer = models.IntegerField(null=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, verbose_name='стамина')

    def __str__(self):
        return str(self.pokemon)
