from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import CreateView, ListView

from Answer.forms import AnswerFormSet
from Question.models import Question
from Survey.models import Survey
from .models import Response


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


class ResponseList(ListView):
    model = Response


class ResponseAnswerCreate(CreateView):
    template_name = 'Response/response_form.html'
    model = Response
    fields = []

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
        context = {'questions': Question.objects.filter(survey_id=self.kwargs['id']).all(),
                   'survey': get_object_or_404(Survey, pk=self.kwargs['id'])}
        # context = super(ResponseAnswerCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['answers'] = AnswerFormSet(self.request.POST)
        else:
            initial = []
            count = []
            number = context['survey'].questions.count()
            for i in range(number):
                initial += [{'body': ''}]
                count += [i]
            context['answers'] = AnswerFormSet(initial=initial, )  # max_num=number, validate_max=True)
            context['number'] = count
        # context['questions_answers'] = zip(context['questions'], context['answers'])
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


# class ResponseAnswerUpdate(UpdateView):
#     template_name = 'Response/response_form.html'
#     model = Response
#     fields = []
#     success_url = reverse_lazy('response:list')
#
#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests and instantiates a blank version of the form.
#         """
#         if request.user.is_authenticated():
#             if request.user.is_student:
#                 if Response.objects.get(survey_id=self.kwargs['slug'], student_id=request.user.id):
#                     self.object = get_object_or_404(Response, survey_id=self.kwargs['slug'],
#                                                     student_id=self.request.user.id)
#                     return self.render_to_response(self.get_context_data())
#                 else:
#                     return redirect('response:create', self.kwargs['slug'])
#             # TODO: add page to redirect if processor or admin
#         return redirect('/%s?next=%s' % (settings.LOGIN_URL, request.path))
#
#     def get_object(self):
#         return get_object_or_404(Response, survey_id=self.kwargs['slug'], student_id=self.request.user.id)
#
#     def get_context_data(self, **kwargs):
#         context = super(ResponseAnswerUpdate, self).get_context_data(**kwargs)
#         context['questions'] = Question.objects.filter(survey_id=self.kwargs['slug']).all()
#         context['answers'] = AnswerFormSet(self.request.POST or None, instance=self.object)
#         return context
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         answers = context['answers']
#         with transaction.atomic():
#             form.save()
#             if answers.is_valid():
#                 answers.save()
#         return super(ResponseAnswerUpdate, self).form_valid(form)


# class ResponseAnswerUpdate(View):
#     def render_the_template(self, request, **kwargs):
#         response = get_object_or_404(Response, survey_id=kwargs['slug'], student_id=self.request.user.id)
#         context = {
#             'questions': Question.objects.filter(survey_id=kwargs['slug']),
#             'answers': AnswerFormSetUpdate(queryset=Answer.objects.filter(response=response))
#         }
#         return render(request, 'Response/response_update.html', context)
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             if request.user.is_student:
#                 if Response.objects.get(survey_id=kwargs['slug'], student_id=request.user.id):
#                     return self.render_the_template(request, **kwargs)
#                 else:
#                     return redirect('response:create', kwargs['slug'])
#             # TODO: add page to redirect if processor or admin
#         return redirect('/%s?next=%s' % (settings.LOGIN_URL, request.path))
#
#     def post(self, request, *args, **kwargs):
#         response = get_object_or_404(Response, survey_id=kwargs['slug'], student_id=self.request.user.id)
#         response.save()
#         answers = AnswerFormSetUpdate(self.request.POST)
#         if answers.is_valid():
#             response.save()
#             answers.save()
#         return redirect('response:list')
