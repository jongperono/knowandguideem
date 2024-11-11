from django.db import models
from django.core.urlresolvers import reverse
from apps.intent.party.models.Party import Party
from apps.intent.pes.knowandguideem.models.peskgmhierarchytype import PesKgmHierarchytype

class PesKgmHierarchy(models.Model):
    ccc_code = {415:111,420:112,428:113,429:114,430:115,431:116,432:117,433:118,434:119,435:120,436:121,33355:122,37053:123}
    mms_code = {432:10,428:20,435:30,420:40,429:50,430:60,415:70,437:80,437:81,33355:90,436:91,437:92,433:93,434:94,37053:96,400:95,437:97,38165:98}
    gpcode_div = models.CharField(max_length=20, blank=True, null=True)
    gpcode_dept = models.CharField(max_length=20, blank=True, null=True)
    MMM = models.IntegerField(blank=True, null=True)
    CCC = models.IntegerField(blank=True, null=True)
    numcode = models.CharField(max_length=765, blank=True, unique=True)
    company = models.ForeignKey(Party,on_delete=models.PROTECT)
    description = models.CharField(max_length=765, blank=True)
    short_name = models.CharField(max_length=20, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True,on_delete=models.PROTECT)
    hierarchytype = models.ForeignKey(PesKgmHierarchytype, null=True, blank=True,on_delete=models.PROTECT)
    datefrom = models.DateField(null=False, blank=False)
    dateto = models.DateField(null=False, blank=False)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    mms_company_code = models.IntegerField(null=False,blank=False,default=0)
    mms_div_code = models.IntegerField(null=True,blank=True,default=0)
    mms_dept_code = models.CharField(max_length=20, blank=True)#IntegerField(null=False,blank=False,default=0)
    
    def natural_key(self):
        return (self.id, (self.numcode + ' - ' + self.description))
    
    class Meta:
        db_table = u'pes_kgm_hierarchy'
    
    def __unicode__(self):
        return (self.numcode + ' - ' + self.description)
    
    @property
    def tree(self):
        html = self.description + ' <i id="id_hierarchy" class="icon-info-sign" title="Other Info" pid="'+str(self.pk)+'"> </i>'
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
    def parentname(self):
        if self.parent:
            return self.parent.description
        return '-'
    
    @property
    def mms_ccc(self):
        try:
            return self.ccc_code[self.company.id]
        except:
            return None
    @property
    def _mms_code(self):
        try:
            return self.mms_code[self.company.id]
        except:
            return None
    
    @property
    def _mmm(self):
        try:
            return self.MMM
        except:
            return None
    
    @property
    def _ccc(self):
        try:
            return self.CCC
        except:
            return None
    
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('peskgmhierarchyeedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('peskgmhierarchydelete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons
    
    @property
    def ctrlbtn_x(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('peskgmhierarchyeedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    '''
        return write_icons

'''
def get_parent(uid):
    to = PesKgmHierarchy.objects.get(pk=uid)
    if to.parent:
        return True,to.description,to.parent_id
    return False,None,to.id

def get_description(uid):
    to = PesKgmHierarchy.objects.get(pk=uid)
    return to.description
'''