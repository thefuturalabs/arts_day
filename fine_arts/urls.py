from django.urls import path
from .import user
from .import news
from .import program_commitee
from .import department_rep
from .import admin
from .import sign_in



urlpatterns = [


    ######################################################################## Sign in Page ########################################################

    path('load_sign_in_page',sign_in.display_sign_in,name="sign_in_display"),

    ##############################################################################################################################################

    ######################################################################### Admin Module #######################################################

    ############################### add officials #########################################

    path('admin_add_officials',admin.add_officials,name="officilas_add"),

    ############################## view officials ########################################

    path('admin_view_officials',admin.view_officials,name="officials_view"),

    ############################## Appeal updates off stage #################################

    path('admin_update_off_stage_appeal_status',admin.update_off_stage_appeal_status,name='appeal_status_off_stage'),

    ############################# view off stage appeal details ##############################

    path('admin_view_off_stage_appeal_details<int:off_stage_appeal_id>',admin.view_off_stage_appeal,name='off_stage_appeal_details_view'),

    ############################## Appeal updates on stage #################################

    path('admin_update_on_stage_appeal_status',admin.update_on_stage_appeal_status,name='appeal_status_on_stage'),

    ############################# view off stage appeal details ##############################

    path('admin_view_on_stage_appeal_details<int:on_stage_appeal_id>',admin.view_on_stage_appeal,name='on_stage_appeal_details_view'),


    ############################## View off stage participants #################################

    path('admin_view_off_stage_participants',admin.view_off_stage_participants,name='view_participants_off_stage'),

    ############################## View on stage participants #################################

    path('admin_view_on_stage_participants',admin.view_on_stage_participants,name='view_participants_on_stage'),

    ############################## Update off stage Results ###########################################

    path('admin_update_off_stage_results',admin.update_off_stage_results,name='result_off_stage__update'),

    ############################## Update on stage Results ###########################################

    path('admin_update_on_stage_results',admin.update_on_stage_results,name='result_on_stage__update'),

    ############################## view off stage result updates #####################################

    path('admin_view_off_stage_results',admin.view_off_stage_result,name='off_stage_result_view'),

    ############################## view on stage result updates #####################################

    path('admin_view_on_stage_results',admin.view_on_stage_result,name='on_stage_result_view'),


    ############################## display admin home page ##########################

    path('admin_view_home',admin.admin_home,name="view_home_admin"),

    ############################# Upload Images ####################################

    path('admin_add_images',admin.admin_upload_images,name='images_upload'),

    ############################# Delete uploaded Images ###########################

    path('admin_remove_images',admin.admin_delete_uploaded_images,name='images_delete'),

    ############################## Add score ########################################

    path('admin_add_score',admin.add_score,name='add_score_admin'),

    ############################## Remove Score #####################################

    path('admin_remove_score',admin.remove_score,name="admin_remove"),

    

    ###############################################################################################################################################

    ######################################################################### User Module ########################################################
    
    ############### view homepage ##########################

    path('',user.display_home,name='home_display'),

    ###################### view news details ################

    path('user_news_details<int:news_id>',user.user_view_news_details,name='detail_news_user'),

    ###################### view program #####################

    path('user_view_program',user.view_program,name='program_view'),

    ####################### view results #####################

    path('user_view_results',user.view_results,name='result_view'),

    ################################################################# Participant section #########################################################

    ######################## Participants Home #############################

    path('view_participant_home',user.participant_home,name="home_participant"),

    ######################### Participant View Appeal status #################

    path('participant_view_appeal_status',user.view_appeal_status,name="appeal_view"),

    ######################## participants view results #########################

    path('participants_view_results',user.view_program_results,name="result_view"),


    ###############################################################################################################################################


    ######################################################################### Department Representative ###########################################

    ################### on stage items appeal #####################

    path('dep_rep_add_on_stage_appeal',department_rep.add_on_stage_appeal,name="appeal_on_stage"),


    ################### off stage items appeal #####################

    path('dep_rep_add_off_stage_appeal',department_rep.add_off_stage_appeal,name="appeal_off_stage"),

    ################# off stage items add participants ##############

    path('dept_rep_add_off_stage_participants',department_rep.add_off_stage_participants,name="participants_off_stage_add"),

    ################# on stage items add participants ##############

    path('dept_rep_add_on_stage_participants',department_rep.add_on_stage_participants,name="participants_on_stage_add"),

    #################################################################################################################################################





    ######################################################################## Program Commitee Module ##############################################

    ######################### Add On Stage Events #########################

    path('program_commitee_add_on_stage_event',program_commitee.add_on_stage_events,name='event_add_on_stage'),

    ######################### Add Off Stage Events #########################

    path('program_commitee_add_off_stage_event',program_commitee.add_off_stage_events,name='event_add_off_stage'),

    ######################### Manage on stage evenets ######################

    path('program_commitee_manage_on_stage_event',program_commitee.edit_on_stage_event,name='edit_on_stage'),

    ######################### Manage off stage evenets ######################

    path('program_commitee_manage_off_stage_event',program_commitee.edit_off_stage_event,name='edit_off_stage'),





    ###############################################################################################################################################

    ########################################################################## Media Module ########################################################

    
    ###################### add news ########################

    path('media_add_news',news.add_news,name='news_add'),

    ###################### view updated news ###############

    path('view_news',news.view_news_updates,name='news_view'),

    ###################### view news details ################

    path('news_details<int:news_id>',news.view_news_details,name='detail_news'),

    ####################### add program videos ################

    path('news_updater_add_program_video',news.update_program_coverage,name='program_video_update'),


    ##################################################################################################################################################
]
