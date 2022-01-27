from django import forms
from .models import *


################################################################# Admin Module ############################################################

##################### adding officilas form ###################

class add_officials_form(forms.ModelForm):

    class Meta:
        model=officilas_table
        fields=['username','password','role']



###################### on stage result form ##########################

class on_stage_result_form(forms.ModelForm):
    
    class Meta:
        model=on_stage_result_table
        fields=['name','position','group','event']


######################  off stage result form ###########################

class off_stage_result_form(forms.ModelForm):

    class Meta:
        model=off_stage_result_table
        fields=['name','position','group','event']



######################## scoreboard form ######################

class scoreboard_form(forms.ModelForm):

    class Meta:
        model=score_board
        fields=['group1_score','group2_score','group3_score','group4_score','group5_score','group6_score']



######################## gallery form #########################

class gallery_image_form(forms.ModelForm):

    class Meta:
        model=gallery_images
        fields=['image1','image2','image3','image4','image5','image6','image7','image8']


###########################################################################################################################################



################################################################## Department Representative Module ########################################

################## On stage items add appeal forms ########

class on_stage_appeal_form(forms.ModelForm):

    class Meta:
        model=on_stage_appeal_table
        fields=['participant_name','group','registration_number','event','appeal_description']


################## Off stage items add appeal forms ########

class off_stage_appeal_form(forms.ModelForm):

    class Meta:
        model=off_stage_appeal_table
        fields=['participant_name','group','registration_number','event','appeal_description']


################## Off stage items add participant forms ########

class off_stage_participants_form(forms.ModelForm):

    class Meta:
        model=off_stage_participant_table
        fields=['participant_name','group','registration_number','event']

################## On stage items add participant forms ########

class on_stage_participants_form(forms.ModelForm):

    class Meta:
        model=on_stage_participant_table
        fields=['participant_name','group','registration_number','event']


############################################################################################################################################




###################################################################### Program Commitee  Module ##########################################

################# on stage items form #####################

class on_stage_event_form(forms.ModelForm):

    class Meta:
        model=on_stage_event_table
        fields=['event_name','day','stage','event_start_time','event_end_time','image1','event_details']


################### off stage items form ###################

class off_stage_event_form(forms.ModelForm):
    
    class Meta:
        model=off_stage_event_table
        fields=['event_name','day','venue','event_start_time','event_end_time','image1','event_details']

###########################################################################################################################################

####################################################################### Media Module #####################################################

######################## add news form #####################

class add_news_form(forms.ModelForm):

    class Meta:
        model=news
        fields=['reporter_name','channel_name','heading','image1','image2','image3','image4','news_details']


######################## add program form #####################

class add_program_form(forms.ModelForm):

    class Meta:
        model=live_coverage
        fields=['reporter_name','channel_name','heading','video1','video_details']



################################################################################################################################################