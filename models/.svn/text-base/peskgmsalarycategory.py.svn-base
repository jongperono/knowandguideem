from django.db import models
from django.core.urlresolvers import reverse
from apps.intent.pes.knowandguideem.models.region import Region
from apps.intent.pes.knowandguideem.models.peskgmlocation import PesSubArea

class PesKgmSalarycategory(models.Model):
    status_CHOICES =((1,'Active'),(0,'Inactive'),(2,'Archived'))
    band_choices = (
        (1, 'Band 1'),
        (2, 'Band 2'),
        (3, 'Band 3'),
        (4, 'Band 4'),
        (5, 'Band 5'),
        (6, 'Category 1'),
        (7, 'Category 2'),
        (8, 'Category 3'),
        (9, 'Category 4'),
        (10, 'Category 5'),
        (11, 'Category 6'),
        (12, 'Category 7'))
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    description = models.CharField(null=False, blank=False,max_length=255)
    minimum_wage = models.DecimalField(null=False, blank=False, max_digits=13, decimal_places=4)
    band = models.IntegerField(null=False, blank=False,choices=band_choices)
    status = models.IntegerField(choices=status_CHOICES, null=False, blank=False)
    datefrom = models.DateField(null=False, blank=False)
    dateto = models.DateField(null=False, blank=False)
    area = models.ForeignKey(Region, null=True,blank=True)
    subarea = models.ForeignKey(PesSubArea, null=True,blank=True)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField()
    archived_date = models.DateField(null=True, blank=True)
    revision_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = u'pes_kgm_salarycategory'
        
    def __unicode__(self):
        return self.description
    
    def natural_key(self):
        return (self.id, self.description)
    
    @property
    def bandname(self):
        if self.band >= 6:
            if self.band == 6:   
                return "Category 1"
            if self.band == 7:   
                return "Category 2"
            if self.band == 8:   
                return "Category 3"
            if self.band == 9:   
                return "Category 4"
            if self.band == 10:   
                return "Category 5"
            if self.band == 11:   
                return "Category 6"
            if self.band == 12:   
                return "Category 7"            
        else:
            return "Band "+str(self.band)
    @property
    def statusname(self):
        if self.status == 0:
            return 'Inactive'
        elif self.status == 1:
            return 'Active'
        elif self.status == 2:
            return 'Archived'
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):
        if self.status == 2:
            write_icons = ''
                        
        else:
            write_icons = '''
                        <a title="Archive" target="" modal-link="'''+ reverse('salarycat_archive',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure you want to archive this entry?" modal-title="Confirm Archive:" class="confirm_page_link"><i class="icon-briefcase icon-large"></i></a>
                        <a title="Edit" target="" href="'''+ reverse('salarycat_modify',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                        <a title="Delete" target="" modal-link="'''+ reverse('salarycat_delete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                        '''
        return write_icons