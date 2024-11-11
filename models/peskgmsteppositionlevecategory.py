from django.db import models
from django.core.urlresolvers import reverse
from apps.intent.pes.knowandguideem.models.peskgmsalarycategory import PesKgmSalarycategory
from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevel import PesKgmSteppositionlevel

class PesKgmSteppositionlevelCategory(models.Model):
    salary_rate_choices = (
        (0, 'Daily'),
        (1, 'Monthly'),)
    salary_category = models.ForeignKey(PesKgmSalarycategory, null=True, blank=True,on_delete=models.PROTECT)
    step_position_level = models.ForeignKey(PesKgmSteppositionlevel, null=True, blank=True,on_delete=models.PROTECT)
    basic = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True, default=0)
    cola = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True, default=0)
    allowance = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True, default=0)
    maximum = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True, default=0)
    salary_rate = models.IntegerField(choices=salary_rate_choices)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    
    class Meta:
        db_table = u'pes_kgm_steppositionlevel_category'
        
    @property
    def total(self):
        return self.basic + self.cola + self.allowance
    
    @property
    def salaryrate(self):
        if self.salary_rate == 0:
            return "Daily"
        elif self.salary_rate == 1:
            return "Monthly"
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('splcat_modify',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('splcat_delete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons