from django.urls import path
from leads import views
app_name = 'leads'
urlpatterns = [
    path('',views.CreateLead.as_view(), name='create'),
    ]   