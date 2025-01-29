from django.shortcuts import render,redirect
from.models import*
from irohub.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse ,JsonResponse
from rest_framework.parsers import JSONParser
from.models import*
from.serializers import*
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

# @csrf_exempt
# def article_list(request):
#      if request.method=='GET':
#           article=saloon.objects.all()
#           serial=work(article,many=True)
#           return JsonResponse(serial.data, safe=False)
#      elif request.method=="POST":
#        data=JSONParser().parse(request)
#        serial=work(data=data)
#        if serial.is_valid():
#         saloon.objects.create(**serial.validated_data)
#         return JsonResponse(serial.data,status=201)
#        return JsonResponse(serial.errors,status=400)
@csrf_exempt
# def article_detail(request, pk):
#     try:
#       saloo= saloon.objects.get(pk=pk)
#     except saloon.DoesNotExist:
#          return HttpResponse(status=404)
#     if request.method=="GET":
#        serial=work(saloo)
#        return JsonResponse(serial.data)
#     elif request.method=='PUT':
#       data=JSONParser().parse(request) 
#       serail=work(saloo,data=data)
#       if serail.is_valid():
#         saloon.objects.filter(pk=pk).update(**serail.validated_data)
#         return JsonResponse(serail.data,status=400)


#       return JsonResponse(serail.errors,status=400)
#     elif request.method == "DELETE":
#       saloo.delete()
#       return HttpResponse(status=204) 
   
@api_view(['GET', 'POST'])
def article_list(request):
     if request.method=='GET':
          article=saloon.objects.all()
          serial=work(article,many=True)
          return Response(serial.data)
     elif request.method=="POST":
       serial=work(data=request.data)
       if serial.is_valid():
        
           saloon.objects.create(**serial.validated_data)
           return Response(serial.data, status=201) 
       return Response(serial.errors, status=400)
       
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
      saloo= saloon.objects.get(pk=pk)
    except saloon.DoesNotExist:
         return HttpResponse(status=404)
    if request.method=="GET":
       serial=work(saloo)
       return Response(serial.data)
    elif request.method=='PUT':
      serial=work(saloo,data=request.data)
      if serial.is_valid():
         saloon.objects.filter(pk=pk).update(**serial.validated_data)
         return Response(serial.data)


      return Response(serial.errors,status=400)
    elif request.method == "DELETE":
      saloo.delete()
      return HttpResponse(status=204) 


class articleAPIview(APIView): 
 def get(self,request):
    article=saloon.objects.all()  
    serial=work(article,many=True) 
    return Response(serial.data)
 def post(self,request):
     serial=work(data=request.data)
     if serial.is_valid():
       saloon.objects.create(**serial.validated_data)
       return Response(serial.data, status=201) 
     return Response(serial.errors, status=400)


class articledetails(APIView):
 def get_object(self,id):
     try:
               return saloon.objects.get(id=id)
     except saloon.doesnotexist:
        return HttpResponse(status=404)   
 def get(self,request,id):
      salon=self.get_object(id)
      serial=work(salon)
      return Response(serial.data)
 def put(self,request,id):
       salon=self.get_object(id)
       serial=work(salon,data=request.data)
       if serial.is_valid():
         saloon.objects.filter(id=id).update(**serial.validated_data)
         return Response(serial.data)
       return Response(serial.errors, status=400)
 def delete(self,request,id):
      salon=self.get_object(id)
      salon.delete()
      return Response(status=204)



def hello(request):
      bran=Branch.objects.all().count()
      sal=saloon.objects.all().count()
      ser=service.objects.all().count()
      cont=contact.objects.all().count()
      reg=contact.objects.all().count()
      requ=booking.objects.filter(status=0).count()
      app=booking.objects.filter(status=1).count()
      decl=booking.objects.filter(status=2).count()
  
      return render(request,'admin.html',{'bran':bran,'sal':sal,'ser':ser,'cont':cont,'reg':reg,'requ':requ,'app':app,'decl':decl})
def form(request):
    return render(request,"form.html")
def table(request):
    data=Branch.objects.all()
    return render(request,"table.html",{'data':data})
def branchinfo(request):
      if request.method=='POST':
         name=request.POST['name']
         image=request.FILES['image']
         data=Branch(name=name,image=image)
         data.save()
      return redirect('hello')
def edit(request,id):
        data=Branch.objects.filter(id=id)
        return render(request,'edit.html',{'data':data})
def delete(request,id):
        Branch.objects.filter(id=id).delete()
        return redirect('table')
def update(request,id):
     if request.method=='POST':
        name=request.POST['name']

        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Branch.objects.get(id=id).image

        Branch.objects.filter(id=id).update(name=name,image=file)
        return redirect('table')
def form1(request): 
    data=Branch.objects.all() 
    return render(request,"form1.html",{'data':data})
def table1(request):
    data1=saloon.objects.all()
    return render(request,"table1.html",{'data1':data1})
def salooninfo(request):
      if request.method=='POST':
         name1=request.POST['name1']
         image1=request.FILES['image1']
         branch=request.POST['branch']
         data1=saloon(name1=name1,image1=image1,branch=branch)
         data1.save()
      return redirect('hello')
  
def edit1(request,id):
        data=Branch.objects.all()
        data1=saloon.objects.filter(id=id)
        return render(request,'edit1.html',{'data1':data1 ,'data':data})
def delete1(request,id):
        saloon.objects.filter(id=id).delete()
        return redirect('table1')

def update1(request,id):
     if request.method=='POST':
        name1=request.POST['name1']
        branch=request.POST['branch']

        try:
            img_c = request.FILES['image1']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = saloon.objects.get(id=id).image1

        saloon.objects.filter(id=id).update(name1=name1,branch=branch,image1=file)
        return redirect('table1')
def form2(request):  
       data1=saloon.objects.all()
       return render(request,"form2.html",{'data1':data1})
def table2(request):
    data2=service.objects.all()
    return render(request,"table2.html",{'data2':data2})
def serviceinfo(request):
      if request.method=='POST':
         name2=request.POST['name2']
         image2=request.FILES['image2']
         price=request.POST['price']
         description=request.POST['description']
         saloon=request.POST['saloon']
         data2=service(name2=name2,image2=image2,price=price,saloon=saloon,description=description)
         data2.save()
      return redirect('hello')
  
def edit2(request,id):
        data1=saloon.objects.all()
        data2=service.objects.filter(id=id)
        return render(request,'edit2.html',{'data2':data2,'data1':data1})
def delete2(request,id):
        service.objects.filter(id=id).delete()
        return redirect('table2')

def update2(request,id):
     if request.method=='POST':
        name2=request.POST['name2']
        saloon=request.POST['saloon']
        description=request.POST['description'] 
        price=request.POST['price']
        
    

        try:
            img_c = request.FILES['image2']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = service.objects.get(id=id).image2

        service.objects.filter(id=id).update(name2=name2,image2=file,saloon=saloon,description=description,price=price)
        return redirect('table2')

def regg(request):
    data=registering.objects.all()
    return render(request,"regtable.html",{'data':data})
def cont(request):
     data=contact.objects.all()
     return render(request,"conttable.html",{'data':data})
def req(request):
     data=booking.objects.filter(status=0)
     return render(request,"bookingrequest.html",{'data':data})
def approve(request,id):
     booking.objects.filter(id=id).update(status = 1)
     return redirect('req')
def declined(request,id):
     booking.objects.filter(id=id).update(status = 2)
     return redirect('req')
def apr(request):
     data=booking.objects.filter(status=1)
     return render(request,'approved.html',{'data':data})
def dec(request):
     data=booking.objects.filter(status=2)
     return render(request,'declined.html',{'data':data})     