from django.db import models

# Create your models here.
from Student.models import Student


# class of survey
class Survey(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='surveys')
    name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    due_date = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# class of Question

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    body = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.body


# class of Answers

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)

    def __str__(self):
        return self.text


# table of taken surveys
class TakenSurvey(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_survey')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='taken_survey')
    is_complete = models.BooleanField(default=False)
    answers = models.TextField(Question.objects.id, Answer.objects.text)


# class to count the Answered questions

class CountAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')
