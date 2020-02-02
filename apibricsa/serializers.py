from rest_framework import serializers

from .models import Hero
from .models import Banners
from .models import Inmuebles

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class BannersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Banners
        fields = ('title', 'description')

class InmueblesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inmuebles
        fields = ('name', 'description')