from django.db import models
from django.core.urlresolvers import reverse
from apps.intent.warehouse.models.location import Location
from apps.intent.pes.knowandguideem.models.region import Region

class PesSubArea(models.Model):
    code = models.CharField(max_length=30L, blank=True, unique=True)
    description = models.CharField(max_length=60L, blank=True)
    contact = models.TextField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'pes_sub_area'
        
    def __unicode__(self):
        return self.description
    
    def natural_key(self):
        return self.id, self.description
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('sub_areaedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('sub_areadelete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons

class PesKgmLocation(models.Model):
    branch_code = models.CharField(max_length=90)
    location = models.ForeignKey(Location,on_delete=models.PROTECT)
    region = models.ForeignKey(Region, null=True, blank=True,on_delete=models.PROTECT)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    sub_area = models.ForeignKey(PesSubArea, null=True, blank=True)
    gp_code = models.CharField(max_length=20,null=True, blank=True)
    LLL = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = u'pes_kgm_location'

    def natural_key(self):
        return (self.id, self.branch_code)
    @property
    def sub_area_desc(self):
        if self.sub_area:
            return self.sub_area.description
        else:
            return ''

    @property
    def partyname(self):
        return self.location.party.name
    
    @property
    def type(self):
        return self.location.location_type.description
    
    def __unicode__(self):
        return self.branch_code
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('peskgmlocationedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('peskgmlocationdelete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons