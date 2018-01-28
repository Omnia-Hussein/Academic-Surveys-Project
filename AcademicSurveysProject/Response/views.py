from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from .models import Response


class ResponseList(ListView):
    model = Response


class ResponseAnswerCreate(CreateView):
    template_name = 'Survey/survey_form.html'
    model = Survey
    fields = []

    def get_context_data(self, **kwargs):
        context = super(SurveyQuestionCreate, self).get_context_data(**kwargs)
        context['questions'] = QuestionFormSet(self.request.POST or None)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        questions = context['questions']
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.professor_id = self.request.user.id
            self.object.save()
            if questions.is_valid():
                questions.instance = self.object
                questions.save()
        return super(SurveyQuestionCreate, self).form_valid(form)


# class ResponseAnswerUpdate(UpdateView):
#     template_name = 'Response/response_form.html'
#     model = Survey
#     fields = ['name', 'description', 'due_date', 'is_active', ]
#     success_url = reverse_lazy('survey:list')
#
#     def get_context_data(self, **kwargs):
#         context = super(SurveyQuestionUpdate, self).get_context_data(**kwargs)
#         context['questions'] = QuestionFormSet(self.request.POST or None, instance=self.object)
#         return context
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         questions = context['questions']
#         with transaction.atomic():
#             self.object = form.save()
#             self.object.save()
#             if questions.is_valid():
#                 questions.instance = self.object
#                 questions.save()
#         return super(SurveyQuestionUpdate, self).form_valid(form)
