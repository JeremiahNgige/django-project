from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author':'Jeremiha',
        'title':'Django',
        'content':'First time using django',
        'date_posted':'25-5-2020', 
    },
    {
        'author':'Anita',
        'title':'Django',
        'content':'Django on the way',
        'date_posted':'25-5-2020',
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
