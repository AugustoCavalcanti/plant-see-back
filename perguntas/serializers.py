from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Question, Choice, Answer

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    alternativas = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'img_url', 'alternativas']

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Answer
        fields = ['acertos', 'choices']