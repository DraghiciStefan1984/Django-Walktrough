from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    latest_question_list=Question.objects.all()
    return render(request, 'index.html', {'latest_question_list':latest_question_list})

def detail(request, question_id):
    return render(request, 'detail: '+question_id)

def results(request, question_id):
    return render(request, 'results: '+question_id)

def vote(request, question_id):
    return render(request, 'votes: '+question_id)