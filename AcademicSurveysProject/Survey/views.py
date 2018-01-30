from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from Question.forms import QuestionFormSet
from .models import Survey


# class SurveyCreate(CreateWithInlinesView):
#     model = Survey
#     fields = ['name', 'description', 'due_date', 'educational_year', 'course']
#     context_object_name = 'survey'
#     inlines = [QuestionSurveyInline,]
#     template_name = 'Survey/survey_form.html'
#
#     # def get_success_url(self):
#     #     return '/inlines/%i' % self.object.pk

# class SurveyCreate(CreateView):
#     model = Survey
#     fields = ('name', 'description', 'due_date', 'is_active', 'educational_year', 'course')
#     template_name = 'Survey/survey_form.html'
#
#     def form_valid(self, form):
#         survey = form.save(commit=False)
#         survey.professor = self.request.user
#         survey.save()
#         messages.success(self.request, 'The survey was created with success! Go ahead and add some questions now.')
#         return redirect('/')
#         # return redirect('survey:change', survey.pk)


class SurveyList(ListView):
    model = Survey


class SurveyQuestionCreate(CreateView):
    template_name = 'Survey/survey_form.html'
    model = Survey
    fields = ['name', 'description', 'due_date', 'is_active', 'course', 'educational_year', ]

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

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     questions = context['questions']
    #     with transaction.atomic():
    #         self.object = form.save()
    #         if questions.is_valid():
    #             questions.instance = self.object
    #             questions.save()
    #         else:
    #             return self.form_invalid(form)
    #     return super(SurveyQuestionCreate, self).form_valid(form)
    #
    # def form_invalid(self, form):
    #     questions = QuestionFormSet(self.request.POST or None)
    #     return self.render_to_response(self.get_context_data(form=form, questions=questions))


class SurveyQuestionUpdate(UpdateView):
    template_name = 'Survey/survey_form.html'
    model = Survey
    fields = ['name', 'description', 'due_date', 'is_active', ]
    success_url = reverse_lazy('survey:list')

    def get_context_data(self, **kwargs):
        context = super(SurveyQuestionUpdate, self).get_context_data(**kwargs)
        context['questions'] = QuestionFormSet(self.request.POST or None, instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        questions = context['questions']
        with transaction.atomic():
            self.object = form.save()
            self.object.save()
            if questions.is_valid():
                questions.instance = self.object
                questions.save()
        return super(SurveyQuestionUpdate, self).form_valid(form)


class SurveyRead(View):
    def get(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey, pk=kwargs['pk'])
        questions = survey.questions.all()
        answers = []
        for question in questions:
            temp = []
            for i in range(6):
                temp += [question.answers.filter(body=str(i)).count()]
            answers += [temp]
        context = {
            'survey': survey,
            'questions': questions,
            'answers': answers,
        }
        return render(request, 'Survey/survey_read.html', context)
