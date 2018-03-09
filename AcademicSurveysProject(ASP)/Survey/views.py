import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from AcademicSurveysProject.decorators import professor_required, survey_professor_owner_required, \
    admin_required, admin_or_survey_professor_owner_required
from Course.models import Course
from Question.forms import QuestionSurveyFormSet
from Student.models import Student
from Survey.utils import render_to_pdf
from .models import Survey


@method_decorator([login_required, admin_required], name='dispatch')
class SurveyOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Survey/survey_option.html')


@method_decorator([login_required, admin_required], name='dispatch')
class SurveyList(ListView):
    model = Survey


@method_decorator([login_required, professor_required], name='dispatch')
class SurveyQuestionCreate(CreateView):
    template_name = 'Survey/survey_form.html'
    model = Survey
    fields = ['name', 'description', 'due_date', 'is_active', 'course', 'educational_year', ]

    def get_form(self, form_class=None):
        form = super(SurveyQuestionCreate, self).get_form()
        form.fields['course'].queryset = Course.objects.filter(professors__user_id=self.request.user.id)
        return form

    def get_context_data(self, **kwargs):
        context = super(SurveyQuestionCreate, self).get_context_data(**kwargs)
        context['questions'] = QuestionSurveyFormSet(self.request.POST or None)
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
                # to send notification emails
                course = self.object.course
                students = Student.objects.filter(courses=course).all()
                for student in students:
                    send_mail('Created survey', 'There is s survey which has been created, please visit the website',
                              'customsmtp587@gmail.com', [student.user.email])
        return super(SurveyQuestionCreate, self).form_valid(form)

        # def form_invalid(self, form):
        #     questions = QuestionSurveyFormSet(self.request.POST or None)
        #     return self.render_to_response(self.get_context_data(form=form, questions=questions))


@method_decorator([login_required, survey_professor_owner_required], name='dispatch')
class SurveyQuestionUpdate(UpdateView):
    template_name = 'Survey/survey_form.html'
    model = Survey
    fields = ['name', 'description', 'due_date', 'is_active', 'course', 'educational_year', ]
    success_url = reverse_lazy('survey:list')

    def get_form(self, form_class=None):
        form = super(SurveyQuestionUpdate, self).get_form()
        form.fields['course'].queryset = Course.objects.filter(professors__user_id=self.request.user.id)
        return form

    def get_context_data(self, **kwargs):
        context = super(SurveyQuestionUpdate, self).get_context_data(**kwargs)
        context['questions'] = QuestionSurveyFormSet(self.request.POST or None, instance=self.object)
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
                # to send notification emails
                course = self.object.course
                students = Student.objects.filter(courses=course).all()
                # datatuple = ()
                for student in students:
                    send_mail('Updated survey', 'There is s survey which has been updated, please visit the website',
                              'customsmtp587@gmail.com', [student.user.email])
                    #     datatuple += (('Updated survey',
                    #                    'There is s survey which has been updated, please visit the website',
                    #                    'customsmtp587@gmail.com', [student.user.email]))
                    # send_mass_mail(datatuple)
        return super(SurveyQuestionUpdate, self).form_valid(form)


@method_decorator([login_required, admin_or_survey_professor_owner_required], name='dispatch')
class SurveyRead(View):
    def get(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey, pk=kwargs['pk'])
        questions = survey.questions.all()
        answers = []
        for question in questions:
            vote = []
            for i in range(6):
                vote += [question.answers.filter(body=i).count()]
            answers += [vote]
        total_number_of_students = survey.course.students.count()
        voted = survey.course.students.filter(responses__survey_id=survey.id).count()
        not_voted = total_number_of_students - voted
        context = {
            'survey': survey,
            'questions': questions,
            'answers': answers,
            'total_number_of_students': total_number_of_students,
            'voted': voted,
            'not_voted': not_voted,
        }
        return render(request, 'Survey/survey_read.html', context)


@method_decorator([login_required, admin_or_survey_professor_owner_required], name='dispatch')
class SurveyReadPDF(View):
    def get(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey, pk=kwargs['pk'])
        questions = survey.questions.all()
        answers = []
        for question in questions:
            vote = []
            for i in range(6):
                vote += [question.answers.filter(body=i).count()]
            answers += [vote]
        total_number_of_students = survey.course.students.count()
        voted = survey.course.students.filter(responses__survey_id=survey.id).count()
        not_voted = total_number_of_students - voted
        context = {
            'survey': survey,
            'questions': questions,
            'answers': answers,
            'total_number_of_students': total_number_of_students,
            'voted': voted,
            'not_voted': not_voted,
        }
        pdf = render_to_pdf('Survey/survey_read_pdf.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ASP - Survey #' + str(survey.id) \
                                          + ' - ' + str(datetime.datetime.now().strftime('%d-%m-%Y')) + '.pdf"'
        return response
