from django.forms import ModelForm, inlineformset_factory

from Question.models import Question
from Survey.models import Survey
from Template.models import Template


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['order', 'body', 'type', 'required', 'choices', 'survey', ]


QuestionSurveyFormSet = inlineformset_factory(Survey, Question, form=QuestionForm, extra=1, can_delete=True)
QuestionTemplateFormSet = inlineformset_factory(Template, Question, form=QuestionForm, extra=1, can_delete=True)
