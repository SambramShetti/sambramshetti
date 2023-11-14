from django.shortcuts import render, redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")
        strength = request.POST.get("strength","")
        project = request.POST.get("project","")
        address = request.POST.get("address","")
        nationalityy = request.POST.get("nationalityy","")
        blood_group = request.POST.get("blood_group","")
        date = request.POST.get("date","")
        place = request.POST.get("place","")
        dob = request.POST.get("dob","")

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills,
                         strength=strength, project=project, address=address, nationalityy=nationalityy, blood_group=blood_group, date=date, place=place, dob=dob)
        profile.save()
        return redirect('list')
    return render(request, 'resume/profile.html')

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    skills = user_profile.skills.split(',')
    previous_work = user_profile.previous_work.split(',')

    # return render(request, "cv/cv.html", {"user_profile":user_profile})
    template = loader.get_template("resume/cv.html") # we are loading our cv.html template here
    context = {
        "user_profile": user_profile,
        "skills": skills,
        "previous_work": previous_work,
    }
    html = template.render(context)
    options = {
        # 'page_size':'Letter',
        'encoding':"UTF-8"
    }
    pdf_config = pdfkit.configuration(wkhtmltopdf=r'C:\wkhtmltox\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options=options, configuration=pdf_config)
    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request, 'resume/list.html', {'profiles':profiles})




    