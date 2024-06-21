from django.contrib import admin

class RankingAdmin(admin.ModelAdmin):
    list_display = ('league',)
    search_fields = ('league',)
    list_filter = ('league',)
