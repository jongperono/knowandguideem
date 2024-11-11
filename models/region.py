from django.db import models
from django.core.urlresolvers import reverse

class Region(models.Model):
    code = models.CharField(max_length=30,blank=False,null=False,unique=True)
    description = models.CharField(max_length=180, blank=False,null=False)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    
    class Meta:
        db_table = u'region'
        
    def __unicode__(self):
        return self.description
        
    def natural_key(self):
        return (self.id, self.description)
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('regionedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('regiondelete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons