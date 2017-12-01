from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail', views.teach_detail, name="teach_detail"),
    url(r'^teacher_introducton', views.teacher_introduction, name="teacher_introduction"),
    url(r'^edit_schedule', views.edit_schedule, name="edit_schedule"),
    url(r'^check_notice/$', views.check_notice, name="check_notice"),
    url(r'^upload_classware', views.upload_classware, name="upload_classware"),
    url(r'^download_classware', views.download_classware, name="download_classware"),
    url(r'^delete_classware', views.delete_classware, name="delete_classware"),
    url(r'^check_homework', views.check_homework, name="check_homework"),
    url(r'^assignHomework/$', views.assign_homework, name="assign_homework"),
    url(r'^editHomework/$', views.edit_homework, name="editHomework"),
    url(r'^makeAnnouncement/$', views.make_announcement, name="makeAnnouncement"),
    url(r'^uploadVideo/$', views.upload_video, name="uploadVideo"),
    url(r'^watchVideo/$', views.watch_video, name="watchVideo")
]
