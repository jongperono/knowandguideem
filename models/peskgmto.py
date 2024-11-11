from django.db import models
from django.core.urlresolvers import reverse
from apps.intent.pes.knowandguideem.models.peskgmjd import PesKgmJd


class PesKgmTo(models.Model):
    from apps.intent.pes.comben.models.pescbmcompensationaccounts import PesKgmPosition_W_Allowance
    code = models.CharField(blank=True, null=True,max_length=255,unique=True)
    description = models.CharField(blank=True,max_length=255)
    jd = models.ForeignKey(PesKgmJd, null=True, blank=True,on_delete=models.PROTECT)
    parent = models.ForeignKey('self', null=True, blank=True,on_delete=models.PROTECT)
    position_func = models.ForeignKey(PesKgmPosition_W_Allowance, null=True, blank=True,on_delete=models.PROTECT)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    is_active_skillset = models.IntegerField(default=0)
    
    def natural_key(self):
        return (self.id, self.description)
    
    @property
    def prop1(self):
        return self.description+'*'
    
    
    class Meta:
        db_table = u'pes_kgm_to'
        
    def __unicode__(self):
        return self.description
    
    @property
    def tree(self):
        html = self.description + ' <i id="id_to" class="icon-info-sign" title="Other Info" pid="'+str(self.pk)+'"> </i>'
        '''
        parent = self.parent_id
        html = self.description
        while True:
            if parent:
                val = get_parent(parent)
                if val[1]:
                    html = val[1] + '&nbsp;&#8250;&nbsp;' + html
                if val[0]:
                    parent = val[2]
                else:
                    html = get_description(val[2]) + '&nbsp;&#8250;&nbsp;' + html
                    parent = None
            else:
                break
        '''
        return html
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('to_modify',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('to_delete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons
    
    @property
    def ctrlbtn_x(self):        
        write_icons = '''
                    <a href="'''+ reverse('selectem_skillset_info',kwargs={'id': self.id}) +'''" target="" title="Details"><i class="icon-list-alt icon-large"></i></a>
                    <a title="Edit" target="" href="'''+ reverse('selectem_skillset_edit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('selectem_skillset_delete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons
'''
def get_parent(uid):
    to = PesKgmTo.objects.get(pk=uid)
    if to.parent:
        return True,to.description,to.parent_id
    return False,None,to.id

def get_description(uid):
    to = PesKgmTo.objects.get(pk=uid)
    return to.description
'''
