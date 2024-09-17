from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    # all_perseon = Person.objects.filter(age = 23)
    all_perseon = Person.objects.all()
    return render(request,"index.html",{"all_person":all_perseon})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        print(name,age)
        #บันทึกข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request,"บันทึกแล้วจ้า !!")
        #เปลี่ยนเส้นทาง
        return redirect("/")
        #บันทึกข้อมูล
    else :
        return render(request,"form.html")
    
    
def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()

        messages.success(request,"แก้ไขข้อมูลแล้วจ้า !!")
        #เปลี่ยนเส้นทาง
        return redirect("/")
    else:
        # ดึงข้อมูลประชากรที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})

def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()

    messages.success(request,"ลบข้อมูลแล้วจ้า !!")
    #เปลี่ยนเส้นทาง
    return redirect("/")