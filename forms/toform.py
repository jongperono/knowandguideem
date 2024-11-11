from django import forms
from django.forms import TextInput,Select
from django.core.urlresolvers import reverse_lazy
from django.forms.models import inlineformset_factory

from apps.intent.pes.knowandguideem.models.peskgmto import PesKgmTo
from apps.intent.pes.knowandguideem.models.peskgmpositionclassification import PesKgmPositionClassification
from apps.intent.pes.knowandguideem.forms.peskgmpositionclassification import PesKgmPositionClassificationForm2

class TOForm(forms.ModelForm):
    class Meta:
        model = PesKgmTo
        fields = ('code','description','parent','jd','position_func')
        widgets = {
            'code': TextInput(attrs={'class': 'span4','required':'true','placeholder':'code...'}),
            'description': TextInput(attrs={'class': 'span4','required':'true','placeholder':'description...'}),
            'jd': TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('jdlookup'),'lookupclass':'span4'}),
            'parent': TextInput(attrs={'autocomplete':'off','class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('tolookup'),'lookupclass':'span4'}),
            'position_func': Select(attrs={'class':'span4'}),
        }

class TOForm1(forms.ModelForm):
    class Meta:
        model = PesKgmTo
        fields = ('code','description','jd','position_func')
        widgets = {
            'code': TextInput(attrs={'class': 'span4','required':'true','placeholder':'code...'}),
            'description': TextInput(attrs={'class': 'span4','required':'true','placeholder':'description...'}),
            'jd': TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('jdlookup'),'lookupclass':'span4'}),
            'position_func': Select(attrs={'class':'span4'}),
        }

PesKgmPositionClassificationFormset = inlineformset_factory(PesKgmTo, PesKgmPositionClassification, form=PesKgmPositionClassificationForm2, extra=1, can_delete=True)