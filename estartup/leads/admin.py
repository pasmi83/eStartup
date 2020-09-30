from django.urls import reverse
from django.utils.http import urlencode
from django.contrib import admin
from django.utils.html import format_html
from leads.models import Lead,Notification

# Register your models here.

class MyAdmin(admin.AdminSite):
    site_header = "Кастомная админка"


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    
    list_display =  ('subject','name','email','notifications_count')
    
    def notifications_count(self,obj):
        count = Notification.objects.filter(lead = obj).count()
        url = reverse('admin:leads_notification_changelist')+'?'+ urlencode({"lead": f"{obj.id}"})
        return format_html('<a href="{}">{}</a>', url, count)
    notifications_count.short_description = "Счётчик сообщений"



    fieldsets = (
        (None, {
            "fields": ('name',),

        }),
        ('Контактные данные', {
            
            "classes":('collapse',),
            "fields": (('email','phone'),               
            ),

        }),
        ('Существо вопроса', {
            
            "fields": ('subject','message',               
            ),
            
        }),
    )
    
    list_filter = ('name','subject')
    ordering = ('name', 'email')
    search_fields = ('subject',)
    list_per_page = 10
    actions_on_top = False
    actions_on_bottom = True