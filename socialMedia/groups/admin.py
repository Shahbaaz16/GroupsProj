from django.contrib import admin
from groups import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    '''tabular inline class, allows us to utilize the admin interface in our django website with the ability to edit models on the same page as the parent model. As the GroupMember model has the parent model Group, we can use tabular inline class so that when we visit the admin page we can click on group and then see the group members and edit those as well
    '''
    model = models.GroupMember


admin.site.register(models.Group)
