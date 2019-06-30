import os

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from main_app.forms import GroupForm
from main_app.models import Group, ScheduleChanges
from django.utils import timezone


def index(request):
    if request.method == 'GET':
        return render(request, 'main_app/index.html')

    elif request.method == 'POST':
        group_form = GroupForm(request.POST)

        if group_form.is_valid():
            current_group = Group.objects.filter(
                group_number=group_form.data['group_number'])

            try:
                current_schedule = ScheduleChanges.objects.get(
                    group_number__group_number=group_form.data['group_number'])
            except ObjectDoesNotExist as e:
                return render(request, 'main_app/index.html')

            if current_group:
                print('valid:', group_form.data['group_number'])
                print(current_schedule.schedule.path)
                file_path = current_schedule.schedule.path
                with open(file_path, 'rb') as schedule_file:
                    response = HttpResponse(
                        schedule_file.read(),
                        content_type='application/vnd.ms-excel'
                    )
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                    return response
            else:
                return HttpResponse(status=404)

            return render(request, 'main_app/index.html')

        else:
            return render(request, 'main_app/index.html')

    return HttpResponse(status=405)


def publication_date(request):
    if request.method == 'POST':
        group_form = GroupForm(request.POST)

        if group_form.is_valid():
            group = ScheduleChanges.objects.get(
                group_number__group_number=group_form.data['group_number'])

            day_time = group.publication_date
            day = day_time.strftime("%A %d %B")
            time = day_time.strftime("%H:%M")
            print(group.publication_date)
            return JsonResponse({
                'day': day,
                'time': time,
            }, safe=False)

        return render(request, 'main_app/index.html')

    return HttpResponse(status=405)
