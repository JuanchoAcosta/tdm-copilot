from django.contrib import admin

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'age', 'tmt_id')
    search_fields = ('name', 'lastname', 'tmt_id')
