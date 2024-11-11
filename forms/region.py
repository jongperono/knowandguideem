# --------> author : json
# --------> 

# --------> django
from django import forms
from django.forms import TextInput

from django.core.urlresolvers import reverse_lazy

# --------> models

from apps.intent.pes.knowandguideem.models.region import Region

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ('description','code')
        widgets = {
            'code': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':'','required':'true' }),
            'description': TextInput(attrs={'autocomplete':'off','class': 'span4','placeholder':'','required':'true' }),
                   }


    