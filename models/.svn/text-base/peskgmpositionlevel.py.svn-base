from django.db import models
from django.core.urlresolvers import reverse

class PesKgmPositionLevel(models.Model):
    code = models.CharField(blank=False,max_length=50,null=False,unique=True)
    description = models.CharField(max_length=90, blank=False,null=False)
    sequence    = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    
    def natural_key(self):
        return (self.id, self.description)
    
    class Meta:
        db_table = u'pes_kgm_position_level'
    def __unicode__(self):
        return self.description
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('editposition',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('deleteposition',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons
    