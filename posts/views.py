from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Posts
from datetime import datetime
# Create your views here.
def index(req):
    posts = Posts.objects.all()
    return render(req,'index.html',{'posts':posts})

def post(req,pk):
    posts = Posts.objects.get(id=pk)
    return render(req,'posts.html',{'posts':posts})

<<<<<<< HEAD
=======
def add_review(req):
    if(req.method == 'POST'):
        title = req.POST['title']
        body = req.POST['body']

        post = Posts(title=title,body=body)
        post.save() # save into db
        return render(req,'index.html')
        
    return render(req,'write.html')
    # return render(req,'index.html')
>>>>>>> sub_branch

def blogpost(req):
    if(req.method == 'POST'):
        title = req.POST.get('title')
        body = req.POST.get('body') 
        post = Posts(title=title,body=body)
        print(title)
        print(body)
        post.save()
        return redirect('/')
    return render(req,'write.html')
          
        