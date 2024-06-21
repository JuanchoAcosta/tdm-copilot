from django.contrib import admin

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    search_fields = ('name',)
