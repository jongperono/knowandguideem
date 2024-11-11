from django.db import models
#from apps.intent.pes.pis.models.pespiscds import PesCmbCompanyStatus

class PesKgmEmploymentStatus(models.Model):
    code = models.CharField(max_length=5)
    description = models.CharField(max_length=20, blank=True)
    currently_employed = models.IntegerField(max_length=11, blank=True)
    company_status = models.IntegerField(null=True,blank=True)
    
    def __unicode__(self):
        return self.description
    
    def natural_key(self):
        return (self.id, self.description)
    
    class Meta:
        db_table = u'pes_kgm_rpb_employment_status'

class PesKgmEmploymentStatusview(models.Model):
    code = models.CharField(max_length=5)
    description = models.CharField(max_length=20, blank=True)
    currently_employed = models.IntegerField(max_length=11, blank=True)
    company_status = models.IntegerField(null=True,blank=True)
    
    def __unicode__(self):
        return self.description
    
    def natural_key(self):
        return (self.id, self.description)
    
    class Meta:
        db_table = u'pes_kgm_rpb_employment_status_view'
        
        
        