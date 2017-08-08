from django.contrib import admin
from .models import NewUser,Recive_Adress,ProduceModel,PgroupModel
# Register your models here.

class NewUserAdmin(admin.ModelAdmin):
    list_display = ('username','password','phonenum','address')


class ProduceAdmin(admin.ModelAdmin):
    list_display = ('name','price','imgURL','sortid')

class PgroupModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(NewUser,NewUserAdmin)
admin.site.register(ProduceModel,ProduceAdmin)
admin.site.register(PgroupModel,PgroupModelAdmin)