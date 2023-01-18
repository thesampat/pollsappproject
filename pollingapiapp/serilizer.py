from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers


class QuestionSerilizers(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['QUser']

class VoteSerilizer(ModelSerializer):
    
    class Meta:
         model = Vote
         fields= ['VQuestion','Result', 'User']
         read_only_fields = ['User']


    def validate(self, data):
        return super().validate(data)


class UserSerilizer(ModelSerializer):
    question_by = QuestionSerilizers(many=True, read_only=True)
    voted_by = VoteSerilizer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'


    def validate(self, data):
        if len(str(data['Phone'])) < 10:
            raise serializers.ValidationError('Phone number must be of 10 Digits')
        return data
    
