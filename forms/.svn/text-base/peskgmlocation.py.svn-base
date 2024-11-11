# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import TextInput,Select

from django.core.urlresolvers import reverse_lazy

# --------> models

from apps.intent.pes.knowandguideem.models.peskgmlocation import PesKgmLocation

class PesKgmLocationForm(forms.ModelForm):
    class Meta:
        model = PesKgmLocation
        fields = ('branch_code','region','sub_area','address','gp_code','LLL')
        widgets = {
            'branch_code': TextInput(attrs={'autocomplete':'off','class': 'span5','placeholder':'','required':'true' }),
              #'region': TextInput(attrs={'autocomplete':'off','class': 'span5 lookUp','placeholder':'','required':'false','data-link': reverse_lazy('regionlookup') }),
              'region': Select(attrs={'autocomplete':'off','class': 'span5','placeholder':'','required':'false' }),
                'sub_area': Select(attrs={'autocomplete':'off','class': 'span5','placeholder':'','required':'false' }),
                'address': TextInput(attrs={'autocomplete':'off','class': 'span5','placeholder':'','required':'true' }),
                'gp_code': TextInput(attrs={'autocomplete':'off','class': 'span5','placeholder':'','required':'true' }),
                'LLL': TextInput(attrs={'autocomplete':'off','class': 'span5','placeholder':''}),
                  }

class PesKgmLocationForminquery(forms.ModelForm):
    class Meta:
        model = PesKgmLocation
        fields = ('branch_code','region','sub_area')
        widgets = {
            'branch_code': TextInput(attrs={'autocomplete':'off','class': 'span5','placeholder':'','required':'true' }),
              #'region': TextInput(attrs={'autocomplete':'off','class': 'span5 lookUp','placeholder':'','required':'false','data-link': reverse_lazy('regionlookup') }),
               'region': Select(attrs={'autocomplete':'off','class': 'span5','placeholder':'','required':'false' }),
                'sub_area': Select(attrs={'autocomplete':'off','class': 'span3','placeholder':'' }),
                  }
    