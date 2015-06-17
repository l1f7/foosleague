from django.contrib import admin
from .models import Match, Goal


class GoalInline(admin.TabularInline):

    '''
        Tabular Inline View for Goal
    '''
    model = Goal
    raw_id_fields = ('match',)
    extra = 0


# Register your models here.
class MatchAdmin(admin.ModelAdmin):

    '''
        Admin View for Match
    '''
    list_display = ('team_1', 'team_2', 'league', 'completed')
    list_filter = ('team_1', 'team_2', 'league', 'completed')
    readonly_fields = ('created', 'modified',)
    inlines = [GoalInline, ]
    search_fields = ['team_1', 'team_2', ]

admin.site.register(Match, MatchAdmin)
