from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list
#         })

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Poll does not exist")
#     return render(request, "polls/detail.html", {
#         "question": question
#     })
    

# def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/results.html", {
#         "question": question
#    })

#class base views
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five published questions"""
        #se coloca el - en el parametro para indicarle desde la mas reciente a las mas antiguas
        #slice [:5] cantidad que busca en la consulta
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #se valida si el usuario seleciono una respuesta valida
        select_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #si no seleciona una opcion hace un render con el mensaje
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Not's selected a answer"
        })
    else:
        #si es valido se almacena el voto en la bd
        select_choice.votes += 1
        select_choice.save()
        #redirrecion de los formularios
        #reverse es la version en python de URL en django
        return HttpResponseRedirect(reverse( "polls:results", args=(question.id,)))