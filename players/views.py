from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer


def redirectView(request):
    return redirect(player_list)


@api_view(['GET'])
def player_list(request):
    players = Player.objects.all().order_by('id')
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def player_detail(request, id):
    player = Player.objects.get(id=id)
    serializer = PlayerSerializer(player, many=False)
    return Response(serializer.data)
