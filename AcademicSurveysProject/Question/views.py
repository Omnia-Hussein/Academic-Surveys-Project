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
