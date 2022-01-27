from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.



#################################################################### User Module #####################################################################


################ function to display Homepage #############

def display_home(request):

    obj1=news.objects.all().order_by('id')
    obj_images=gallery_images.objects.all().first()
    obj_score=score_board.objects.all().first()

    ############### on stage items details ######################################
    obj_on_stage_day1=on_stage_event_table.objects.filter(day='day1').order_by('event_start_time')
    obj_on_stage_day2=on_stage_event_table.objects.filter(day='day2').order_by('event_start_time')
    obj_on_stage_day3=on_stage_event_table.objects.filter(day='day3').order_by('event_start_time')

    ################ off stage items details ##########################################
    obj_off_stage_day1=off_stage_event_table.objects.filter(day='day1').order_by('event_start_time')
    obj_off_stage_day2=off_stage_event_table.objects.filter(day='day2').order_by('event_start_time')
    obj_off_stage_day3=off_stage_event_table.objects.filter(day='day3').order_by('event_start_time')


    context={
        "news_updates":obj1,
        "images_uploads":obj_images,
        "score":obj_score,
        ############### on stage items details  ########### 
        "on_stage_items_day1":obj_on_stage_day1,
        "on_stage_items_day2":obj_on_stage_day2,
        "on_stage_items_day3":obj_on_stage_day3,

        ################## off stage items details ##########

        "off_stage_items_day1":obj_off_stage_day1,
        "off_stage_items_day2":obj_off_stage_day2,
        "off_stage_items_day3":obj_off_stage_day3,

    }

    return render(request,'user/homepage.html',context)


################### view details of news ##############

def user_view_news_details(request,news_id):

    obj=news.objects.get(id=news_id)

    return render(request,'user/view_news_details.html',{'news_updates':obj})



################# view program #######################

def view_program(request):

    obj=live_coverage.objects.all().order_by('-id')

    return render(request,'user/view_program.html',{"program_watch_details":obj})

################# view results #######################

def view_results(request):

    obj1=off_stage_result_table.objects.all()
    obj2=on_stage_result_table.objects.all()

    context={
        "off_stage_results":obj1,
        "on_stage_results":obj2,
    }

    return render(request,'user/results.html',context)

    


#############################################################################################################################################################



################################################################ Participant section ########################################################################

######################### Participant View results ############

def view_program_results(request):

    obj1=off_stage_event_table.objects.all()
    obj2=on_stage_event_table.objects.all()

    context={
        "off_stage_details":obj1,
        "on_stage_details":obj2
    }

    if request.method == "POST":
        
        get_event=request.POST.get("event")

        if off_stage_result_table.objects.filter(event=get_event).exists() or on_stage_result_table.objects.filter(event=get_event).exists():

            messages.info(request,"The results of the program")

            if off_stage_result_table.objects.filter(event=get_event).exists():

                obj3=off_stage_result_table.objects.filter(event=get_event)

                context={
                    "off_stage_details":obj1,
                    "on_stage_details":obj2,
                    "results":obj3
                }

                
                return render(request,'user/participants_view_result.html',context)
            else:
                obj4=on_stage_result_table.objects.filter(event=get_event)

                context={
                    "off_stage_details":obj1,
                    "on_stage_details":obj2,
                    "results":obj4
                }

                
                return render(request,'user/participants_view_result.html',context)



        
        else:
            messages.error(request,"No results found")





    return render(request,'user/participants_view_result.html',context)




######################## participant View appeal status ###############

def view_appeal_status(request):

    obj1=off_stage_event_table.objects.all()
    obj2=on_stage_event_table.objects.all()

    context={
        "off_stage_details":obj1,
        "on_stage_details":obj2
    }

    if request.method == "POST":

        get_name=request.POST.get("name")
        get_number=request.POST.get("app_number")
        get_event=request.POST.get("event")
        get_group=request.POST.get("group")

        if off_stage_appeal_table.objects.filter(participant_name=get_name,group=get_group,event=get_event,application_number=get_number).exists() or on_stage_appeal_table.objects.filter(participant_name=get_name,group=get_group,event=get_event,application_number=get_number).exists():
            
            messages.info(request,"Your appeal status : ")

            if off_stage_appeal_table.objects.filter(application_number=get_number).exists():

                obj3=off_stage_appeal_table.objects.get(application_number=get_number)
                get_status=obj3.status

                context={
                    "off_stage_details":obj1,
                    "on_stage_details":obj2,
                    "status":get_status
                }
                

                return render(request,'user/participants_view_appeal_status.html',context)
            else:
                
                obj4=on_stage_appeal_table.objects.get(application_number=get_number)
                get_status=obj4.status

                context={
                    "off_stage_details":obj1,
                    "on_stage_details":obj2,
                    "status":get_status
                }

                return render(request,'user/participants_view_appeal_status.html',context)

        else:
            messages.error(request,"No result found")    



    return render(request,'user/participants_view_appeal_status.html',context)







######################### participant view event schedule #########



def participant_home(request):

    obj1=off_stage_event_table.objects.all()
    obj2=on_stage_event_table.objects.all()

    context={
        "off_stage_details":obj1,
        "on_stage_details":obj2
    }

    if request.method == "POST":

        get_name=request.POST.get("name")
        get_number=request.POST.get("app_number")
        get_event=request.POST.get("event")
        get_group=request.POST.get("group")

        if on_stage_participant_table.objects.filter(participant_name=get_name,group=get_group,event=get_event,application_number=get_number).exists() or off_stage_participant_table.objects.filter(participant_name=get_name,group=get_group,event=get_event,application_number=get_number).exists():
            
            messages.info(request,"Your event details")

            if on_stage_event_table.objects.filter(event_name=get_event).exists():

                obj3=on_stage_event_table.objects.get(event_name=get_event)
                get_location=obj3.stage

                context={
                    "off_stage_details":obj1,
                    "on_stage_details":obj2,
                    "event_details":obj3,
                    "location":get_location
                }
                

                return render(request,'user/participants_home.html',context)
            else:
                
                obj4=off_stage_event_table.objects.get(event_name=get_event)
                get_location=obj4.venue
                context={
                    "off_stage_details":obj1,
                    "on_stage_details":obj2,
                    "event_details":obj4,
                    "location":get_location
                }

                return render(request,'user/participants_home.html',context)

        else:
            messages.error(request,"No result found")    



    return render(request,'user/participants_home.html',context)


##############################################################################################################################################################