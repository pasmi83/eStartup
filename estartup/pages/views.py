from django.views.generic.base import TemplateView,ContextMixin

from tutors.models import Tutor
from courses.models import Course

class ContextListMixin(ContextMixin):
    extra_context = {"tutors":Tutor.objects.all(),
    "courses":Course.objects.all()}

#class CoursesListMixin(ContextMixin):
#   extra_context = {"courses":Course.objects.all}
    
class Index(TemplateView,ContextListMixin):
    template_name = 'pages/index.html'

    
    

