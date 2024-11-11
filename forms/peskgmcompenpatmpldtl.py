from django import forms
from django.forms import TextInput,Select

from apps.intent.pes.comben.models.pescbmcompensationaccounts import PesCbmPADtl
from apps.intent.pes.comben.models.pescbmcompensationaccounts import PesKgmPosition_W_Allowance

class PesCbmPADtlForm(forms.ModelForm):
    class Meta:
        model = PesCbmPADtl
        fields = ('position','amount')
        widgets = {
            'amount': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':''}),
            'position': Select(attrs={'autocomplete':'off','class': 'span3','required':'true'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(PesCbmPADtlForm, self).__init__(*args, **kwargs)
        self.fields['position'].queryset = PesKgmPosition_W_Allowance.objects.filter(type=6)