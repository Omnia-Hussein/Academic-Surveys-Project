from django.db import models
from Professor.models import Professor
from EducationalYear.models import EducationalYear
from Course.models import Course


class Survey(models.Model):
    name = models.CharField(
        max_length=400,
    )
    description = models.TextField(
        max_length=4000,
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
    )
    due_date = models.DateTimeField()
    is_active = models.BooleanField(
        default=True,
    )
    professor = models.ForeignKey(
        Professor,
        related_name='surveys',
    )
    educational_year = models.ForeignKey(
        EducationalYear,
        related_name='surveys',
    )
    course = models.ForeignKey(
        Course,
        related_name='surveys',
    )

    def __str__(self):
        return self.name

#
# # class of Question
#
# class Question(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
#     body = models.CharField('Question', max_length=255)
#
#     def __str__(self):
#         return self.body
#
#
# # class of Answers
#
# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
#     text = models.CharField('Answer', max_length=255)
#
#     def __str__(self):
#         return self.text
#
#
# # table of taken surveys
# class TakenSurvey(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_survey')
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='taken_survey')
#     is_complete = models.BooleanField(default=False)
#     answers = models.TextField(Question.objects.id, Answer.objects.text)
#
#
# # class to count the Answered questions
#
# class CountAnswer(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')
