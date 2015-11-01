from django import forms
from .models import fertilizer,avail #, fertilizer_a

class fertilizerform(forms.ModelForm):
    class Meta:
        model = fertilizer
        
class availform(forms.ModelForm):
    class Meta:
        model = avail
        #code
    
    #code

        

        
