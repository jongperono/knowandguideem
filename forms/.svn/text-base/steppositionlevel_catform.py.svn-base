from django import forms
from django.forms import TextInput,Select
from django.core.urlresolvers import reverse_lazy

from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevecategory import PesKgmSteppositionlevelCategory

class StepPositionLevelCatForm(forms.ModelForm):
    class Meta:
        model = PesKgmSteppositionlevelCategory
        fields = ('step_position_level','basic','cola','allowance','maximum','salary_rate')
        widgets = {
            'step_position_level': TextInput(attrs={'class': 'span4 lookUp','required':'true','placeholder':'','data-link': reverse_lazy('spl_lookup') ,'lookupclass':'span4'}),
            'basic': TextInput(attrs={'class': 'span4','required':'true','placeholder':'Basic...'}),
            'cola': TextInput(attrs={'class': 'span4','required':'true','placeholder':'COLA...'}),
            'allowance': TextInput(attrs={'class': 'span4','placeholder':'Allowance...'}),
            'maximum': TextInput(attrs={'class': 'span4','placeholder':'Maximum...'}),
            'salary_rate': Select(attrs={'class': 'span4','placeholder':'Maximum...'}),
        }   