from django.contrib import admin

from .models import League, LeagueMember

class LeagueMemberInline(admin.TabularInline):
    '''
        Tabular Inline View for LeagueMember
    '''
    model = LeagueMember
    min_num = 1
    extra = 1

class LeagueAdmin(admin.ModelAdmin):
    '''
        Admin View for League
    '''
    list_display = ('name',)
    readonly_fields = ('created', 'modified',)
    inlines = [
        LeagueMemberInline
    ]
    search_fields = ['name']

admin.site.register(League, LeagueAdmin)


class LeagueMemberAdmin(admin.ModelAdmin):
    list_display = ('player', 'league', )

admin.site.register(LeagueMember, LeagueMemberAdmin)