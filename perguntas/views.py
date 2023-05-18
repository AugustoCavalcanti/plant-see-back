from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Choice, Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]


@permission_classes((permissions.AllowAny,))
class QuestionRegister(APIView):

    def post(self, request, format=None):
        dados = request.data
        ids = []
        total_acertos = 0
        for x in dados:
            ids.append(dados[x])

        alternativas = Choice.objects.filter(id__in=ids)

        for alternativa in alternativas:
            if alternativa.correct:
                total_acertos += 1

        porcentagem = round((Answer.objects.filter(acertos__lt=total_acertos).count() * 100) / Answer.objects.count())
        resposta = Answer(acertos=total_acertos, porcentagem=porcentagem)
        resposta.save()
        resposta.choices.set(alternativas)

        return JsonResponse({'resposta': resposta.id}, status=status.HTTP_201_CREATED)
 

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def answer_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        answer = Answer.objects.get(pk=pk)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)