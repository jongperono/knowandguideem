from django.db import models
from django.core.urlresolvers import reverse
from apps.intent.upload.models.upload import Fileupload
from apps.intent.party.models.Person import Person

class PesKgmJd(models.Model):
    code = models.CharField(blank=False,max_length=255,unique=True,null=False)
    description = models.CharField(blank=False,max_length=255,null=False)
    value = models.TextField(blank=True,null=True)
    manual = models.CharField(blank=True,max_length=255,null=True)
    dep_div = models.CharField(blank=True,max_length=255,null=True)
    position = models.CharField(blank=True,max_length=255,null=True)
    version = models.CharField(blank=True,max_length=10,null=True)
    revision = models.CharField(blank=True,max_length=10,null=True)
    effec_date = models.DateField(blank=True,null=True)
    rev_date = models.DateField(blank=True,null=True)
    appr1 = models.ForeignKey(Person,null=True,blank=True)
    appr2 = models.ForeignKey(Person,null=True,blank=True)
    appr3 = models.ForeignKey(Person,null=True,blank=True)
    appr4 = models.ForeignKey(Person,null=True,blank=True)
    appr5 = models.ForeignKey(Person,null=True,blank=True)
    appr6 = models.ForeignKey(Person,null=True,blank=True)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    
    def natural_key(self):
        return (self.id, self.description)
    
    class Meta:
        db_table = u'pes_kgm_jd'
        
    def __unicode__(self):
        return self.description
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Print" target="_blank" href="'''+ reverse('jobdesc_print_pdf',kwargs={'uid': self.id}) +'''"><i class="icon-print icon-large"></i></a>
                    <a title="Edit" target="" href="'''+ reverse('jobdesc_modify',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('jobdesc_delete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    '''
        return write_icons
    
class PesKgmJdUpload(models.Model):
    upload = models.ForeignKey(Fileupload)
    date_from = models.DateField()
    date_to = models.DateField()