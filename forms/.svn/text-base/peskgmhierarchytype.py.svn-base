# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import TextInput,Select

from django.core.urlresolvers import reverse_lazy

# --------> models

from apps.intent.pes.knowandguideem.models.peskgmhierarchytype import PesKgmHierarchytype

class PesKgmHierarchytypeForm(forms.ModelForm):
    class Meta:
        model = PesKgmHierarchytype
        fields = ('description','sequence','code','status')
        widgets = {
            'code': TextInput(attrs={'autocomplete':'off','class': 'span2','placeholder':'','required':'true' }),
            'description': TextInput(attrs={'autocomplete':'off','class': 'span2','placeholder':'','required':'true' }),
            'sequence': TextInput(attrs={'autocomplete':'off','class': 'span2','placeholder':'','required':'true' }),
            'status': Select(attrs={'autocomplete':'off','class': 'span2','placeholder':'','required':'true' }),
                   }


    