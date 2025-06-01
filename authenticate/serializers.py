from rest_framework import serializers
from .models import WatchList,StreamingService, Review

# class WatchListSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField()
#     rating = serializers.DecimalField(max_digits=3, decimal_places=1)
#     gross_revenue = serializers.DecimalField(max_digits=15, decimal_places=2)

#     def create(self, value):
#         """
#         Create and return a new `WatchList` instance, given the validated data.
#         """
#         return WatchList.objects.create(**value)
#     def update(self, instance, value):
#         """
#         Update and return an existing `WatchList` instance, given the validated data.
#         """

#         instance.title = value.get('title', instance.title)
#         instance.description = value.get('description', instance.description)
#         instance.rating = value.get('rating', instance.rating)
#         instance.gross_revenue = value.get('gross_revenue', instance.gross_revenue)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         """
#         Check that the rating is between 0 and 10.
#         """
#         if data['rating'] < 0 or data['rating'] > 10:
#             raise serializers.ValidationError("Rating must be between 0 and 10.")
#         return data
    
#     def validate_title(self, value):
#         """
#         Validate the length of a string field.
#         """
#         if len(value) < 4:
#             raise serializers.ValidationError("title must be at least 4 character long.")
#         return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id']

class WatchListSerializer(serializers.ModelSerializer):
    # length=serializers.SerializerMethodField()
    # def get_length(self, obj):
    #     return len(obj.title) 
    reviews= ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        # fields = [ 'id','title', 'description','rating', 'gross_revenue']
        # exclude = [ 'id',]
        fields= '__all__'
        read_only_fields = ['id']
    
#     def validate(self, data):
# #         """
# #         Check that the rating is between 0 and 10.
# #         """
#         if data['rating'] < 0 or data['rating'] > 10:
#             raise serializers.ValidationError("Rating must be between 0 and 10.")
#         return data
    
#     def validate_title(self, value):
#         if len(value) < 4:
#             raise serializers.ValidationError("Title must be at least 4 characters long.")
#         return value


class StreamingServiceSerializer(serializers.ModelSerializer):
    watchlists = WatchListSerializer(many=True, read_only=True)
    # watchlists=serializers.StringRelatedField(
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = StreamingService
        fields = '__all__'
        read_only_fields = ['id']
    
    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name must be at least 3 characters long.")
    #     return value