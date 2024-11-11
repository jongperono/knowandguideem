from django import forms
from django.forms import TextInput,Select
from django.core.urlresolvers import reverse_lazy
from apps.intent.pes.knowandguideem.models.peskgmrpb import PesKgmRpb
from apps.intent.pes.knowandguideem.models.region import Region

class RPBForm(forms.ModelForm):
    class Meta:
        model = PesKgmRpb
        fields = ('to','required_count','pes_location','empoyment_status','autoreplenish','hierarchy','code','description','datefrom','dateto','da_count','temp')
        widgets = {
            'code':TextInput(attrs={'class': 'span4','placeholder':'Code...','required':'true'}),
            'description':TextInput(attrs={'class': 'span4','placeholder':'Description...','required':'true'}),
            'to': TextInput(attrs={'class': 'span4 lookUp','required':'true','placeholder':'','data-link': reverse_lazy('tolookup') ,'lookupclass':'span4'}),
            'required_count': TextInput(attrs={'class': 'span4','required':'true','placeholder':'Required Count...'}),
            'autoreplenish':Select(attrs={'class': 'span4','required':'true','placeholder':'Auto Replenish...'}),
            'pes_location': TextInput(attrs={'class': 'span4 lookUp','required':'true','placeholder':'','data-link': reverse_lazy('peslocation_lookup2') ,'lookupclass':'span4'}),
            'empoyment_status': TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('emp_lookup') ,'required':'true','lookupclass':'span4'}),
            'hierarchy': TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('peshierarchylookup2') ,'required':'true','lookupclass':'span4'}),
            'datefrom': TextInput(attrs={'class': 'span4 datepicker','required':'true','autocomplete':'off'}),
            'dateto': TextInput(attrs={'class': 'span4 datepicker','required':'true','autocomplete':'off'}),
            'da_count':TextInput(attrs={'class':'span4'}),
            'temp':Select(attrs={'class':'span4','required':'true'}),
        }   
        

class RPBFormReport(forms.ModelForm):
    class Meta:
        model = PesKgmRpb
        fields = ('to','required_count','pes_location','empoyment_status','autoreplenish','hierarchy','code','description')
        widgets = {
            'code':TextInput(attrs={'class': 'span4','placeholder':'Code...'}),
            'description':TextInput(attrs={'class': 'span4','placeholder':'Description...'}),
            'to': TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('tolookup') ,'lookupclass':'span3'}),
            'required_count': TextInput(attrs={'class': 'span4','placeholder':'Required Count...'}),
            'autoreplenish':Select(attrs={'class': 'span4','placeholder':'Auto Replenish...'}),
            'pes_location': TextInput(attrs={'class': 'span3 lookUp','placeholder':'','data-link': reverse_lazy('peslocation_lookup2') ,'lookupclass':'span3'}),
            'empoyment_status': TextInput(attrs={'class': 'span3 lookUp','placeholder':'','data-link': reverse_lazy('emp_lookup') ,'lookupclass':'span3'}),
            'hierarchy': TextInput(attrs={'class': 'span3 lookUp','placeholder':'','data-link': reverse_lazy('peshierarchylookup2') ,'lookupclass':'span3'}),
        }

class RPBReportForm(forms.Form):
    yes_no_CHOICES = [('','-----------'),(0,'No'),(1,'Yes')]
    area_CHOICES = [('','-----------')]+[(m.id, m.description) for m in Region.objects.filter(deleted=0)]
    area = forms.ChoiceField(choices=area_CHOICES,required=False,widget=forms.Select(attrs={'class':'span4','autocomplete':'off'}))
    autoreplenish = forms.ChoiceField(choices=yes_no_CHOICES,required=False,widget=forms.Select(attrs={'class':'span4','autocomplete':'off'}))
    company = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('partylookup') ,'lookupclass':'span3','autocomplete':'off'}))
    employment_status = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('emp_lookup') ,'lookupclass':'span3','autocomplete':'off'}))
    branch = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('peslocation_lookup2') ,'lookupclass':'span3','autocomplete':'off'}))
    division = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('division_lookup') ,'lookupclass':'span3','autocomplete':'off'}))
    department = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('department_lookup') ,'lookupclass':'span3','autocomplete':'off'}))
        
        