from django.views.generic.base import TemplateView,ContextMixin

from tutors.models import Tutor
from courses.models import Course
from courses.models import CourseAdvantage
from projects.models import Project
from feedbacks.models import Feedback


class ContextListMixin(ContextMixin):
    extra_context = {"tutors":Tutor.objects.all(),
    "courses":Course.objects.all(),
    "advantages":CourseAdvantage.objects.all(),
    "projects":Project.objects.all(),
    "feedbacks":Feedback.objects.all(),
    }

#class CoursesListMixin(ContextMixin):
#   extra_context = {"courses":Course.objects.all}
    
class Index(TemplateView,ContextListMixin):
    template_name = 'pages/index.html'

    
    

