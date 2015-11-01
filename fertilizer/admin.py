from django.contrib import admin
from .models import fertilizer, avail #, fertilizer_a

class fertilizeradmin(admin.ModelAdmin):
    class Meta:
        model = fertilizer
    
admin.site.register(fertilizer, fertilizeradmin)

class availadmin(admin.ModelAdmin):
    class Meta:
        model = avail
        
admin.site.register(avail, availadmin)



#class fertilizeraadmin(admin.ModelAdmin):
  #  class Meta:
    #    model = fertilizer_a
    
#admin.site.register(fertilizer_a, fertilizeraadmin)   
# Register your models here.
