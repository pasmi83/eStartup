from django.views.generic.base import TemplateView,ContextMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect

from django.contrib import messages
from django.urls import reverse


from tutors.models import Tutor
from courses.models import Course
from courses.models import CourseAdvantage
from projects.models import Project
from feedbacks.models import Feedback
from announcements.models import Announcement
from leads.models import Lead
from leads.forms import LeadForm
from setup.models import Setup

from leads.utils import get_error_message_from_form






class ContextListMixin(ContextMixin):
    extra_context = {"tutors":Tutor.objects.all(),
    "courses":Course.objects.all(),
    "advantages":CourseAdvantage.objects.all(),
    "projects":Project.objects.all(),
    "feedbacks":Feedback.objects.all(),
    "announcements":Announcement.objects.all(),
    "setup":Setup.objects.all(),

    }

    

class CreateLeadForm(FormMixin):
    model = Lead
    form_class = LeadForm
    success_url =  '/#contact'

    def form_valid(self,form,*args):
        try:
            lead = Lead(**form.cleaned_data)
            lead.save()#создание объекта связи, если форма валидна
        except:
            messages.error(self.request, "Сообщение не передано")
        else:
            messages.success(self.request, "Сообщение передано, ждите ответа")
        
        return super().form_valid(form,*args)
    
    def form_invalid(self,form,*args):
        for error in form.errors.items():
            get_error_message_from_form(self, error)
        
        return redirect(reverse('pages:index')+'#contact')
    

class PostDataMixin:
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    
class Index(TemplateView,CreateLeadForm,ContextListMixin,PostDataMixin):
    template_name = 'pages/index.html'

    
    
    """
    Handle POST requests: instantiate a form instance with the passed
    POST variables and then check if it's valid.
    """





    
    

