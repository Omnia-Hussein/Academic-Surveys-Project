from django.shortcuts import render, redirect
from .models import Survey
from .forms import SurveyForm, QuestionForm ,UserForm

# region Create
def create(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
            Survey.objects.create(
                user=user,
                id_number=form.cleaned_data['id_number'],
                name=form.cleaned_data['name'],
                mobile_number=form.cleaned_data['mobile_number'],
                secondary_email=form.cleaned_data['secondary_email'],
                type=form.cleaned_data['type'],
            )
            user.save()
            return redirect('student_index')
    else:
        signup_form = SignUpForm()
        form = StudentForm()
    return render(request, 'Student/create.html', {'signup_form': signup_form, 'form': form})
# endregion


# region index
def index(request):
    students = Student.objects.all()
    return render(request, "Student/index.html", {"students": students})
# endregion



