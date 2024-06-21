from django.contrib import admin

class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
