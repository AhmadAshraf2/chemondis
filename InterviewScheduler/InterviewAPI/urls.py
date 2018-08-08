from django.conf.urls import url
from . import views

'''
routing rules for urls begining with /Interview/...
'''
urlpatterns = [
    url(r'^view/$', views.ViewAllSlots.as_view()),

    url(r'^create/$', views.CreateSlot.as_view(), name='create_slot'),

    url(r'^interviewslot/$', views.InterviewSlots.as_view(), name='interview_slots'),
]