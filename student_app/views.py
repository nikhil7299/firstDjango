from django.shortcuts import render

# Create your views here.
def student_list(request):
    students = [
        {"name":"Sam","age":20 ,"grade":'A'},
        {"name":"Kane","age":21 ,"grade":'B'},
        {"name":"Alice","age":23 ,"grade":'A+'},

    ]
    return render(request,'student_list.html',{'students':students})
