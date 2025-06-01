from .models import WatchList,StreamingService, Review 
# from django.http import JsonResponse
from .serializers import WatchListSerializer,StreamingServiceSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics



# Create your views here.
# class ReviewDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
      queryset = Review.objects.all()
      serializer_class = ReviewSerializer


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


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
def get_watchlist(request, watchlist_id):
    try:
        watchlist = WatchList.objects.get(id=watchlist_id)
    except WatchList.DoesNotExist:
        return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
  
            # WatchList = WatchList.objects.get(id=WatchList_id)
            # data = {
            #     'title': WatchList.title,
            #     'description': WatchList.description,
            #     'release_date': WatchList.release_date,
            #     'rating': WatchList.rating,
            #     'gross_revenue': WatchList.gross_revenue,
            #     'WatchList_id': WatchList.id
            # }
            serializer = WatchListSerializer(watchlist)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    if request.method == 'PUT':
     
            # WatchList = WatchList.objects.get(id=WatchList_id)
            serializer = WatchListSerializer(watchlist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)                                                    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    if request.method == 'DELETE':
            # WatchList = WatchList.objects.get(id=WatchList_id)
            watchlist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      
        

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
     