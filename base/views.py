from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from datetime import datetime
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import authenticate, login, logout


def base(request):   
    
    return redirect("/articles/")


def user_login(request):    
    
    # якщо ми в форму получили post (логін/пароль)
    if request.method == 'POST':
            
        username = request.POST['username']
        password = request.POST['password']
          
        user = authenticate(username=username, password=password)
  
        if (user is not None) and user.is_active:
            login(request, user)                        
            return redirect("/")
        else:
            return render(request, "base/login.html", {"login_error": "Помилка входу. Спробуйте ще раз."})
    
    # якщо поста не було, малюєм форму
    return render(request, "base/login.html")


def user_logout(request):    
    logout(request)
    return render(request, "base/login.html")
    
          
# робив кукі
# def base2(request):   
#     
#     if "last_visit" in request.COOKIES:
#         last_visit = "Останній візит: {}".format(request.COOKIES["last_visit"])
#     else:
#         last_visit = "Останній візит: невідомо"
#     
#     context = {"last_visit": last_visit}
# 
#     response =  render(request, 'base/base.html', context)
#     response.set_cookie("last_visit", datetime.today().strftime("%d.%m.%Y %H:%M"))
#     
#     return response        