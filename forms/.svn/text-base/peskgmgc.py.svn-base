from django import forms
from django.forms import TextInput,Select
from datetime import datetime
from django.core.urlresolvers import reverse_lazy

#models
from apps.intent.pes.payroll.models.cashgift import PesKgmCashgiftAmount,\
    PesKgmCashGiftLockDates, PesKgmCashgiftX, PesKgmCashgiftMatrix,\
    PesKgmCashgiftDtlsX
from apps.intent.upload.models.upload import Fileupload2
from apps.intent.pes.knowandguideem.models.peskgmcashgift import PesCGCompany, PesKgmCashGiftRating, PesKgmCgParamDates

class PesPayrollCGForm(forms.ModelForm):
    class Meta:
        YEAR_CHOICES = reversed([(n, n) for n in range (2014, datetime.now().year+1)])
        model = PesKgmCashgiftAmount
        fields = ('person', 'year', 'suspension', 'score')
        widgets = {
            'person': TextInput(attrs={'autocomplete':'off','class': 'span4 lookUp','placeholder':'','data-link': reverse_lazy('employee_personlookup'),'lookupclass':'span4','data-link-par':'mod=py-jo-pp' }),
            'year': Select(attrs={'class':'span4',}, choices=YEAR_CHOICES),
            'suspension': TextInput(attrs={'class':'span4',}),
            'score': TextInput(attrs={'class':'span4',}),
        }
        
class PesPayrollCGForm2(forms.ModelForm):
    class Meta:
        YEAR_CHOICES = reversed([(n, n) for n in range (2014, datetime.now().year+1)])
        model = PesKgmCashgiftAmount
        fields = ('person', 'year', 'suspension', 'score')
        widgets = {
            'person': TextInput(attrs={'autocomplete':'off','class': 'span4'}),
            'year': Select(attrs={'class':'span4',}, choices=YEAR_CHOICES),
            'suspension': TextInput(attrs={'class':'span4',}),
            'score': TextInput(attrs={'class':'span4',}),
        }

class PesPayrollCGUploadForm(forms.ModelForm):
    year = forms.CharField(widget=forms.TextInput(attrs={'class': 'span2','placeholder':'','autocomplete':'off'}))
    class Meta:
        model = Fileupload2
        fields = ('file',)

class PesPayrollCGMasteListForm(forms.Form):
    YEAR_CHOICES = reversed([(n, n) for n in range (2014, datetime.now().year+1)])
    year = forms.ChoiceField(widget = forms.Select(attrs={'class':'span4',}), choices=YEAR_CHOICES)
    
class PesKgmCashGiftLockDatesForm(forms.ModelForm):
    class Meta:
        model = PesKgmCashGiftLockDates
        fields = ('datefrom', 'dateto','resigned_date')
        widgets = {
            'datefrom': TextInput(attrs={'autocomplete':'off','class': 'span3 datepicker'}),
            'dateto': TextInput(attrs={'autocomplete':'off','class': 'span3 datepicker'}),
            'resigned_date': TextInput(attrs={'autocomplete':'off','class': 'span3 datepicker'}),
        }

class PesKgmCgParamDatesForm(forms.ModelForm):
    class Meta:
        model = PesKgmCgParamDates
        fields = ('contract_enddate','regularization_date')
        widgets = {
            
            'contract_enddate': TextInput(attrs={'autocomplete':'off','class': 'span3 datepicker'}),
            'regularization_date': TextInput(attrs={'autocomplete':'off','class': 'span3 datepicker'}),
        }

class PesKgmCashgiftXForm(forms.ModelForm):
    class Meta:
        model = PesKgmCashgiftX
        fields = ('name', 'dt_frm','dt_to','type')
        widgets = {
            'name': TextInput(attrs={'autocomplete':'off','class': 'span4'}),
            'dt_frm': TextInput(attrs={'autocomplete':'off','class': 'span4 datepicker'}),
            'dt_to': TextInput(attrs={'autocomplete':'off','class': 'span4 datepicker'}),
            'type': Select(attrs={'class':'span4',}),
        }

class PesKgmCashgiftMatrixForm(forms.ModelForm):
    class Meta:
        model = PesKgmCashgiftMatrix
        fields = ('rate_id', 'amount','plus_rate_id','plus_amount','lvl_f','lvl_t','lvl2_f','lvl2_t')
        widgets = {
            'plus_amount': TextInput(attrs={'autocomplete':'off','class': 'span4','required':'required'}),
            'amount': TextInput(attrs={'autocomplete':'off','class': 'span4','required':'required'}),
            'rate_id': Select(attrs={'class':'span4','required':'required'}),
            'plus_rate_id': Select(attrs={'class':'span4','required':'required'}),
            'lvl_f': Select(attrs={'class':'span4','required':'required'}),
            'lvl_t': Select(attrs={'class':'span4','required':'required'}),
            'lvl2_f': Select(attrs={'class':'span4','required':'required'}),
            'lvl2_t': Select(attrs={'class':'span4','required':'required'}),
        }

class PesKgmCashgiftDtlsXForm(forms.ModelForm):
    class Meta:
        model = PesKgmCashgiftDtlsX
        fields = ('from_rate','to_rate')
        widgets = {
            'from_rate': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
            'to_rate': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
        }

class PesKgmCgCompanyForm(forms.ModelForm):
    class Meta:
        model = PesCGCompany
        fields = ('company','company_rate','OverAll')
        widgets = {
            'company': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
            #'company_rate': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
            #'OverAll': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
            'company_rate': Select(attrs={'class':'span2','required':'required'}),
            'OverAll': Select(attrs={'class':'span2','required':'required'}),
        }
        
class PesKgmCashgiftRatingForm(forms.ModelForm):
    class Meta:
        model = PesKgmCashGiftRating 
        fields = ('position_level','all_hit','hit_nothit','all_nothit')
        widgets = {
            'position_level': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
            'all_hit': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
            'hit_nothit': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
            'all_nothit': TextInput(attrs={'autocomplete':'off','class': 'span2'}),
        }