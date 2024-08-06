from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun1(request):
    return HttpResponse('welcome')

def fun2(request):
    return HttpResponse('hello everyone') 

def fun3(request,a,b):
    return HttpResponse(str(a)+'  '+b)    

def fun4(request,a,c):
    if a>c:
        return HttpResponse("a is large")
    else:
        return HttpResponse("c is large")    
    return HttpResponse(str(a)+'  '+str(c))  

def salary(request,year,sal):
    
    if year>5:
        return HttpResponse("Eligible for 5 percent salary : "+str(sal*1.05))
    else:
         return HttpResponse("Not eligible for 5 percent salary")     
    

def bill(request,unit):
    if unit<=100:
        return HttpResponse("No charge !")
    elif unit<200:
        return HttpResponse("5 rupees extra:" +str((unit-100)*5))
    elif unit>200:
        return HttpResponse("10 per unit !:" +str((unit-200)*10+500))           
     
   
def number(request,num):
    if num==1:
       return HttpResponse("sunday") 
    elif num==2: 
        return HttpResponse("monday") 
    elif num==3:
       return HttpResponse("tuesday")
    elif num==4:
       return HttpResponse("wednesday")
    elif num==5:
       return HttpResponse("thursday")
    elif num==6:
       return HttpResponse("friday")
    elif num==7:
       return HttpResponse("saturday")
    elif num==8:
       return HttpResponse("invalid !")                     
