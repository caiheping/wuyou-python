from django.conf.urls import url
from resumes.views import ShowResumeView, ResumeView, ResumeWorkingView, ResumeEducationView, ResumeJobView, ResumeProjectExperienceView

urlpatterns = [
    url(r'^show_resume$', ShowResumeView.as_view(), name='show_resume'),
    url(r'^resume$', ResumeView.as_view(), name='resume'),
    url(r'^resumeWorking$', ResumeWorkingView.as_view(), name='resumeWorking'),
    url(r'^resumeEducation$', ResumeEducationView.as_view(), name='resumeEducation'),
    url(r'^resumeJob$', ResumeJobView.as_view(), name='resumeJob'),
    url(r'^resumeProjectExperience$', ResumeProjectExperienceView.as_view(), name='resumeProjectExperience'),
]
