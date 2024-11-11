from django.db import models
from apps.intent.pes.knowandguideem.models.peskgmto import PesKgmTo

from apps.intent.party.models.Party import Party
from apps.intent.pes.knowandguideem.models.peskgmhierarchy import PesKgmHierarchy
from apps.intent.pes.knowandguideem.models.peskgmlocation import PesKgmLocation

class PesKgmCompanyscope(models.Model):
    hierarchy = models.ForeignKey(PesKgmHierarchy, null=True, blank=True,on_delete=models.PROTECT)
    employee = models.ForeignKey(Party, null=True, blank=True)
    to = models.ForeignKey(PesKgmTo, null=True, blank=True,on_delete=models.PROTECT)
    pes_location = models.ForeignKey(PesKgmLocation, null=True, blank=True,on_delete=models.PROTECT)
    class Meta:
        db_table = u'pes_kgm_companyscope'
        
        