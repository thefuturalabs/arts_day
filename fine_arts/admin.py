from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
# Register your models here.


################################################################## Admin Module ###############################################################

################### add officials #######################

def add_officials(request):
    
    if request.method == "POST":

        get_username=request.POST.get("username")
        get_password=request.POST.get("password")
        get_role=request.POST.get("role")

        if not officilas_table.objects.filter(username=get_username,password=get_password,role=get_role).exists():


            form=add_officials_form(request.POST)

            if form.is_valid():

                form.save()
            else:
                form=add_officials_form()
        else:
            messages.info(request,"Already added Member")


    return render(request,'admin/add_officials.html')

################### view officials details ###############

def view_officials(request):

    obj=officilas_table.objects.all()

    req_id=request.POST.get("id")

    try:
        obj_delete=officilas_table.objects.get(id=req_id)
    
    except officilas_table.DoesNotExist:

        obj_delete=None
    
    if request.method == "POST":

        obj_delete.delete()

    return render(request,'admin/View_offcials.html',{"officials_details":obj})


################### display Admin Dash board ###############

def admin_home(request):

    return render(request,'admin/admin_homepage.html')


##################### update off stage appeal status ################

def update_off_stage_appeal_status(request):

    obj_off_stage=off_stage_appeal_table.objects.all().order_by('-id')
    

    context={
        "off_stage_appeals":obj_off_stage,
        
    }

    req_id=request.POST.get("id")

    try:
        obj_update=off_stage_appeal_table.objects.get(id=req_id)
        
    
    except off_stage_appeal_table.DoesNotExist:
        obj_update=None
    
    

    if request.method == "POST":

        get_updates=request.POST.get("update")
        obj_update.status=get_updates
        obj_update.save()


    return render(request,'admin/update_off_stage_appeal_status.html',context)

################################## View Off stage Appeal Details ###################

def view_off_stage_appeal(request,off_stage_appeal_id):

    obj=off_stage_appeal_table.objects.get(id=off_stage_appeal_id)


    return render(request,'admin/view_off_stage_appeal_details.html',{"appeal_details":obj})


##################### update on stage appeal status ################

def update_on_stage_appeal_status(request):

    obj_on_stage=on_stage_appeal_table.objects.all().order_by('-id')
    

    context={
        "on_stage_appeals":obj_on_stage,
        
    }

    req_id=request.POST.get("id")

    try:
        obj_update=on_stage_appeal_table.objects.get(id=req_id)
        
    
    except on_stage_appeal_table.DoesNotExist:
        obj_update=None
    
    

    if request.method == "POST":

        get_updates=request.POST.get("update")
        obj_update.status=get_updates
        obj_update.save()


    return render(request,'admin/update_on_stage_appeal_status.html',context)

################################## View On stage Appeal Details ###################

def view_on_stage_appeal(request,on_stage_appeal_id):

    obj=on_stage_appeal_table.objects.get(id=on_stage_appeal_id)


    return render(request,'admin/view_on_stage_appeal_details.html',{"appeal_details":obj})







################## Upload Gallery Images ###############

def admin_upload_images(request):

    if request.method == "POST":

        form=gallery_image_form(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        else:
            form=gallery_image_form()

    return render(request,'admin/add_images.html')


###################### Delete Images ###################

def admin_delete_uploaded_images(request):

    if request.method == "POST" and 'back_btn' in request.POST:

        return redirect('view_home_admin')
    
    if request.method == "POST" and 'delete_btn' in request.POST:

        obj=gallery_images.objects.all()
        obj.delete()

        return redirect('view_home_admin')


######################### Add score ########################

def add_score(request):

    if request.method =='POST':

        form=scoreboard_form(request.POST)

        if form.is_valid():

            form.save()
        else:

            form=scoreboard_form()


    return render(request,'admin/add_score.html')

###################### Delete score ###################

def remove_score(request):

    if request.method == "POST" and 'back_btn' in request.POST:

        return redirect('view_home_admin')
    
    if request.method == "POST" and 'delete_btn' in request.POST:

        obj=score_board.objects.all()
        obj.delete()

        return redirect('view_home_admin')

    return render(request,'admin/remove_score.html')



################################ View off stage participants ##################

def view_off_stage_participants(request):

    obj=off_stage_participant_table.objects.all().order_by('-id')

    req_id=request.POST.get("id")

    try:
        obj_delete=off_stage_participant_table.objects.get(id=req_id)
    
    except off_stage_participant_table.DoesNotExist:
        obj_delete=None

    if request.method == "POST":

        obj_delete.delete()

    return render(request,'admin/View_off_stage_participants.html',{"off_stage_participants_details":obj})


################################ View on stage participants ##################

def view_on_stage_participants(request):

    obj=on_stage_participant_table.objects.all().order_by('-id')

    req_id=request.POST.get("id")

    try:
        obj_delete=on_stage_participant_table.objects.get(id=req_id)
    
    except on_stage_participant_table.DoesNotExist:
        obj_delete=None

    if request.method == "POST":

        obj_delete.delete()

    return render(request,'admin/View_on_stage_participants.html',{"on_stage_participants_details":obj})


###################################### Update off stage results ###############################


def update_off_stage_results(request):

    obj=off_stage_event_table.objects.all()

    if request.method =="POST":

        form=off_stage_result_form(request.POST)

        if form.is_valid():

            form.save()
        else:

            form=off_stage_result_form()


    return render(request,'admin/update_off_stage_result.html',{"off_stage_details":obj})


###################################### Update on stage results ###############################


def update_on_stage_results(request):

    obj=on_stage_event_table.objects.all()

    if request.method =="POST":

        form=on_stage_result_form(request.POST)

        if form.is_valid():

            form.save()
        else:

            form=on_stage_result_form()


    return render(request,'admin/update_on_stage_result.html',{"on_stage_details":obj})



########################## view off stage result ##########################

def view_off_stage_result(request):
    
    obj=off_stage_result_table.objects.all().order_by('-id')

    req_id=request.POST.get("id")

    try:
        obj_delete=off_stage_result_table.objects.get(id=req_id)
    
    except off_stage_result_table.DoesNotExist:
        obj_delete=None

    if request.method == "POST":

        obj_delete.delete()


    return render(request,'admin/View_off_stage_result.html',{"off_stage_results":obj})

########################## view on stage result ##########################

def view_on_stage_result(request):
    
    obj=on_stage_result_table.objects.all().order_by('-id')

    req_id=request.POST.get("id")

    try:
        obj_delete=on_stage_result_table.objects.get(id=req_id)
    
    except on_stage_result_table.DoesNotExist:
        obj_delete=None

    if request.method == "POST":

        obj_delete.delete()


    return render(request,'admin/View_on_stage_result.html',{"on_stage_results":obj})




   

###############################################################################################################################################