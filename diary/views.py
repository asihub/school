from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm
from datetime import datetime 


def diary(request):
    
    form = DiaryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    
    # виводимо завдання
    #d_notes = Diary.objects.all()
    d_notes = Diary.objects.filter(hw_date__gte = datetime.today())
    context = {'d_notes': d_notes, 'form': form}
    return render(request, 'diary/diary.html', context)

