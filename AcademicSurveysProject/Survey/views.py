from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from .forms import SurveyForm, QuestionForm
from extra_views import CreateWithInlinesView
from .models import Survey
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib import messages
from Question.forms import QuestionFormSet
from braces.views import MultiplePermissionsRequiredMixin


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
