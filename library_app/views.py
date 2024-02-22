from django.shortcuts import render

# Create your views here.
def home(request):
    book1 = {"title":"Book1",'author':'Author1','subject':'Friction'}
    book2 = {"title":"Book2",'author':'Author2','subject':'Surface Tension'}
    context = {
        'book1':book1,
        'book2':book2,
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def books(request):
    books = [
        {"title":"Book1",'author':'Author1','Subject':'Friction1'},
        {"title":"Book2",'author':'Author2','Subject':'Friction2'},
        {"title":"Book3",'author':'Author3','Subject':'Friction3'},
        {"title":"Book4",'author':'Author4','Subject':'Friction4'},
    ]
    return render(request,'books.html',{'books':books})

