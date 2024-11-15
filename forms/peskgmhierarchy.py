# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import TextInput,Select

from django.core.urlresolvers import reverse_lazy
from apps.intent.pes.comben.models.pescbmcompensationaccounts import PesKgmPosition_W_Allowance
# --------> models


from apps.intent.pes.knowandguideem.models.peskgmhierarchy import PesKgmHierarchy
class PesKgmHierarchyForm(forms.ModelForm):
    class Meta:
        model = PesKgmHierarchy
        fields = ('numcode','description','parent','hierarchytype','company','datefrom','dateto','gpcode_div','gpcode_dept','MMM',
                  'mms_company_code','mms_div_code','mms_dept_code')
        widgets = {
            'numcode': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':'','required':'true' }),
            'description': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':'','required':'true' }),
            'parent': TextInput(attrs={'autocomplete':'off','class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('peshierarchylookup2') ,'lookupclass':'span4'}),
            'hierarchytype': TextInput(attrs={'autocomplete':'off','class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('peshierarchytypelookup'),'lookupclass':'span4','required':'true'}),
            'company': TextInput(attrs={'autocomplete':'off','class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('partylookup') ,'lookupclass':'span4','required':'true'}),
            'datefrom': TextInput(attrs={'class': 'span4 datepicker','required':'true','autocomplete':'off'}),
            'dateto': TextInput(attrs={'class': 'span4 datepicker','required':'true','autocomplete':'off'}),
            'gpcode_div': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            'gpcode_dept': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            'MMM': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            'mms_company_code': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            'mms_div_code': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            'mms_dept_code': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
                  }

class PesKgmHierarchyGPForm(forms.ModelForm):
    class Meta:
        model = PesKgmHierarchy
        fields = ('gpcode_div','gpcode_dept','MMM')#,'mms_company_code','mms_div_code','mms_dept_code')
        widgets = {
            'gpcode_div': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            'gpcode_dept': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            'MMM': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            #'mms_company_code': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            #'mms_div_code': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
            #'mms_dept_code': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':''}),
                  }

class PesKgmHierarchyFormReports(forms.ModelForm):
    class Meta:
        model = PesKgmHierarchy
        fields = ('numcode','description','parent','hierarchytype','company',)
        widgets = {
            'gpcode_div': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':''}),
            'gpcode_dept': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':''}),
            'numcode': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':''}),
            'description': TextInput(attrs={'autocomplete':'off','class': 'span3','placeholder':''}),
            'parent': TextInput(attrs={'autocomplete':'off','class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('peshierarchylookup2') ,'lookupclass':'span4'}),
            'hierarchytype': TextInput(attrs={'autocomplete':'off','class': 'span3 lookUp','placeholder':'','data-link': reverse_lazy('peshierarchytypelookup'),'lookupclass':'span4' }),
            'company': TextInput(attrs={'autocomplete':'off','class': 'span3 lookUp','placeholder':'','data-link': reverse_lazy('nbu_lookup') ,'lookupclass':'span4'}),
          
                  }

class CompanyFilterForm(forms.Form):
    hierarchy = forms.CharField(widget=forms.TextInput(attrs={'class': 'span4 lookUp btch_company','placeholder':'','data-link': reverse_lazy('hierarchycompanylookup') ,'lookupclass':'span4','autocomplete':'off'}),required=False)