from django import forms
from django.forms import TextInput,Select
from apps.intent.pes.knowandguideem.models.peskgmstep import PesKgmStep

class StepForm(forms.ModelForm):
    
    class Meta:
        model = PesKgmStep
        fields = ('description','code','status')
        widgets = {
            'description': TextInput(attrs={'class': 'span4','required':'true','placeholder':'Description...'}),
            'code': TextInput(attrs={'class': 'span4','required':'true','placeholder':'Code...'}),
            'status': Select(attrs={'class': 'span4','required':'true','placeholder':''}),
        }   