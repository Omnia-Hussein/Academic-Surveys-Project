import datetime

from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from Course.models import Course
from EducationalYear.models import EducationalYear
from Question.forms import QuestionTemplateFormSet
from Question.models import Question
from Survey.models import Survey
from .models import Template


class TemplateOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Template/template_option.html')


class TemplateList(ListView):
    model = Template


class TemplateQuestionCreate(CreateView):
    template_name = 'Template/template_form.html'
    model = Template
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(TemplateQuestionCreate, self).get_context_data(**kwargs)
        context['questions'] = QuestionTemplateFormSet(self.request.POST or None)
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
        return super(TemplateQuestionCreate, self).form_valid(form)

        # def form_invalid(self, form):
        #     questions = QuestionTemplateFormSet(self.request.POST or None)
        #     return self.render_to_response(self.get_context_data(form=form, questions=questions))


class TemplateQuestionUpdate(UpdateView):
    template_name = 'Template/template_form.html'
    model = Template
    fields = ['name', 'description', ]
    success_url = reverse_lazy('template:list')

    def get_context_data(self, **kwargs):
        context = super(TemplateQuestionUpdate, self).get_context_data(**kwargs)
        context['questions'] = QuestionTemplateFormSet(self.request.POST or None, instance=self.object)
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
        return super(TemplateQuestionUpdate, self).form_valid(form)


class TemplateRead(View):
    def get(self, request, *args, **kwargs):
        template = get_object_or_404(Template, pk=kwargs['pk'])
        questions = template.questions.all()
        context = {
            'template': template,
            'questions': questions,
        }
        return render(request, 'Template/template_read.html', context)


class TemplateSurvey(View):
    def get(self, request, *args, **kwargs):
        template = get_object_or_404(Template, pk=kwargs['pk'])
        questions = template.questions.all()
        educational_year = EducationalYear.objects.last()
        course = Course.objects.filter(professors__user_id=request.user.id).first()
        if not course:
            raise PermissionDenied
        survey = Survey.objects.create(name=template.name, description=template.description, is_active=False,
                                       professor_id=request.user.id, educational_year_id=educational_year.id,
                                       course_id=course.id, due_date=datetime.datetime.now())
        for question in questions:
            Question.objects.create(order=question.order, body=question.body, choices=question.choices,
                                    type=question.type, required=question.required, survey_id=survey.id)
        return redirect('survey:update', pk=survey.id)
