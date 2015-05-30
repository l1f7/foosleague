from django.contrib import admin
from .models import Team
from players.models import Player


# class PlayerInline(admin.TabularInline):
#       '''
#           Tabular Inline View for Player
#       '''
#       model = Player
#       min_num = 3
#       max_num = 2
#       extra = 0


class TeamAdmin(admin.ModelAdmin):
    '''
        Admin View for Team
    '''
    list_display = ('name', 'streak')
    list_filter = ('players',)
    readonly_fields = ('created', 'modified',)
    # inlines = [PlayerInline,]
    search_fields = ['name', 'players',]

admin.site.register(Team, TeamAdmin)