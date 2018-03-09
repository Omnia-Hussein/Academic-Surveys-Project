from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from AcademicSurveysProject.decorators import admin_or_response_student_owner_required, response_student_owner_required, \
    admin_required, response_student_course_required
from Answer.forms import AnswerFormSet, AnswerForm
from Answer.models import Answer
from Question.models import Question
from Survey.models import Survey
from .models import Response


@method_decorator([login_required, admin_or_response_student_owner_required], name='dispatch')
class ResponseRead(View):
    def get(self, request, *args, **kwargs):
        response = get_object_or_404(Response, pk=kwargs['pk'])
        survey = response.survey
        questions = survey.questions.all()
        answers = response.answers.all()
        context = {
            'response': response,
            'survey': survey,
            'questions': questions,
            'answers': answers,
        }
        return render(request, 'Response/response_read.html', context)


@method_decorator([login_required, admin_required], name='dispatch')
class ResponseList(ListView):
    model = Response


@method_decorator([login_required, response_student_course_required], name='dispatch')
class ResponseAnswerCreate(CreateView):
    template_name = 'Response/response_form.html'
    model = Response
    fields = []
    success_url = reverse_lazy('home:option')

    # def get(self, request, *args, **kwargs):
    #     """
    #     Handles GET requests and instantiates a blank version of the form.
    #     """
    #     if request.user.is_authenticated():
    #         if request.user.is_student:
    #             if Response.objects.get(survey_id=self.kwargs['id'], student_id=request.user.id):
    #                 return redirect('response:list')
    #             else:
    #                 return self.render_to_response(self.get_context_data())
    #         # TODO: add page to redirect if processor or admin
    #     return redirect('/%s?next=%s' % (settings.LOGIN_URL, request.path))

    def get_context_data(self, **kwargs):
        context = {'survey': get_object_or_404(Survey, pk=self.kwargs['id']),
                   'questions': Question.objects.filter(survey_id=self.kwargs['id']).all()}
        # context = super(ResponseAnswerCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['answers'] = AnswerFormSet(self.request.POST)
        else:
            # initial = []
            number = context['questions'].count()
            # for _ in range(number):
            #     initial.append({'body': ''})
            # answer_formset = inlineformset_factory(Response, Answer, form=AnswerForm, can_delete=False, extra=number,
            #                                        max_num=number, validate_max=True)
            # context['answers'] = answer_formset(initial=initial)
            context['answers'] = inlineformset_factory(Response, Answer, form=AnswerForm, can_delete=False,
                                                       extra=number, max_num=number, validate_max=True)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        answers = context['answers']
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.student_id = self.request.user.id
            self.object.survey_id = self.kwargs['id']
            self.object.save()
            if answers.is_valid():
                answers.instance = self.object
                instances = answers.save(commit=False)
                # questions = Survey.objects.get(id=self.kwargs['id']).questions.all()
                questions = context['survey'].questions.all()
                for answer, question in zip(instances, questions):
                    answer.question_id = question.id
                answers.save()
        return super(ResponseAnswerCreate, self).form_valid(form)


@method_decorator([login_required, response_student_owner_required], name='dispatch')
class ResponseAnswerUpdate(UpdateView):
    template_name = 'Response/response_form.html'
    model = Response
    fields = []
    success_url = reverse_lazy('home:option')

    def get_object(self):
        return get_object_or_404(Response, survey_id=self.kwargs['slug'], student_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(ResponseAnswerUpdate, self).get_context_data(**kwargs)
        context['survey'] = Survey.objects.get(pk=self.kwargs['slug'])
        context['questions'] = Question.objects.filter(survey_id=self.kwargs['slug']).all()
        context['answers'] = AnswerFormSet(self.request.POST or None, instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        answers = context['answers']
        with transaction.atomic():
            form.save()
            if answers.is_valid():
                answers.save()
        return super(ResponseAnswerUpdate, self).form_valid(form)
