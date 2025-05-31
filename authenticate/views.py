from .models import WatchList,StreamingService 
# from django.http import JsonResponse
from .serializers import WatchListSerializer,StreamingServiceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def get_watchlists(request):
    if request.method == 'GET':
        WatchLists=WatchList.objects.all()
        # data={'WatchLists':list(WatchLists.values())}
        # return JsonResponse(data)
        serializer = WatchListSerializer(WatchLists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


@api_view(['GET','PUT','DELETE'])
def get_watchlist(request, watchList_id):
    try:
        WatchList = WatchList.objects.get(id=watchList_id)
    except WatchList.DoesNotExist:
        return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            # WatchList = WatchList.objects.get(id=WatchList_id)
            # data = {
            #     'title': WatchList.title,
            #     'description': WatchList.description,
            #     'release_date': WatchList.release_date,
            #     'rating': WatchList.rating,
            #     'gross_revenue': WatchList.gross_revenue,
            #     'WatchList_id': WatchList.id
            # }
            serializer = WatchListSerializer(WatchList)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except WatchList.DoesNotExist:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        try:
            # WatchList = WatchList.objects.get(id=WatchList_id)
            serializer = WatchListSerializer(WatchList, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)                                                    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchList.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        try:
            # WatchList = WatchList.objects.get(id=WatchList_id)
            WatchList.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET','POST'])
def get_streaming_services(request):
    if request.method == 'GET':
        try:
            streaming_services = StreamingService.objects.all()
            serializer = StreamingServiceSerializer(streaming_services, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StreamingService.DoesNotExist:
            return Response({'error': 'Streaming services not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = StreamingServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def get_streaming_service(request, streaming_service_id):
    try:
        streaming_service = StreamingService.objects.get(id=streaming_service_id)
    except StreamingService.DoesNotExist:
        return Response({'error': 'Streaming service not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StreamingServiceSerializer(streaming_service)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = StreamingServiceSerializer(streaming_service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        streaming_service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#     return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
     