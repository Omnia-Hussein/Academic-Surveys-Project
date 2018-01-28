from django.forms import ModelForm, inlineformset_factory
from extra_views import InlineFormSet
from .models import Question, Survey

# class QuestionSurveyInline(InlineFormSet):
#     model = Question
#     fields = ['order', 'body', 'type', 'required', 'choices', 'survey']
#     # formset_class = BaseTableFormSet
#
#
# class QuestionTemplateInline(InlineFormSet):
#     model = Question
#     fields = ['order', 'body', 'type', 'required', 'choices', 'template']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['order', 'body', 'type', 'required', 'choices', 'survey']


QuestionFormSet = inlineformset_factory(Survey, Question, form=QuestionForm, extra=1, can_delete=True)
