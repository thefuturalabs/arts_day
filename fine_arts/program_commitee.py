from django.shortcuts import render
from .forms import *


############################################################# Program Commitee Module ######################################################

################### Function to add on stage  Events ###############

def add_on_stage_events(request):

    if request.method =='POST':

        form=on_stage_event_form(request.POST,request.FILES)

        if form.is_valid():

            form.save()
        
        else:
            form=on_stage_event_form()


    return render(request,'program_commitee/add_on_stage_event.html')


################### Function to add off stage  Events ###############

def add_off_stage_events(request):

    if request.method =='POST':
    
        form=off_stage_event_form(request.POST,request.FILES)

        if form.is_valid():

            form.save()
        
        else:
            form=on_stage_event_form()


    return render(request,'program_commitee/add_off_stage_event.html')


############################### Manage on stage Events #########################

def edit_on_stage_event(request):

    obj=on_stage_event_table.objects.all().order_by('event_start_time')

    get_id=request.POST.get("id")

    try:
        obj_delete=on_stage_event_table.objects.filter(id=get_id)
    
    except on_stage_event_table.DoesNotExist:
        obj_delete=None

    
    if request.method == "POST":

        obj_delete.delete()
    

   

    return render(request,'program_commitee/manage_on_stage_event.html',{"on_stage_details":obj})


############################### Manage off stage Events #########################

def edit_off_stage_event(request):

    obj=off_stage_event_table.objects.all().order_by('event_start_time')

    get_id=request.POST.get("id")

    try:
        obj_delete=off_stage_event_table.objects.filter(id=get_id)
    
    except off_stage_event_table.DoesNotExist:
        obj_delete=None

    
    if request.method == "POST":

        obj_delete.delete()
    

   

    return render(request,'program_commitee/manage_off_stage_event.html',{"off_stage_details":obj})





##############################################################################################################################################