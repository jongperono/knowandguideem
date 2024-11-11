from django.db import models
from django.core.urlresolvers import reverse
from apps.intent.pes.knowandguideem.models.peskgmto import PesKgmTo
from apps.intent.pes.knowandguideem.models.peskgmlocation import PesKgmLocation
from apps.intent.pes.knowandguideem.models.peskgmemploymentstatus import PesKgmEmploymentStatus
from apps.intent.pes.knowandguideem.models.peskgmhierarchy import PesKgmHierarchy
from apps.intent.pes.base.helpers.rpb import get_hierarchy_parents2
from apps.intent.pes.base.helpers.rpb import get_to_parents2
import unicodedata
import datetime

class PesKgmRpb(models.Model):
    auto_CHOICES =((1,'Yes'),(0,'No'))
    code = models.CharField(blank=False,max_length=50,unique=True)
    description = models.CharField(blank=False,max_length=255)
    to = models.ForeignKey(PesKgmTo, null=False, blank=False,on_delete=models.PROTECT)
    required_count = models.IntegerField(null=False, blank=False)
    current_count = models.IntegerField(null=True, blank=True, default=0)
    pes_location = models.ForeignKey(PesKgmLocation, null=False, blank=False,on_delete=models.PROTECT)
    empoyment_status = models.ForeignKey(PesKgmEmploymentStatus, null=False, blank=False,on_delete=models.PROTECT)
    autoreplenish = models.IntegerField(null=False, blank=False,choices=auto_CHOICES)
    hierarchy = models.ForeignKey(PesKgmHierarchy,null=False,blank=False,on_delete=models.PROTECT)
    datefrom = models.DateField(null=False, blank=False)
    dateto = models.DateField(null=False, blank=False)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    da_count = models.IntegerField(null=True,blank=True)
    temp = models.IntegerField(null=True,blank=True,choices=auto_CHOICES)
    
    class Meta:
        db_table = u'pes_kgm_rpb'
    
    def __unicode__(self):
        #return self.code
        return self.code.encode('ascii','ignore') 
    
    @property
    def present_count(self):
        #return 0
        #print self.pk
        #print datetime.date.today()
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute('''SELECT COUNT(*) FROM pes_pis_cds,pes_kgm_rpb_employment_status 
                        WHERE pes_pis_cds.employmentstat_id = pes_kgm_rpb_employment_status.id
                        AND pes_pis_cds.rpb_id = %s
                        AND ( pes_pis_cds.contract_end_date >= %s
                        OR pes_pis_cds.contract_end_date IS NULL )''', (self.pk, datetime.date.today()));
        count = cursor.fetchone() 
        return int(count[0])
    
    @property
    def present_count2(self):
        #return 0
        #print self.pk
        dategiven = datetime.date.today() + datetime.timedelta(days=30)
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute('''SELECT COUNT(*) FROM pes_pis_cds,pes_kgm_rpb_employment_status 
                        WHERE pes_pis_cds.employmentstat_id = pes_kgm_rpb_employment_status.id
                        AND pes_pis_cds.rpb_id = %s
                        AND ( pes_pis_cds.contract_end_date >= %s
                        OR pes_pis_cds.contract_end_date IS NULL )''', (self.pk, dategiven));
        count = cursor.fetchone() 
        return int(count[0])
    
    @property
    def balance_count(self):
        return self.required_count - self.present_count
    
    @property
    def balance_count2(self):
        return self.required_count - self.present_count2

    @property
    def selectem_action(self):
        balance=self.required_count - self.present_count2
        html=""
        if balance>0:
            html='<i id="select_rpb-'+str(self.id)+'" class="icon-thumbs-up-alt icon-large select_rpb"></i>'
        return html
    
    @property
    def hierarchy_tree(self):
        html = '<a href="'+ reverse('pes_rpb_hierarchy',kwargs={'id': self.id}) +'">'+ self.hierarchy.description + "</a>" + ' <i id="id_hierarchy_'+str(self.pk)+'" class="icon-info-sign id_hierarchy" title="Other Info" pid="'+str(self.pk)+'" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus." data-placement="top" data-toggle="popover" data-selector="true" data-trigger="manual" data-popover-status="0"> </i>'
        return html
        #return self.hierarchy.tree
        #return get_hierarchy_parents(self.hierarchy_id)
    
    @property
    def hierarchytree(self):
        return get_hierarchy_parents2(self.hierarchy_id)
    
    @property
    def auto(self):
        if self.autoreplenish == 1:
            return 'Yes'
        else:
            return 'No'
    
    @property
    def da_totalcount(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute('''SELECT COUNT(*) FROM pes_pis_dalist 
                        WHERE rpb_id = %s AND status = %s''', (self.pk, 1));
        count = cursor.fetchone() 
        return int(count[0])
    
    @property
    def to_name(self):
        html = '<a href="'+ reverse('pes_rpb_to',kwargs={'id': self.id}) +'">'+ self.to.description + "</a>" + ' <i id="id_to_'+str(self.pk)+'" class="icon-info-sign id_to" title="Other Info" pid="'+str(self.pk)+'" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus." data-placement="top" data-toggle="popover" data-selector="true" data-trigger="manual" data-popover-status="0"> </i>'
        return html
        #return self.to.tree
        #return get_to_parents(self.to_id)
    
    @property
    def totree(self):
        return get_to_parents2(self.to_id)
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):        
        write_icons = '''
                    <a title="Edit" target="" href="'''+ reverse('rpb_modify',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                    <a title="Delete" target="" modal-link="'''+ reverse('rpb_delete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                    <a title="Download" target="" href="'''+ reverse('rpb_tagged_associates_dl',kwargs={'id': self.id}) +'''"><i class="icon-file-text icon-large"></i></a>
                    '''
        return write_icons