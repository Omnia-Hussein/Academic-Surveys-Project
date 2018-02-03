from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from Question.forms import QuestionTemplateFormSet
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
