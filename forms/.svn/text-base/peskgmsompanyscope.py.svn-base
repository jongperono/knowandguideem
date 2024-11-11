# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import TextInput

from django.core.urlresolvers import reverse_lazy

# --------> models

from apps.intent.pes.knowandguideem.models.peskgmcompanyscope import PesKgmCompanyscope

class PesKgmCompanyscopeForm(forms.ModelForm):
    class Meta:
        model = PesKgmCompanyscope
        fields = ('hierarchy','employee','to','pes_location',)
        widgets = {
            'hierarchy': TextInput(attrs={'autocomplete':'off','class': 'span2 lookUp','placeholder':'','data-link': reverse_lazy('peshierarchylookup2'),'required':'true' }),
            'employee': TextInput(attrs={'autocomplete':'off','class': 'span2 lookUp','placeholder':'','data-link': reverse_lazy('employee_lookup'),'required':'true' }),
            'to': TextInput(attrs={'autocomplete':'off','class': 'span2 lookUp','placeholder':'','data-link': reverse_lazy('tolookup'),'required':'true' }),
            'pes_location': TextInput(attrs={'autocomplete':'off','class': 'span2 lookUp','placeholder':'','data-link': reverse_lazy('pes_position_lookup'),'required':'true' }),
          
                  }


    