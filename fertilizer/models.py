from django.db import models
from django.utils.encoding import smart_unicode

class fertilizer(models.Model):
    name_fertilizer = models.CharField(max_length=120, null=True, blank=True)
    #avail_fertilizer = models.CharField(max_length=120, null=True, blank=True)
    
    def __unicode__(self):
        return smart_unicode(self.name_fertilizer)
    
class avail(models.Model):
    avail_fertilizer = models.CharField(max_length=120, null=True, blank=True)
    
    def __unicode__(self):
        return smart_unicode(self.avail_fertilizer)
    #code

    
    
    #def __unicode__(self):
    #   return smart_unicode(self.avail_fertilizer)
    
    
    
    #code

    
#class fertilizer_a(models.Model):
    #fertilizera = models.CharField(max_length=120, null=True, blank=True)
    
   # def __unicode__(self):
     #   return smart_unicode(self.fertilizera)
