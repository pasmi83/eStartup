from django.shortcuts import render
from django.views.generic.edit import CreateView
from leads.models import Lead
from leads.forms import LeadForm
# Create your views here.
class CreateLead(CreateView):
    model = Lead
    form_class = LeadForm
    success_url =  '/'
    template_name = 'pages/index.html'


