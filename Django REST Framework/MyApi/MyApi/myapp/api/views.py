from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def firstFunction(request):
    # print(request.query_params['id'])
    # number = int(request.query_params['id']) * 5
    return Response({'message' : 'Request accepted'})