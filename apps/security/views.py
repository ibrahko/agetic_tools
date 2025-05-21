from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def test_post(request):
    return Response({'message': 'Requête POST acceptée !'})
