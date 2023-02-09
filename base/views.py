from django.shortcuts import render, redirect
from Resume import settings
from django.http import HttpResponse
from .models import Post, Projects, Comment, Contact
import random
from django.contrib import messages



def index(request):
    posts =Post.objects.all()
    projects =Projects.objects.all()
    comment = Comment.objects.all()
    
    contact = Contact()
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.subject = request.POST['subject']
        contact.message = request.POST['message']
        contact.save()
        messages.success(request, "Thanks for contacting me i will be in touch!")


            
        return redirect('/#contact-section')
    
    return render(request, 'index.html',{'posts': posts, 'projects': projects, 'comment':comment})

def index1(request):
    
    return render(request, 'index1.html')

def single(request, pk):
    projects =Projects.objects.get(id=pk)
    count = projects.comment_set.count()

    comments = projects.comment_set.all()
    comment = Comment()
    if request.method == 'POST':
        comment.name = request.POST['name']
        comment.email = request.POST['email']
        comment.body = request.POST['body']
        comment.number = str(random.randint(1,10)) + ".png"
        comment.project = Projects.objects.get(id=pk)
        comment.save()
    return render(request, 'single.html',{'projects': projects, 'comments':comments, 'comment':count})



def download_file(request):
    file = open(str(settings.BASE_DIR) + "/Resume/files/cv_ait_mlouk_ismail.pdf", 'rb')
    response = HttpResponse(file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv_ait_mlouk_ismail.pdf"'
    return response
