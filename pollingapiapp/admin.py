from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['User_C','Phone']
admin.site.register(UserProfile, UserAdmin)


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['Question', 'Op1', 'Op2', 'Op3', 'Op4', 'Date']
admin.site.register(Question, QuestionAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ['VQuestion', 'Result', 'User']

admin.site.register(Vote, VoteAdmin)





