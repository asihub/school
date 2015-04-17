from django.shortcuts import render

def votes(request):
    
    return render(request, "vote/votes.html")