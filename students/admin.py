from django.contrib import admin
from .models import StudentProfile, Skill, Achievement, Certificate

admin.site.register(StudentProfile)
admin.site.register(Skill)
admin.site.register(Achievement)
admin.site.register(Certificate)
