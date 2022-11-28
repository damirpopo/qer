from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request,"about.html")

def contacts(request):
     contacts={
        "tel" : "+79991627885",
        "mail" : "misterdamir5@gmail.com"
    }
     return render(request,"contacts.html", context={"contacts": contacts})
def form(request):
    return render(request,"form.html")