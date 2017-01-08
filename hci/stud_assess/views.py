from django.contrib.auth import views
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.template import loader


# Create your views here.

# def teacher_login(request):
#     template_response = views.login(request),
#     # Do something with 'template_response'
#     return template_response

# def teacher_login(request):
#     template = loader.get_template('stud_assess/teacher_login.html')
#     return HttpResponse(template.render())


def home(request):
    template = loader.get_template('stud_assess/home.html')
    return HttpResponse(template.render())


def index(request):
    latest_ques = Question.objects.order_by('-pub_date')[:3]
    # output = ', '.join([q.question_text for q in latest_ques])
    template = loader.get_template('stud_assess/index.html')
    context = {
        'latest_question': latest_ques
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse('You are viewing question number %s.' % question_id)
