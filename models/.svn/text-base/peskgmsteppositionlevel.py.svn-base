from django.db import models
from apps.intent.pes.knowandguideem.models.peskgmstep import PesKgmStep
from apps.intent.pes.knowandguideem.models.peskgmpositionlevel import PesKgmPositionLevel
from django.core.urlresolvers import reverse

access_choices = ((1,"Level 1"),
                  (2,"Level 2"),
                  (3,"Level 3"),
                  (4,"Level 4"),
                  (5,"Level 5"),)
        
class PesKgmSteppositionlevel(models.Model):
    status_CHOICES = (1, 'Active'), (0, 'Inactive')
    step = models.ForeignKey(PesKgmStep, null=False, blank=False,on_delete=models.PROTECT)
    position_level = models.ForeignKey(PesKgmPositionLevel, null=False, blank=False,on_delete=models.PROTECT)
    sequence = models.IntegerField(blank=True,max_length=11)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    access = models.IntegerField(null=False,blank=False,choices=access_choices)
    seq2 = models.DecimalField(max_digits=13, decimal_places=2)
    status = models.IntegerField(default=1,choices=status_CHOICES,null=True,blank=True)
    
    class Meta:
        db_table = u'pes_kgm_steppositionlevel' 
        
    def natural_key(self):
        return (self.id,self.position_level.description + self.step.description)
    
    def __unicode__(self):
        return (self.position_level.description + self.step.description)
    
    @property
    def access_name(self):
        for a,b in access_choices:
            if self.access == a:
                return b
            
    @property
    def description(self):
        return (self.position_level.description + self.step.description)
    
    @property
    def statusname(self):
        if self.status == 0:
            return 'Inactive'
        elif self.status == 1:
            return 'Active'
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('editstepposition',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('deletestepposition',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons