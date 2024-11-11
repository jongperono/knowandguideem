# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import TextInput,Select

from django.core.urlresolvers import reverse_lazy

# --------> models

from apps.intent.pes.knowandguideem.models.peskgmpositionclassification import PesKgmPositionClassification

class PesKgmPositionClassificationForm(forms.ModelForm):
    class Meta:
        
        model = PesKgmPositionClassification
        fields = ('to','description','start_step_position_level','code','status','category')
        widgets = {
            'code': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true' }),
            'to': TextInput(attrs={'autocomplete':'off','class': 'span3 lookUp','placeholder':'','required':'true' ,'data-link': reverse_lazy('tolookup')}),
            'description': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true' }),
            'start_step_position_level': TextInput(attrs={'autocomplete':'off','class': 'span3 lookUp','placeholder':'','required':'true' ,'data-link': reverse_lazy('spl_lookup')}),
            'status': Select(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true' }),
            'category': Select(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true' }),
                   }

class PesKgmPositionClassificationForm2(forms.ModelForm):
    class Meta:
        
        model = PesKgmPositionClassification
        fields = ('description','start_step_position_level','code','status','category')
        widgets = {
            'code': TextInput(attrs={'autocomplete':'off','class': 'span3 code','placeholder':''}),
            'description': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':''}),
            'start_step_position_level': TextInput(attrs={'autocomplete':'off','class': 'span2 lookUp','placeholder':'','data-link': reverse_lazy('spl_lookup')}),
            'status': Select(attrs={'autocomplete':'off','class': 'span2','placeholder':''}),
            'category': Select(attrs={'autocomplete':'off','class': 'span3','placeholder':'','required':'true' }),              
                   }

class PositionReportForm(forms.Form):
    yes_no_CHOICES = [('','-----------'),(0,'Inactive'),(1,'Active')]
    status = forms.ChoiceField(choices=yes_no_CHOICES,required=False,widget=forms.Select(attrs={'class':'span4'}))
    to = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('tolookup') ,'lookupclass':'span3','autocomplete':'off'}))
    bandlevel = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('spl_lookup') ,'lookupclass':'span3','autocomplete':'off'}))
    code = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4','placeholder':'','autocomplete':'off'}))
    description = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4','placeholder':'','autocomplete':'off'}))
    