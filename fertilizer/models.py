from django.db import models
from django.utils.encoding import smart_unicode
    
class name(models.Model):
    name_register = models.CharField(max_length=120, null=True, blank=True)
    
    def __unicode__(self):
        return smart_unicode(self.name_register)
    
class email(models.Model):
    email_register = models.CharField(max_length=120, null=True, blank=True)
    
    def __unicode__(self):
        return smart_unicode(self.email_register)
    
class password(models.Model):
    password_register = models.CharField(max_length=120, null=True, blank=True)
    
    def __unicode__(self):
        return smart_unicode(self.password_register)
    
    
    
    #code
    

    
    
    #def __unicode__(self):
    #   return smart_unicode(self.avail_fertilizer)
    
    
    
    #code

    
#class fertilizer_a(models.Model):
    #fertilizera = models.CharField(max_length=120, null=True, blank=True)
    
   # def __unicode__(self):
     #   return smart_unicode(self.fertilizera)
