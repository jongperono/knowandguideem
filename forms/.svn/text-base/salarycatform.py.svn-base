from django import forms
from django.forms import TextInput,Select
from apps.intent.pes.knowandguideem.models.peskgmsalarycategory import PesKgmSalarycategory
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory

class SalaryCategoryForm(forms.ModelForm):
    class Meta:
        model = PesKgmSalarycategory
        fields = ('description','minimum_wage','band','status','datefrom','dateto','code','revision_date','area','subarea')
        widgets = {
            'code': TextInput(attrs={'class': 'span4','required':'true','autocomplete':'off'}),
            'description': TextInput(attrs={'class': 'span4','required':'true','placeholder':'description...'}),
            'minimum_wage': TextInput(attrs={'class': 'span4','required':'true'}),
            'band': Select(attrs={'class':'span4','required':'true'}),
            'status': Select(attrs={'class': 'span4','required':'true','autocomplete':'off'}),
            'datefrom': TextInput(attrs={'class': 'span4 datepicker','required':'true','autocomplete':'off'}),
            'dateto': TextInput(attrs={'class': 'span4 datepicker','required':'true','autocomplete':'off'}),
            #'archived_date': TextInput(attrs={'class': 'span4 datepicker','autocomplete':'off'}),
            'revision_date': TextInput(attrs={'class': 'span4 datepicker','autocomplete':'off'}),
            'area': Select(attrs={'autocomplete':'off','class': 'span4 select2'}),
            'subarea': Select(attrs={'autocomplete':'off','class': 'span4 select2'}),
        }

class SalaryCategory(forms.Form):
    salarycat = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('salarycatlookup2') ,'lookupclass':'span3','autocomplete':'off'}))
    

SalaryCategoryFormSet = formset_factory(SalaryCategory, extra=1)