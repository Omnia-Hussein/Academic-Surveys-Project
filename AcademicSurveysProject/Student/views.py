from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from Home.forms import UserForm


# Create your views here.
# region Create
def create(request):
    if request.method == 'POST':
        signup_form = UserForm(request.POST)
        form = StudentForm(request.POST)
        if signup_form.is_valid() and form.is_valid():
            user = signup_form.save()
            Student.objects.create(
                user=user,
                secondary_email=form.cleaned_data['secondary_email'],
                type=form.cleaned_data['type'],
            )
            user.save()
            return redirect('student_list')
    else:
        signup_form = UserForm()
        form = StudentForm()
    return render(request, 'Student/create.html', {'user_form': signup_form, 'form': form})
# endregion


# region index
def index(request):
    students = Student.objects.all()
    return render(request, "Student/list.html", {"students": students})
# endregion


# region Details
def read(request, student_id_number):
    student = Student.objects.get(id_number=student_id_number)
    # student = Student.objects.filter(id=student_id).first()
    return render(request, "Student/read.html", {"student": student})
# endregion


# # region Update
# def edit(request, st_id):
#     if request.method == 'GET':
#         student = Student.objects.filter(id=st_id).first()
#         return render(request, "Student/edit.html", {"student": student})
#     else:
#         old = Student.objects.get(id=st_id)
#         st = StudentForm(request.POST)
#         old.name = st['name'].value()
#         old.address = st['address'].value()
#         old.academic_year = st['academic_year'].value()
#         old.mobile_number = st['mobile_number'].value()
#
#         old.save()
#         return redirect("st_index")
# # endregion
#
#
# # region Delete
# def delete(request, st_id):
#     Student.objects.get(id=st_id).delete()
#     return redirect("st_index")
# # endregion
