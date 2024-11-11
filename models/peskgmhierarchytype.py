from django.db import models
from django.core.urlresolvers import reverse

class PesKgmHierarchytype(models.Model):
    status_CHOICES =((1,'Active'),(0,'Inactive'))
    code = models.CharField(blank=False,max_length=30,unique=True,null=False)
    description = models.CharField(max_length=90, null=False,blank=False)
    sequence = models.IntegerField(null=True, blank=True,unique=True)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    status = models.IntegerField(choices=status_CHOICES)
    def natural_key(self):
        return (self.id, self.description)
    
    class Meta:
        db_table = u'pes_kgm_hierarchytype'
    
    def __unicode__(self):
        return self.description
    
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
        if self.status == 1:
            write_icons = '''
                        <a title="Edit" target="" href="'''+ reverse('hierarchytypeedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                        '''
        elif self.status == 0:
            write_icons = '''
                        <a title="Edit" target="" href="'''+ reverse('hierarchytypeedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                        <a title="Delete" target="" modal-link="'''+ reverse('hierarchytypedelete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                        '''
        return write_icons