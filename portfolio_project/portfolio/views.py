from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Lesson, Post, Contact, HomePageContent

def home(request):
    home_content = HomePageContent.objects.first()
    projects = Project.objects.all()[:6]
    skills = Skill.objects.all()
    lessons = Lesson.objects.all()[:3]
    posts = Post.objects.all()[:3]
    
    context = {
        'home_content': home_content,
        'projects': projects,
        'skills': skills,
        'lessons': lessons,
        'posts': posts,
    }
    return render(request, 'portfolio/home.html', context)

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': all_projects})

def skills(request):
    all_skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': all_skills})

def lessons(request):
    all_lessons = Lesson.objects.all()
    return render(request, 'portfolio/lessons.html', {'lessons': all_lessons})

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'portfolio/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            message=message_text
        )
        
        subject = f'New Contact Message from {name}'
        message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'portfolio/contact.html')
