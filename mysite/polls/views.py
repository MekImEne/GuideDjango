from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader, RequestContext

from .models import Question

def index (request):
    list_questions = Question.objects.order_by('-pub_date')[:5]
    #output = ", ".join(q.question_text for q in list_questions)
    #return HttpResponse(output)
    # first code return HttpResponse('Great job guys ! This is the index page of our polls application')

    #template = loader.get_template('polls/index.html')
    context = {'list_questions': list_questions}

    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: %s" %question_id)

def results(request, question_id):
    return HttpResponse("This are the results of the question: %s" %question_id)

def vote(request, question_id):
    return HttpResponse("Vote on the question: %s" %question_id)