# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import Select,TextInput

from django.core.urlresolvers import reverse_lazy

# --------> models

from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevel import PesKgmSteppositionlevel

class peskgmsteppositionlevelForm(forms.ModelForm):
    class Meta:
        model = PesKgmSteppositionlevel
        fields = ('step','position_level','access','status','seq2')
        widgets = {
            #'step': TextInput(attrs={'autocomplete':'off','class': 'span3 lookUp','placeholder':'','data-link': reverse_lazy('pes_step_lookup'),'required':'true'}),
            # 'position_level': TextInput(attrs={'autocomplete':'off','class': 'span3 lookUp','placeholder':'','data-link': reverse_lazy('pes_position_lookup'),'required':'true' }),
            'step': Select(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true'}),
            'position_level': Select(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true' }),
            'access': Select(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true' }),
            'status': Select(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true' }),
            'seq2': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':''}),
                  }


    