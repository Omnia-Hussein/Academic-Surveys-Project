from django.forms import ModelForm, inlineformset_factory

from Question.models import Question
from Survey.models import Survey


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['order', 'body', 'type', 'required', 'choices', 'survey', ]


QuestionFormSet = inlineformset_factory(Survey, Question, form=QuestionForm, extra=1, can_delete=True)
