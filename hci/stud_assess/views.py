from django.contrib.auth import views, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.template import loader
from django.views.generic import View
# from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django import template
from django.contrib.auth.models import Group


def home(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		students = Student.objects.all()
		is_teacher = request.user.groups.filter(name='teacher')
		is_student = request.user.groups.filter(name='student')
		return render(request, "stud_assess/home.html", {'students': students, 
														'is_teacher': is_teacher, 
														'is_student': is_student})

    

def displayMarks(request, stud_id):
	data = Student.objects.filter(id=stud_id)
	students = Student.objects.all()
	return render(request, "stud_assess/canvas.html", {'data': data, 'students': students})


# class UserFormView(View):
#     form_class = UserForm
#     template_form = 'stud_assess/login.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_form, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             # cleaned version of data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # return users credentials if user is corrrect
#             user = authenticate(username=username, password=password)
#
#             print(user)
#             print("Helloooooooooooooooooooooooooooooooooo")
#
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('/hello')
