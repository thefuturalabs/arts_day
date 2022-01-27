from django.db import models

# Create your models here.


######################################################################### Admin Module #############################################################

################## officials registration table #############

class officilas_table(models.Model):
    username=models.CharField(max_length=500)
    password=models.CharField(max_length=500)
    role=models.CharField(max_length=250)



################## on stage Result Table ########################

class on_stage_result_table(models.Model):
    name=models.CharField(max_length=500)
    position=models.CharField(max_length=250)
    group=models.CharField(max_length=250)
    event=models.CharField(max_length=500)


################## off stage Result Table ########################

class off_stage_result_table(models.Model):
    name=models.CharField(max_length=500)
    position=models.CharField(max_length=250)
    group=models.CharField(max_length=250)
    event=models.CharField(max_length=500)



##################### gallery images table ################

class gallery_images(models.Model):
    image1=models.ImageField(upload_to='gallery_images')
    image2=models.ImageField(upload_to='gallery_images')
    image3=models.ImageField(upload_to='gallery_images')
    image4=models.ImageField(upload_to='gallery_images')
    image5=models.ImageField(upload_to='gallery_images')
    image6=models.ImageField(upload_to='gallery_images')
    image7=models.ImageField(upload_to='gallery_images')
    image8=models.ImageField(upload_to='gallery_images')

####################### table to store score ##############

class score_board(models.Model):
    group1_score=models.IntegerField()
    group2_score=models.IntegerField()
    group3_score=models.IntegerField()
    group4_score=models.IntegerField()
    group5_score=models.IntegerField()
    group6_score=models.IntegerField()

####################################################################################################################################################



######################################################################### Department Representative Module ##########################################

################ off stage items appeal table ###############

class off_stage_appeal_table(models.Model):

    participant_name=models.CharField(max_length=500)
    group=models.CharField(max_length=50)
    registration_number=models.CharField(max_length=250)
    event=models.CharField(max_length=1000)
    application_number=models.CharField(max_length=250)
    appeal_description=models.CharField(max_length=50000)
    status=models.CharField(max_length=500)

################ on stage items appeal table ###############

class on_stage_appeal_table(models.Model):

    participant_name=models.CharField(max_length=500)
    group=models.CharField(max_length=50)
    registration_number=models.CharField(max_length=250)
    event=models.CharField(max_length=1000)
    application_number=models.CharField(max_length=250)
    appeal_description=models.CharField(max_length=50000)
    status=models.CharField(max_length=500)


################ off stage items participants table ###############

class off_stage_participant_table(models.Model):

    participant_name=models.CharField(max_length=500)
    group=models.CharField(max_length=50)
    registration_number=models.CharField(max_length=250)
    event=models.CharField(max_length=1000)
    application_number=models.CharField(max_length=250)
    

################ on stage items participants table ###############

class on_stage_participant_table(models.Model):

    participant_name=models.CharField(max_length=500)
    group=models.CharField(max_length=50)
    registration_number=models.CharField(max_length=250)
    event=models.CharField(max_length=1000)
    application_number=models.CharField(max_length=250)
   




#################################################################################################################################################








###################################################################### Program Commitee Module #################################################



##################### Table to store On stage items ###########

class on_stage_event_table(models.Model):

    event_name=models.CharField(max_length=500)
    day=models.CharField(max_length=50)
    stage=models.CharField(max_length=50)
    event_start_time=models.TimeField(auto_now=False, auto_now_add=False)
    event_end_time=models.TimeField(auto_now=False, auto_now_add=False)
    image1=models.ImageField(upload_to='event_images')
    event_details=models.CharField(max_length=3000)

##################### Table to store On stage items ###########

class off_stage_event_table(models.Model):

    event_name=models.CharField(max_length=500)
    day=models.CharField(max_length=50)
    venue=models.CharField(max_length=500)
    event_start_time=models.TimeField(auto_now=False, auto_now_add=False)
    event_end_time=models.TimeField(auto_now=False, auto_now_add=False)
    image1=models.ImageField(upload_to='event_images')
    event_details=models.CharField(max_length=3000)
    

################################################################################################################################################

###################################################################### Media Module ############################################################


################### Table to store news ##################

class news(models.Model):

    reporter_name=models.CharField(max_length=250)
    channel_name=models.CharField(max_length=250)
    heading=models.CharField(max_length=1000)
    image1=models.ImageField(upload_to='news_images')
    image2=models.ImageField(upload_to='news_images')
    image3=models.ImageField(upload_to='news_images')
    image4=models.ImageField(upload_to='news_images')
    news_details=models.CharField(max_length=100000)

################### Table to store program videos ##################

class live_coverage(models.Model):

    reporter_name=models.CharField(max_length=250)
    channel_name=models.CharField(max_length=250)
    heading=models.CharField(max_length=1000)
    video1=models.FileField(upload_to='live_coverage_media/%y')
    video_details=models.CharField(max_length=100000)




#################################################################################################################################################