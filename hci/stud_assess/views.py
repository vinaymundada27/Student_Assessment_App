from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.


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