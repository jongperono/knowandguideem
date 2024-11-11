# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import TextInput

from django.core.urlresolvers import reverse_lazy

# --------> models

from apps.intent.pes.knowandguideem.models.peskgmpositionlevel import PesKgmPositionLevel

class peskgmpositionlevelForm(forms.ModelForm):
    class Meta:
        model = PesKgmPositionLevel
        fields = ('description','code','sequence')
        widgets = {
            'description': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':'Description..','required':'true' }),
            'code': TextInput(attrs={'class': 'span4','required':'true','placeholder':'Code...'}),
            'sequence': TextInput(attrs={'class': 'span4','required':'true','placeholder':'sequence...'}),
            
                  }


    