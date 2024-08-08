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

def city(request,city):
    if city=="Delhi":
       return HttpResponse("Red Fort")
    elif city=="agra":
       return HttpResponse("Taj Mahal")
    elif city=="jaipur":
        return HttpResponse("Jal Mahal")
    else:
        return HttpResponse('no monument found')

def cost(request,costprice):
    if costprice > 100000:
        return HttpResponse("tax:" +str(0.15 * costprice))
    elif costprice > 50000:
        return HttpResponse("tax" +str(0.10 * costprice))
    else:
        return HttpResponse("tax" +str(0.05 * costprice))
    
def num(request,nmbr):
    last_digit = nmbr % 10
    if last_digit % 3 == 0:
        return HttpResponse("The last digit of the number is divisible by 3.")
    else:
        return HttpResponse("The last digit of the number is not divisible by 3.")    
                

def html(req):
    a="heloooo"
    b=[1,2,3,4,5,6,7,8,9,10]
    c={'name':"aisu",'age':21}
    return render(req,'index.html',{'data':b,'data2':a,'data3':c})  

def htmll(req):
    b=[1,2,3,4,5,6,7,8,9,10]
    return render(req,'2nd.html',{'data':b})      


def student(req):
    students=[{'name':"aiswarya",'age':21,'mark':100},
    {'name':"aisuu",'age':20,'mark':99},
    {'name':"aisu",'age':19,'mark':98},
    {'name':"ais",'age':18,'mark':97},
    {'name':"ai",'age':17,'mark':96}]                  
    return render(req,'studdtls.html',{'data':students})

def above(req):
    students=[{'name':"aiswarya",'age':21,'mark':100},
    {'name':"aisuu",'age':20,'mark':99},
    {'name':"aisu",'age':19,'mark':98},
    {'name':"ais",'age':18,'mark':47},
    {'name':"ai",'age':17,'mark':46}]    
    for i in students:
        if i["mark"]>50:
            selected_students=[{'name':"aiswarya",'age':21,'mark':100},
            {'name':"aisuu",'age':20,'mark':99},
            {'name':"aisu",'age':19,'mark':98}]
    return render(req,'markabove.html',{'std':selected_students})


def below(req):
    students=[{'name':"aiswarya",'age':21,'mark':100},
    {'name':"aisuu",'age':20,'mark':99},
    {'name':"aisu",'age':19,'mark':98},
    {'name':"ais",'age':18,'mark':47},
    {'name':"ai",'age':17,'mark':46}] 
    selected_students=[]   
    for i in students:
        if i["mark"]<50:
            selected_students.append(i) 
    return render(req,'markbelow.html',{'stud':selected_students})

def pet(req):
    return render(req,'static.html')