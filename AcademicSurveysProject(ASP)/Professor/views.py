from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from AcademicSurveysProject.decorators import admin_required, admin_or_profile_professor_required
from Home.forms import UserCreate, UserUpdate
from .forms import ProfessorForm
from .models import Professor


@method_decorator([login_required, admin_required], name='dispatch')
class ProfessorOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Professor/professor_option.html')


@method_decorator([login_required, admin_or_profile_professor_required], name='dispatch')
class ProfessorRead(DetailView):
    model = Professor
    template_name = 'Professor/professor_read.html'
    slug_field = 'user__id_number'


@method_decorator([login_required, admin_required], name='dispatch')
class ProfessorList(ListView):
    model = Professor
    template_name = 'Professor/professor_list.html'


@method_decorator([login_required, admin_required], name='dispatch')
class ProfessorCreate(SuccessMessageMixin, CreateView):
    """
    Creates new Professor along with associated user
    """
    template_name = 'Professor/professor_form.html'
    form_class = ProfessorForm
    second_form_class = UserCreate
    success_message = 'Professor profile saved successfully'

    def get_context_data(self, **kwargs):
        context = super(ProfessorCreate, self).get_context_data(**kwargs)
        if 'user_form' not in context:
            context['user_form'] = self.second_form_class
        return context

    def form_valid(self, form):
        user_form = UserCreate(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            professor = form.save(commit=False)
            professor.user = user
            professor.user.is_professor = True
            professor.save()
            user.save()
        else:
            return self.form_invalid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        user_form = UserCreate(self.request.POST)
        return self.render_to_response(self.get_context_data(form=form, user_form=user_form))


@method_decorator([login_required, admin_required], name='dispatch')
class ProfessorUpdate(SuccessMessageMixin, UpdateView):
    """
    Update Professor profile along with associated user
    """
    model = Professor
    template_name = 'Professor/professor_update.html'
    form_class = ProfessorForm
    second_form_class = UserUpdate
    success_message = 'Professor profile saved successfully'
    slug_field = 'user__id_number'

    def get_success_url(self):
        return reverse('professor:read', kwargs={'slug': str(self.object.user.id_number), })

    def get_context_data(self, **kwargs):
        context = super(ProfessorUpdate, self).get_context_data(**kwargs)
        context['user_form'] = self.second_form_class(self.request.POST or None, instance=self.object.user)
        return context

    def form_valid(self, form):
        user_form = UserUpdate(self.request.POST, instance=self.object.user)
        if user_form.is_valid():
            user_form.save()
        else:
            return self.form_invalid(form)
        return super(ProfessorUpdate, self).form_valid(form)

    def form_invalid(self, form):
        user_form = UserCreate(self.request.POST)
        return self.render_to_response(self.get_context_data(form=form, user_form=user_form))
