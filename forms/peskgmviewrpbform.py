from django import forms
from django.forms import TextInput
from django.core.urlresolvers import reverse_lazy

#models
from apps.intent.pes.knowandguideem.models.peskgmviewrpb import PesKgmViewRpb

class PesKgmViewRpbForm(forms.ModelForm):
    class Meta:
        model = PesKgmViewRpb
        fields = ('person',)
        widgets = {
            'person': TextInput(attrs={'class': 'span4 lookUp','required':'true','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off'}),
        }