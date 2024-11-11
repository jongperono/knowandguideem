from __future__ import unicode_literals
from django.db import models
from apps.intent.party.models.Person import Person
from apps.intent.pes.knowandguideem.models.peskgmhierarchy import PesKgmHierarchy
from apps.intent.party.models.Party import Party
from django.core.urlresolvers import reverse

class PesKgmCashgift(models.Model):
    name = models.CharField(max_length=45L)
    class Meta:
        db_table = 'pes_kgm_cashgift'
    
    def __unicode__(self):
        return self.name

class PesKgmCashgiftDtls(models.Model):
    cashgift_id = models.ForeignKey(PesKgmCashgift)
    from_rate = models.IntegerField() # Field renamed because it was a Python reserved word.
    to_rate = models.IntegerField()
    percentage = models.IntegerField()
    class Meta:
        db_table = 'pes_kgm_cashgift_dtls'
        
class PesKgmNewCashgiftAmount(models.Model):
    person = models.ForeignKey(Person, null=True, blank=True)
    year = models.IntegerField()
    company_id = models.CharField(max_length=45L)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    is_final = models.IntegerField(default=0)
    nbu_id = models.CharField(max_length=45L)
    
    
    class Meta:
        db_table = 'pes_kgm_cg_amount'
        
class PesKgmCashGiftRating(models.Model):
    position_level = models.CharField(max_length=255L)
    all_hit = models.DecimalField(max_digits=11, decimal_places=3)
    hit_nothit = models.DecimalField(max_digits=11, decimal_places=3)
    all_nothit = models.DecimalField(max_digits=11, decimal_places=3)
    
    class Meta:
        db_table = 'pes_kgm_cg_rate'
    
    @property
    def ctrlbtn_w(self):
        html = '''
                    <a title="Edit" target="" href="'''+ reverse('pes_kgm_cg_new_ratetbl_edit',kwargs={'uid': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    
               '''
        
        return html

class PesCGCompany(models.Model):
    rate_CHOICES = ((1,'YES'),(0,'NO'))
    company = models.ForeignKey(Party,on_delete=models.PROTECT)
    company_rate = models.IntegerField(choices=rate_CHOICES, blank=True, null=True)
    OverAll = models.IntegerField(choices=rate_CHOICES,blank=True, null=True)
    
    
    class Meta:
       db_table = 'pes_kgm_cg_company_dtls'
       
    @property
    def txn(self):
        return self.id
    
    @property
    def ctrlbtn_w(self):
        html = '''
                    <a title="Edit" target="" href="'''+ reverse('pes_kgm_cg_cmpy_dtl_edit',kwargs={'uid': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    
               '''
        
        return html
    
    @property
    def cmpyrate_stat(self):
        name = PesCGCompany.objects.get(company_id=self.company)
        
        if name.company_rate == 1:
            return 'YES'
        else:
            return 'NO'
    
    @property
    def allcmpy_stat(self):
        name = PesCGCompany.objects.get(company_id=self.company)
        
        if name.OverAll == 1:
            return 'YES'
        else:
            return 'NO'
        
class PesKgmCgParamDates(models.Model):
    
    contract_enddate = models.DateField()
    regularization_date = models.DateField()
    
    class Meta:
        db_table = 'pes_kgm_cg_paramdates'
    
        
    