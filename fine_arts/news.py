from django.shortcuts import render
from .forms import *



############################################################# Media Module #####################################################################



################## Add News ###################

def add_news(request):

    if request.method == 'POST':
        form=add_news_form(request.POST,request.FILES)

        if form.is_valid():

            form.save()
        else:
            form=add_news_form()



    return render(request,'news/add_news.html')


###################### View News updates #############

def view_news_updates(request):

    obj=news.objects.all().order_by('-id')

    return render(request,'news/view_updted_news.html',{'news_update':obj})

################### view details of news ##############

def view_news_details(request,news_id):

    obj=news.objects.get(id=news_id)

    return render(request,'news/view_news_details.html',{'news_updates':obj})


########################### add program #####################

def update_program_coverage(request):

    if request.method == 'POST':
        form=add_program_form(request.POST,request.FILES)

        if form.is_valid():

            form.save()
        else:
            form=add_program_form()

    return render(request,'news/add_program.html')



###############################################################################################################################################