from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            # token, _ = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            # return Response({"message": "User created successfully","data":serializer.data,"token":token.key}, status=status.HTTP_201_CREATED)
            return Response({"message": "User created successfully","data":serializer.data,"refresh":str(refresh),"access":str(refresh.access_token),}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = RegisterSerializer()
# @api_view(['POST'])
# def logout(request):
#     if request.method == 'POST':
#         try:
#             request.user.auth_token.delete()
#             return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
#         except (AttributeError, Token.DoesNotExist):
#             return Response({"error": "User is not authenticated"}, status=status.HTTP_400_BAD_REQUEST)

    