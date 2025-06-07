from django.contrib.auth.models import User

from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,style={'input_type': 'password'})
    first_name = serializers.CharField(max_length=30, )
    last_name = serializers.CharField(max_length=30,)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name','password2']

    extra_kwargs = {
        'password': {'write_only': True, 'style': {'input_type': 'password'}},  
    }
    
    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        user.set_password(password)
        user.save()
        return user