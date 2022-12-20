from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer


@api_view(['GET'])
def player_list(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

# def player_list(request):
#     players = Player.objects.all().order_by('id')
#     serializer = PlayerSerializer(players, many=True)
#     resp = Response(serializer.data)
#     resp['Access-Control-Allow-Origin'] = '*'
#     resp['Access-Control-Allow-Headers'] = '*'
#     resp['Access-Control-Allow-Methods'] = '*'
#     return resp

@api_view(['GET'])
def player_detail(request, id):
    player = Player.objects.get(id=id)
    serializer = PlayerSerializer(player, many=False)
    return Response(serializer.data)
