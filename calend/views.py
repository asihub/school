from django.shortcuts import render, redirect
from calendar import Calendar
from datetime import datetime
from .forms import EventForm
from .models import Event


def yearCalend(request, year=datetime.now().year, month=datetime.now().month):

    # Якщо був post 
    ev_form = EventForm(request.POST or None)   

    if ev_form.is_valid():
        event = ev_form.save(commit=False)
        event.author = request.user.username
        event.save()
        return redirect('.')    

    
    events = Event.objects.filter(ev_date__month=month).order_by("ev_date")   
       
    if isinstance(year, str):
        year = int(year)    
    if isinstance(month, str):
        month = int(month)    

    #year=datetime.now().year, month=datetime.now().month

    calend = Calendar(firstweekday=0)
    
    # days = list(calend.itermonthdates(datetime.now().year, datetime.now().month)) # дати місяця
    # days = list(calend.itermonthdays(datetime.now().year, datetime.now().month)) # дні місяця    
    
    days = list(calend.itermonthdays2(year, month)) # кортежі день місяця:день тижня
    
    days_titles = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]
    months_titles = ["Січень", "Лютий", "Березень", 
                     "Квітень", "Травень", "Червень", 
                     "Липень", "Серпень", "Вересень", 
                     "Жовтень", "Листопад", "Грудень"]
    
    month_title = months_titles[month - 1]    
    
    if month == datetime.now().month:
        today = datetime.now().day
    else:
        today = None 
    
    prev_calend = prev_month(year, month)
    next_calend = next_month(year, month)
    
    context = {'days': days, 
               "days_titles": days_titles, 
               "month_title": month_title,
               "month": month,
               "prev_month": prev_calend[1],
               "next_month": next_calend[1],
               "prev_year": prev_calend[0],
               "next_year": next_calend[0],
               "ev_form":ev_form,
               "events":events,
               }
    
    if today is not None:
        context.update({"today": today})    
    
    return render(request, 'calend/yearcalend.html', context)

# Наступний місяь
def next_month(year=datetime.now().year, month=datetime.now().month):
    
    if month in range(1,12):
        month += 1 
    elif month == 12:
        month = 1
        year += 1
    else:
        raise ValueError
    
    return (year, month)

# Попередній місяць
def prev_month(year=datetime.now().year, month=datetime.now().month):
    
    if month in range(2,13):
        month -= 1 
    elif month == 1:
        month = 12
        year -= 1
    else:
        raise ValueError
    
    return (year, month)





        