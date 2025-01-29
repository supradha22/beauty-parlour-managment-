from django.shortcuts import render,redirect
from wipro.models import*
from.models import*
# Create your views here.

def hey(request):
    data=Branch.objects.all()
    data1=saloon.objects.all()
    data2=service.objects.all()
    return render(request,'user.html',{'data':data,'data1':data1,'data2':data2})
def contacts(request):
    return render(request,'contact.html')
def contactinfo(request):
      if request.method=='POST':
         name1=request.POST['name1']
         email1=request.POST['email1']
         message=request.POST['message']
         data=contact(name1=name1,email1=email1,message=message)
         data.save()
      return redirect('contacts')
  
def login(request):
    return render(request,'login.html')
def registerinfo(request):
    return render(request,'register.html')
def register1(request):
      if request.method=='POST':
         name=request.POST['name']
         email=request.POST['email']
         password=request.POST['password']
         number=request.POST['number']
         data=registering(name=name,email=email,password=password,number=number)
         data.save()
      return redirect('registerinfo')




def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        if registering.objects.filter(name=username,email=email).exists():
           data = registering.objects.filter(name=username,email=email).values('id','number','password').first()
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['number'] 
           request.session['password_u'] = data['password'] 
           request.session['username_u'] = username
           request.session['email_u'] = email
           return redirect('hey') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('hey')

def userlogout(request):
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('hey')

def card(request):
     data=Branch.objects.all()
     return render(request,'card.html',{'data':data})



def card1(request,branch):
    if(branch == "all"):
        data =saloon.objects.all()
    else:
        data =saloon.objects.filter(branch=branch)   
    return render(request,'card1.html',{'data':data})
 

def card2(request,saloon):
    if(saloon == "all"):
     data2 =service.objects.all()
    else:
     data2 =service.objects.filter(saloon=saloon)
    return render(request,'card2.html',{'data2':data2})
 
def view2(request,id):
    data2=service.objects.filter(id=id)
    return render(request,'view.html',{'data2':data2})
def bookinginfo(request,id):
    if 'u_id' in request.session:

       data2=service.objects.filter(id=id)
       return render(request,'booking.html',{'data2':data2})
    return render(request,'login.html',{'msg1':"you need to login first to access this page"})
# def userid()
def bookservice(request,id):
    if request.method == "POST":
     u_id =request.session.get('u_id')
     bookingdate =request.POST.get('bookingdate')
     bookingtime =request.POST.get('bookingtime')
     data=booking(userreg =registering.objects.get(id=u_id),userser =service.objects.get(id=id),bookingdate=bookingdate,bookingtime=bookingtime)
     data.save()
    return redirect(history)
def history(request):
     u_id =request.session.get('u_id')
     data=booking.objects.filter(userreg=u_id)
     return render(request,'history.html',{'data':data})
