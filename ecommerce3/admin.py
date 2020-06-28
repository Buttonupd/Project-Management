from django.contrib import admin
from .models import Cohort
from .models import UserProfile
from .models import Invite


class CohortAdmin(admin.ModelAdmin):
    list_display = ['name','email','city','found_date',]
    search_fields = ['name', 'social_name','city',]

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'cohort',]

class InviteAdmin(admin.ModelAdmin):
    list_display = ['inviter', 'invited',]
    search_fields = ['inviter', 'invited',]
   

# Register your models here.
admin.site.register(Cohort, CohortAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Invite, InviteAdmin)

