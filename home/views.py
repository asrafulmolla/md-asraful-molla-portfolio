from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    from collections import defaultdict
    skill_groups = defaultdict(list)
    for skill in Skill.objects.all():
        skill_groups[skill.get_category_display()].append(skill.name)
    context = {
    'profile': Profile.objects.first(),
    'educations': Education.objects.all(),
    'experiences': Experience.objects.all(),
    'skills': Skill.objects.all(),
    'projects': Project.objects.all(),
    'problem_solving': ProblemSolving.objects.all(),
    'achievements': Achievement.objects.all(),
    'leaderships': Leadership.objects.all(),
    'certifications': Certification.objects.all(),
    'publications': Publication.objects.all(),
    'recommendations': Recommendation.objects.all(),
    'skill_groups': dict(skill_groups),
}
    return render(request, 'home/index.html', context)

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'home/blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'home/blog_detail.html', {'blog': blog})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to DB (optional)
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, "Your message has been sent!")
        return redirect('home') 
    
    return render(request, 'home/partials/contact.html') 

def gallery_list(request):
    gallery_items = Gallery.objects.all()
    return render(request, 'home/gallery.html', {'gallery_items': gallery_items})

def contact_submit(request):
    if request.method == "POST":
        # Process form
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        messages.success(request, "Message sent successfully!")
        return redirect('home')  # Redirect back to homepage
    else:
        # Optional: if someone visits /contact/ directly, redirect to home
        return redirect('home')