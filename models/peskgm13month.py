from __future__ import unicode_literals
from django.db import models

from apps.intent.pes.knowandguideem.models.peskgmstep import PesKgmStep
from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevel import PesKgmSteppositionlevel

class PesKgm13Month(models.Model):
    name = models.CharField(max_length=45L)
    class Meta:
        db_table = 'pes_kgm_13month'
    
    def __unicode__(self):
        return self.name

class PesKgm13MonthDtls(models.Model):
    kgm_13month = models.ForeignKey(PesKgm13Month,on_delete=models.PROTECT)
    stplvl_from = models.DecimalField(max_digits=13, decimal_places=2)
    stplvl_to = models.DecimalField(max_digits=13, decimal_places=2)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    class Meta:
        db_table = 'pes_kgm_13month_dtls'