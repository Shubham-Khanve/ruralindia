from django.contrib import admin
from .models import name, email, password #, fertilizer_a

class nameadmin(admin.ModelAdmin):
    class Meta:
        model = name
        
admin.site.register(name, nameadmin)

class emailadmin(admin.ModelAdmin):
    class Meta:
        model = email
        
admin.site.register(email, emailadmin)

class passwordadmin(admin.ModelAdmin):
    class Meta:
        model = password
        
admin.site.register(password, passwordadmin)



#class fertilizeraadmin(admin.ModelAdmin):
  #  class Meta:
    #    model = fertilizer_a
    
#admin.site.register(fertilizer_a, fertilizeraadmin)   
# Register your models here.
