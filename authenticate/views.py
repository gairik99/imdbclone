from .models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def get_movies(request):
    if request.method == 'GET':
        movies=Movie.objects.all()
        # data={'movies':list(movies.values())}
        # return JsonResponse(data)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','PUT','DELETE'])
def get_movie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            # movie = Movie.objects.get(id=movie_id)
            # data = {
            #     'title': movie.title,
            #     'description': movie.description,
            #     'release_date': movie.release_date,
            #     'rating': movie.rating,
            #     'gross_revenue': movie.gross_revenue,
            #     'movie_id': movie.id
            # }
            serializer = MovieSerializer(movie)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        try:
            # movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)                                                    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Movie.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        try:
            # movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)