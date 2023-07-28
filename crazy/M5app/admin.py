from django.contrib import admin
from M5app.models import userimg

# Register your models here.
class pets(admin.ModelAdmin):
    list_display=['gender','img','name','price','species','breed','age','gender','description']
admin.site.register(userimg,pets)





