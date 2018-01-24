from django.shortcuts import render, redirect
from .models import Professor
from .forms import ProfForm, SignUpForm


# Create your views here.
# region Create
def create(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        form = ProfForm(request.POST)
        if signup_form.is_valid() and form.is_valid():
            user = signup_form.save()
            Professor.objects.create(
                user=user,
                id_number=form.cleaned_data['id_number'],
                name=form.cleaned_data['name'],
                mobile_number=form.cleaned_data['mobile_number'],
                secondary_email=form.cleaned_data['secondary_email'],

            )
            user.save()
            return redirect('professor_index')
    else:
        signup_form = SignUpForm()
        form = ProfForm()
    return render(request, 'create.html', {'signup_form': signup_form, 'form': form})
# endregion


# region index
def index(request):
    Professors = Professor.objects.all()
    return render(request, "index.html", {"Professors": Professors})
# endregion