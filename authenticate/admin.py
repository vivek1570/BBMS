from django.contrib import admin

# Register your models here.

from .models import person
from .models import donor,stock,receive
# from .models import doctors

# admin.site.register(person)



# admin.site.register(donor)

class PersonDetails(admin.ModelAdmin):
    list_display =  ('p_name', 'p_phone', 'p_b_group', 'p_add','p_gender', 'p_age','p_loc')

admin.site.register(person,PersonDetails)

class RecieveDetail(admin.ModelAdmin):
    list_display=('r_name','r_phone','r_b_group','r_quantity','r_loc')
admin.site.register(receive,RecieveDetail)

class Stockdetail(admin.ModelAdmin):
   list_display=('b_group','b_quantity')
admin.site.register(stock,Stockdetail)

class Donordetail(admin.ModelAdmin):
    list_display=('d_phone','d_b_group','d_quantity','d_date','d_loc')
admin.site.register(donor,Donordetail)



