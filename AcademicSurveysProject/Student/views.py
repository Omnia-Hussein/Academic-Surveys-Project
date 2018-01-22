from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student
from .forms import StudentForm


# Create your views here.
# region Create
def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_index')
    else:
        form = StudentForm()
    return render(request, 'Student/create.html', {'form': form})
# endregion


# region index
def index(request):
    students = Student.objects.all()
    return render(request, "Student/index.html", {"students": students})
# endregion


# # region Details
# def details(request, student_id):
#     student = Student.objects.get(id=student_id)
#     # student = Student.objects.filter(id=student_id).first()
#     return render(request, "Student/details.html", {"student": student})
# # endregion
#
#
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
