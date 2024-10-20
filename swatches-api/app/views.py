from rest_framework import permissions, viewsets, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.request import *
from rest_framework import viewsets
import random

from app.models import ColourType
from app.serializers import ColourTypeSerializer, ColourRequestSerializer


class ColourTypesViewSet(viewsets.ModelViewSet):

    queryset = ColourType.objects.all()
    serializer_class = ColourTypeSerializer

    @action(detail=True)
    def generate_colours(self, request, *args, **kwargs):
      response_colours = []
      colour_type_pool = ["RGB", "HSL"]
      for count in range(5):
        colour_type = ColourType.objects.get(colour_type=colour_type_pool[random.randint(0,1)])
        response_colours.append(
          {'type': colour_type.colour_type, 
          colour_type.first_value: random.randint(1, colour_type.first_value_max),
          colour_type.second_value: random.randint(1, colour_type.second_value_max),
          colour_type.third_value: random.randint(1, colour_type.third_value_max)}
        )

      return Response(
        { 'colours': response_colours}
        , status=status.HTTP_200_OK)
