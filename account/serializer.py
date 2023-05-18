from .models import User,Author
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password_2=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','password','password_2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self,attrs):
        password=attrs.get('password')
        password_2=attrs.get('password_2')
        if password_2!=password:
            raise serializers.ValidationError('пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user=User(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        try:
            author=Author.objects.create(
                user=user
            )
        except Exception as e:
            user.delete()
            raise e
        else:
            author.username=user.username
        return author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Author
        fields="__all__"

