from django.shortcuts import render
from .models import Job, Position

def index(request):
    if request.method == 'POST':
        data = request.POST
        position = Position(designation = data['job_title'])
        position.save()
        position_object = Position.objects.get(id=position.id)
        if request.FILES['file_upload']:
            Job.objects.create(position=position_object, name=data['name'], email=data['email'], location=data['location'],
                                phone=data['phone'], college=data['college'], graduation_year=data['graduation_year'],
                                skills=data['skills'], github=data['Github'], linkedin=data['LinkedIn'], expectations=data['expectations'],
                                availability=data['availability'], resume=request.FILES['file_upload'])
        else:
            Job.objects.create(position=position_object, name=data['name'], email=data['email'], location=data['location'],
                                phone=data['phone'], college=data['college'], graduation_year=data['graduation_year'],
                                skills=data['skills'], github=data['Github'], linkedin=data['LinkedIn'], expectations=data['expectations'],
                                availability=data['availability'])

    return render(request, 'main_app/index.html',{})
