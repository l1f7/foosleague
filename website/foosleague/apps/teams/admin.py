from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    '''
        Admin View for Team
    '''
    list_display = ('name', 'logo', 'player_1', 'player_2',)
    list_filter = ('player_1', 'player_2',)
    readonly_fields = ('created', 'modified',)
    search_fields = ['name', 'player_1', 'player_2']

admin.site.register(Team, TeamAdmin)