from django.contrib import admin

# Register your models here.
from courses.models import Course
from courses.models import CourseImage
from courses.models import CourseAdvantage


admin.site.register(Course)
admin.site.register(CourseImage)
admin.site.register(CourseAdvantage)