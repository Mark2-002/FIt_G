from django.shortcuts import render

# Create your views here.
def home(request):

     return render(request,"index.html")
def form1(request):
    data={}
    try:
     if request.method=="POST":
    #  n1 =int(request.GET['num1']),
    #  n2 =int(request.GET['num2']),
         n1 = int(request.POST.get('num1'))
         n2 =int(request.POST.get('num2'))
         final=n1+n2
     data={
         'n1':n1,
         'n2':n2,
         'output':final
         }

    except:
         pass 
    return render(request,"form.html",data)

def login_form(request):
    data={}
    try:
      unm=request.POST.get('username')
      pwd=request.POST.get('password')
      data={
        'usn':unm,
        'psw':pwd
      }
    except:
        pass
    return render(request,"login_form.html",data)

def data(request):
    return render(request,"data.html")


def contact_us(request):
    return render(request,"contact_us.html")

def services(request):
    return render(request,"services.html")


def s_citizen(request):
    return render(request,"s_citizen.html")


def kids(request):
    return render(request,"kids.html")

def sum(request):
    try:
        n=request.GET["first"]
        n1=request.GET["second"]
        
    except:
        pass
    
    return render(request,"sum.html",{"first":n,"second":n1})    