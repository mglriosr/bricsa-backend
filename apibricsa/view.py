from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero
from .serializers import BannersSerializer
from .models import Banners
from .serializers import InmueblesSerializer
from .models import Inmuebles


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class BannersViewSet(viewsets.ModelViewSet):
  queryset = Banners.objects.all().order_by('title')
  serializer_class = HeroSerializer

class InmueblesViewSet(viewsets.ModelViewSet):
  queryset = Inmuebles.objects.all().order_by('name')
