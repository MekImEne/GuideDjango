from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.template import loader, RequestContext

from .models import Question, Choice

def index (request):
    list_questions = Question.objects.order_by('-pub_date')[:5]
    #output = ", ".join(q.question_text for q in list_questions)
    #return HttpResponse(output)
    #template = loader.get_template('polls/index.html')
    context = {'list_questions': list_questions}

    #first code return HttpResponse('Great job guys ! This is the index page of our polls application')
    #second code return HttpResponse(template.render(context, request)) # the results will not be ordered 1,2,3,...

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("This is the detail view of the question: %s" %question_id)
    #question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    #return HttpResponse("This are the results of the question: %s" %question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    #return HttpResponse("Vote on the question: %s" %question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Please select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return  HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
