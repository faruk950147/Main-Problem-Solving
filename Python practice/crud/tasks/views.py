from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'students/student_list.html', {'students': students})

# def add_student(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')

#         Student.objects.create(name=name, email=email, phone=phone)
#         return redirect('student_list')

#     return render(request, 'students/add_student.html')

# def edit_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'POST':
#         student.name = request.POST.get('name')
#         student.email = request.POST.get('email')
#         student.phone = request.POST.get('phone')
#         student.save()
#         return redirect('student_list')
#     return render(request, 'students/edit_student.html', {'student': student})

# def delete_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'POST':
#         student.delete()
#         return redirect('student_list')
#     return render(request, 'students/confirm_delete.html', {'student': student})



# 🔸 Create
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/add_student.html', {'form': form})

# 🔸 Read
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# 🔸 Update
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/edit_student.html', {'form': form})

# 🔸 Delete
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'student': student})
