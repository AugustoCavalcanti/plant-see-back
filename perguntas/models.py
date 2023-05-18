from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    img_url = models.URLField(max_length=300, blank=True, null=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='alternativas', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return '%d: %s' % (self.id, self.choice_text)
    

class Answer(models.Model):
    acertos = models.IntegerField(null=False, blank=False)
    choices = models.ManyToManyField(Choice)
    porcentagem = models.FloatField(null=True, blank=True)