from django.contrib import admin

from .models import Season

class SeasonAdmin(admin.ModelAdmin):
    '''
        Admin View for Season
    '''
    list_display = ('name','start','end')
    readonly_fields = ('created', 'modified',)
    search_fields = ['name', 'start', 'end']

admin.site.register(Season, SeasonAdmin)