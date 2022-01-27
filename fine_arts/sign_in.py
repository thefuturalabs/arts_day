from django.shortcuts import render,redirect
from .models import *


############################################################### sign in page #####################################################################################

def display_sign_in(request):

    if request.method == "POST":

        get_username=request.POST.get("username")
        get_password=request.POST.get("password")

        if get_username =="admin" and get_password == "admin":

            return redirect('view_home_admin')
        
        elif officilas_table.objects.filter(username=get_username,password=get_password,role='media').exists():

            return redirect('news_add')
        
        elif officilas_table.objects.filter(username=get_username,password=get_password,role='Department_rep').exists():
    
            return redirect('participants_off_stage_add')
        
        elif officilas_table.objects.filter(username=get_username,password=get_password,role='program_commitee').exists():
        
            return redirect('event_add_off_stage')

        elif off_stage_participant_table.objects.filter(participant_name=get_username,registration_number=get_password).exists() or on_stage_participant_table.objects.filter(participant_name=get_username,registration_number=get_password).exists() :

            return redirect('home_participant')

        

        else:
            return render(request,'error.html')

    return render(request,'signin.html')




#############################################################################################################################################################