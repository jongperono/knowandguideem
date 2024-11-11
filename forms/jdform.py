from django import forms
from django.forms import TextInput,Textarea

#models
from apps.intent.pes.knowandguideem.models.peskgmjd import PesKgmJd
from django.core.urlresolvers import reverse_lazy

class JobDescriptionForm(forms.ModelForm):
    
    class Meta:
        model = PesKgmJd
        fields = ('description','code','value','manual','dep_div','position','version','revision','effec_date',
                  'rev_date','appr1','appr2','appr3','appr4','appr5','appr6')
        widgets = {
            'code':TextInput(attrs={'class': 'span4','placeholder':'Code...'}),
            'description': TextInput(attrs={'class': 'span4','required':'true','placeholder':'description...'}),
            'value': Textarea(attrs={'class': 'span4'}),
            'manual':TextInput(attrs={'class': 'span4','placeholder':''}),
            'dep_div':TextInput(attrs={'class': 'span4','placeholder':''}),
            'position':TextInput(attrs={'class': 'span4','placeholder':''}),
            'version':TextInput(attrs={'class': 'span4','placeholder':''}),
            'revision':TextInput(attrs={'class': 'span4','placeholder':''}),
            'effec_date': TextInput(attrs={'class': 'span4 datepicker'}),
            'rev_date': TextInput(attrs={'class': 'span4 datepicker'}),
            'appr1': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr2': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr3': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr4': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr5': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr6': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
        }


class JobDescriptionEditForm(forms.ModelForm):
    value = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 20}))
    class Meta:
        model = PesKgmJd
        fields = ('description','code','manual','dep_div','position','version','revision','effec_date',
                  'rev_date','appr1','appr2','appr3','appr4','appr5','appr6')
        widgets = {
            'code':TextInput(attrs={'class': 'span4','placeholder':'Code...'}),
            'description': TextInput(attrs={'class': 'span4','required':'true','placeholder':'description...'}),
            'manual':TextInput(attrs={'class': 'span4','placeholder':''}),
            'dep_div':TextInput(attrs={'class': 'span4','placeholder':''}),
            'position':TextInput(attrs={'class': 'span4','placeholder':''}),
            'version':TextInput(attrs={'class': 'span4','placeholder':''}),
            'revision':TextInput(attrs={'class': 'span4','placeholder':''}),
            'effec_date': TextInput(attrs={'class': 'span4 datepicker'}),
            'rev_date': TextInput(attrs={'class': 'span4 datepicker'}),
            'appr1': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr2': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr3': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr4': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr5': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
            'appr6': TextInput(attrs={'class': 'span4 lookUp','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','autocomplete':'off','data-link-par':'mod=kg'}),
        }