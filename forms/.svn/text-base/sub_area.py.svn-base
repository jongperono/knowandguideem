# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import TextInput

from django.core.urlresolvers import reverse_lazy

# --------> models

from apps.intent.pes.knowandguideem.models.peskgmlocation import PesSubArea

class PesSubAreaForm(forms.ModelForm):
    class Meta:
        model = PesSubArea
        fields = ('description','code','contact')
        widgets = {
            'code': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':'','required':'true' }),
            'description': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':'','required':'true' }),
            'contact': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':'','required':'true' }),
                   }


    