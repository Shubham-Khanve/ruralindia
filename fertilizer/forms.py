from django import forms
from .models import name, email, password #, fertilizer_a
       
class nameform(forms.ModelForm):
    class Meta:
        model = name
        
class emailform(forms.ModelForm):
    class Meta:
        model = email
        
class passwordform(forms.ModelForm):
    class Meta:
        model = password
        #code
    
    #code

        

        
