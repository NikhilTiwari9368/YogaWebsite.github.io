from django.shortcuts import render 
from django.http import HttpResponse
from matplotlib.style import context
from services.models import services
from contact.models import contact
from django.contrib.auth.forms import UserCreationForm

def home(request):

    servicesData = services.objects.all()
    # for a in servicesData:
    #     print(a)
    # print(servicesData)

    return render(request , "home.html")

def userform(request):
    finalans = 0 
    data={}

    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            print(finalans)
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
    except:
        pass
    return render(request , "userform.html",data)

def saveEnquiry(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        en=contact(contact_name=name , contact_email = email , contact_comment=comment)

        en.save()
    return render(request ,"home.html")

def login(request):
    return render(request , "login.html")

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request , "register.html" , context)