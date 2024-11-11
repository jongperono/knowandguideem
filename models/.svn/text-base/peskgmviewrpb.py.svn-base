from django.db import models
from django.core.urlresolvers import reverse
from apps.intent.party.models.Person import Person

class PesKgmViewRpb(models.Model):
    person = models.ForeignKey(Person,null=False,blank=False)
    applied_by = models.ForeignKey(Person,null=False,blank=False)
    date_applied = models.DateField(null=False,blank=False)
    
    class Meta:
        db_table = 'pes_kgm_view_rpb'
    
    @property
    def companyid(self):
        return self.person.company_id
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('viewrpb_modify',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('viewrpb_delete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons