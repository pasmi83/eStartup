from django import forms
from leads.models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name','phone','email','subject','message']

    name = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "name":"name", "class":"form-control", "id":"name", "placeholder":"Your Name", "data-rule":"minlen:4", "data-msg":"Please enter at least 4 chars"}))#

    phone = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "name":"phone", "class":"form-control", "id":"phone", "placeholder":"Your Phone", "data-rule":"minlen:7", "data-msg":"Please enter at least 4 chars"}))#

    subject = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "name":"subject", "id":"subject", "placeholder":"Subject", "data-rule":"minlen:4", "data-msg":"Please enter at least 8 chars of subject"}))#

    email = forms.EmailField(widget=forms.TextInput(attrs={"type":"email", "class":"form-control", "name":"email", "id":"email", "placeholder":"Your Email", "data-rule":"email", "data-msg":"Please enter a valid email"}))#

    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "name":"message", "rows":"5", "data-rule":"required", "data-msg":"Please write something for us", "placeholder":"Message"}))#