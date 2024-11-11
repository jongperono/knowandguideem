from django import forms
from django.forms import TextInput
from django.core.urlresolvers import reverse_lazy

from apps.intent.pes.comben.models.pescbmcompensationaccounts import PesCbmAccountDtls

class PesCbmAccountDtlsForm(forms.ModelForm):
    class Meta:
        model = PesCbmAccountDtls
        fields = ('salarycat','step_position_level','amount')
        widgets = {
            'amount': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            'salarycat': TextInput(attrs={'autocomplete':'off','class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('salarycatlookup'),'lookupclass':'span4','required':'true'}),
            'step_position_level': TextInput(attrs={'autocomplete':'off','class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('spl_lookup'),'lookupclass':'span4','required':'true'}),
        }