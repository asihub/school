from django.shortcuts import render, get_object_or_404, redirect
from .models import Vote, Answer, Result

def votes(request):
    
    votes = Vote.objects.filter(status=1)
    context = {"dataset": votes}   
    
    return render(request, "vote/votes.html", context)

def vote(request, vote_id=1):
    
    vote = get_object_or_404(Vote, pk=vote_id)
    
    if request.method=="POST":
        if "answer" in request.POST:
            result = Result(answer_id=request.POST["answer"], user=request.user)
            result.save()
            redirect(".")        
    
    
    answers = Answer.objects.filter(vote_id=vote_id)
    #results = Result.objects.

    
    return render(request, "vote/vote.html", {"vote": vote, "dataset": answers})

