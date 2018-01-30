from django.forms import ModelForm, inlineformset_factory, modelformset_factory, TextInput

from .models import Answer, Response


class AnswerForm(ModelForm):

    class Meta:
        model = Answer
        fields = ['body', ]
        widgets = {
            'body': TextInput(),
        }


AnswerFormSet = inlineformset_factory(Response, Answer, form=AnswerForm, can_delete=False)
AnswerFormSetUpdate = modelformset_factory(Answer, form=AnswerForm, can_delete=False)
