from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.utils.crypto import get_random_string
from django.contrib import messages



################################################################### Department Representative Module ##################################################

################ Add off stage Participants #############

def add_off_stage_participants(request):

    obj=off_stage_event_table.objects.all()

    if request.method == 'POST':

        form=off_stage_participants_form(request.POST)
        get_name=request.POST.get("participant_name")
        get_group=request.POST.get("group")
        get_event=request.POST.get("event")

        if not off_stage_participant_table.objects.filter(participant_name=get_name,group=get_group,event=get_event).exists():

            if form.is_valid():
                obj=form.save(commit=True)
                obj.application_number="ARTS"+get_random_string(8)
                application_number_temp=obj.application_number
                obj.save()
                return render(request,'dept_rep/message.html',{"number":application_number_temp})
        else:
            messages.error(request,"This Participant has been already registered")
    else:
        form=off_stage_participants_form()


    return render(request,'dept_rep/add_off_stage_participants.html',{"off_stage_items":obj})


################ Add on stage Participants #############

def add_on_stage_participants(request):

    obj=on_stage_event_table.objects.all()

    if request.method == 'POST':

        form=on_stage_participants_form(request.POST)
        get_name=request.POST.get("participant_name")
        get_group=request.POST.get("group")
        get_event=request.POST.get("event")

        if not on_stage_participant_table.objects.filter(participant_name=get_name,group=get_group,event=get_event).exists():

            if form.is_valid():
                obj=form.save(commit=True)
                obj.application_number="ARTS"+get_random_string(8)
                application_number_temp=obj.application_number
                obj.save()
                return render(request,'dept_rep/message.html',{"number":application_number_temp})
        else:
            messages.error(request,"This Participant has been already registered")
    else:
        form=on_stage_participants_form()


    return render(request,'dept_rep/add_on_stage_participants.html',{"on_stage_items":obj})


################### add off stage appeal ############

def add_off_stage_appeal(request):

    obj=off_stage_event_table.objects.all()

    if request.method == 'POST':

        form=off_stage_appeal_form(request.POST)
        get_name=request.POST.get("participant_name")
        get_group=request.POST.get("group")
        get_event=request.POST.get("event")

        if not off_stage_appeal_table.objects.filter(participant_name=get_name,group=get_group,event=get_event).exists():

            if form.is_valid():
                obj=form.save(commit=True)
                obj.application_number="ARTSAPPEAL"+get_random_string(8)
                application_number_temp=obj.application_number
                obj.status="Under Consideration"
                obj.save()
                return render(request,'dept_rep/message.html',{"number":application_number_temp})
        else:
            messages.error(request,"This appeal has been already registered")
    else:
        form=off_stage_appeal_form()


    return render(request,'dept_rep/add_off_stage_appeal.html',{"off_stage_items":obj})


################### add on stage appeal ############

def add_on_stage_appeal(request):

    obj=on_stage_event_table.objects.all()

    if request.method == 'POST':

        form=on_stage_appeal_form(request.POST)
        get_name=request.POST.get("participant_name")
        get_group=request.POST.get("group")
        get_event=request.POST.get("event")

        if not on_stage_appeal_table.objects.filter(participant_name=get_name,group=get_group,event=get_event).exists():

            if form.is_valid():
                obj=form.save(commit=True)
                obj.application_number="ARTSAPPEAL"+get_random_string(8)
                application_number_temp=obj.application_number
                obj.status="Under Consideration"
                obj.save()
                return render(request,'dept_rep/message.html',{"number":application_number_temp})
        else:
            messages.error(request,"This appeal has been already registered")
    else:
        form=on_stage_appeal_form()


    return render(request,'dept_rep/add_on_stage_appeal.html',{"on_stage_items":obj})

    

################## display thank you message #############################

def display_thank_you(request):

    if request.method == "POST":

        return redirect('participants_on_stage_add')

    return render(request,'dept_rep/message.html')





###################################################################################################################################################