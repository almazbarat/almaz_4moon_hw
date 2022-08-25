from django.contrib import admin

from core.models import Bottle, BottlesCount


admin.site.register(Bottle)


class BottlesCountAdmin(admin.ModelAdmin):
    model = BottlesCount
    list_display = ["count", "order", "bottle", "finished"]
    list_editable = ["order", "bottle", "finished"]
    fields = ["count", "order", "bottle", "finished"]
    

admin.site.register(BottlesCount, BottlesCountAdmin)