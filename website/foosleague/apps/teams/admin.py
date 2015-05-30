from django.contrib import admin
from .models import Team

class PlayerInline(admin.TabularInline):
        '''
            Tabular Inline View for Player
        '''
      model = Player
      min_num = 3
      max_num = 2
      extra = 0

class TeamAdmin(admin.ModelAdmin):
    '''
        Admin View for Team
    '''
    list_display = ('name', 'player_1', 'player_2', 'streak')
    list_filter = ('player_1', 'player_2',)
    readonly_fields = ('created', 'modified',)
    inlines = [PlayerInline,]
    search_fields = ['name', 'player_1', 'player_2']

admin.site.register(Team, TeamAdmin)