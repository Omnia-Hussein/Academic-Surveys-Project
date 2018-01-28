# from django import forms
# from .models import Survey, Question, Answer
#
#
# class SurveyForm(forms.ModelForm):
#     class Meta:
#         model = Survey
#         fields = (
#             'owner',
#             'due_date',
#             'creator',
#             'recipient',
#             'name',
#         )
#
#
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ('survey', 'body',)
#
#
# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ('queston', 'text',)
