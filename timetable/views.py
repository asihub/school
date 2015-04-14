from django.shortcuts import render
from timetable.models import Timetable
from datetime import datetime, timedelta


# --- Розклад ---
def timetable(request, week="this"):
    
    if week == "this":
        p = getWeekParity()
    else:
        p = getWeekParity(delta=7)

    if p: 
        tt_list = Timetable.objects.exclude(week_parity=1)
    else: 
        tt_list = Timetable.objects.exclude(week_parity=2)
        
    today = datetime.today()
    
    context = {'tt_list': tt_list, 'parity': p, 'today': today, 'week': week}
    return render(request, 'timetable/timetable.html', context)


# --- Перевірим, чи тиждень парний ---
def getWeekParity(forDate=datetime.today(), delta=0):    
    
    forDate += timedelta(days=delta)
    return (int(forDate.strftime("%U")) + 1) % 2 == 0
    
        
    