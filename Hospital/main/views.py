from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact , Comment , Appointment
# Create your views here.


def index_page(request : HttpRequest):

 return render(request, "main/index.html")


def contact_me (request : HttpRequest):
      if request.method == "POST":
        new_contact = Contact(name= request.POST["name"], email = request.POST["email"],  content = request.POST["content"], subject = request.POST["subject"])
        new_contact.save()
        
        return redirect("main:contact")


      return render(request, "main/contact.html")

def about (request : HttpRequest):

    return render (request,"main/about.html")


def details (request : HttpRequest):
    comments=Comment.objects.all()
    if request.method == "POST":
        new_comment = Comment(name = request.POST["name"], comment= request.POST["comment"])
        new_comment.save()
        return redirect("main:details")
    return render (request,"main/details.html", {"comments":comments})
    

    return render (request,"main/details.html")


def clinic (request : HttpRequest):

    return render (request,"main/clinic.html")

def doctors (request : HttpRequest):

    return render (request,"main/doctors.html")


def add_clinic(request : HttpRequest):

    if not request.user.is_staff:
        return redirect("accounts:login_user")

    if request.method == "POST":
        #to add a new entry
        new_clinic = Post(title= request.POST["title"], pcontent = request.POST["pcontent"], release_date = request.POST["release_date"], image = request.FILES["img"])
        new_clinic.save()
        return redirect("main:clinic")


    return render(request,"main/addclinic.html")



def clinic_detail(request : HttpRequest, clinic_id):

    clinic = Post.objects.get(id=clinic_id)


    return render(request, "main/details.html", {"clinic" : clinic})