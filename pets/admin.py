from django.contrib import admin
from .models import pet, state


class StateAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'state_name')


# Register your models here.
admin.site.register(pet)
admin.site.register(state, StateAdmin)
