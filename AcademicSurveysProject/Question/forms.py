from django.forms import ModelForm, inlineformset_factory

from Question.models import Question
from Survey.models import Survey
from Template.models import Template


class QuestionSurveyForm(ModelForm):
    class Meta:
        model = Question
        fields = ['order', 'body', 'type', 'required', 'choices', 'survey', ]


class QuestionTemplateForm(ModelForm):
    class Meta:
        model = Question
        fields = ['order', 'body', 'type', 'required', 'choices', 'template', ]


QuestionSurveyFormSet = inlineformset_factory(Survey, Question, form=QuestionSurveyForm, extra=1, can_delete=True,
                                              min_num=1)
QuestionTemplateFormSet = inlineformset_factory(Template, Question, form=QuestionTemplateForm, extra=1, can_delete=True,
                                                min_num=1)
