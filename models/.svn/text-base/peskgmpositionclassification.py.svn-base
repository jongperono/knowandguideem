from django.db import models
from apps.intent.pes.knowandguideem.models.peskgmto import PesKgmTo
from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevel import PesKgmSteppositionlevel
#helpers
from apps.intent.pes.base.helpers.rpb import get_to_parents
from django.core.urlresolvers import reverse

class PesKgmPositionClassification(models.Model):
    status_CHOICES =((1,'Active'),(0,'Inactive'))
    category_CHOICES = ((1,'General Associate'),
                        (2,'Supervisor'),
                        (3,'Manager'),
                        (4,'Board Of Director')
                        )
    code = models.CharField(blank=True, null=True,max_length=50,unique=True)
    to = models.ForeignKey(PesKgmTo,on_delete=models.PROTECT)
    description = models.CharField(max_length=180)
    start_step_position_level = models.ForeignKey(PesKgmSteppositionlevel,on_delete=models.PROTECT)
    deleted = models.IntegerField(null=False,blank=False,default=0)
    date_del = models.DateField(null=True,blank=True)
    status = models.IntegerField(choices=status_CHOICES)
    category = models.IntegerField(default=1,choices=category_CHOICES)
    #end_step_position_level = models.ForeignKey(PesKgmSteppositionlevel,null=True,blank=True)
    class Meta:
        db_table = u'pes_kgm_position_classification'
    
    @property
    def to_name(self):
        html = '<a href="'+ reverse('to_treeview')+str("#ul-"+str(self.to_id)) +'">'+ self.to.description + "</a>" + ' <i id="id_to_'+str(self.to_id)+'" class="icon-info-sign id_to" title="Other Info" pid="'+str(self.to_id)+'" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus." data-placement="top" data-toggle="popover" data-selector="true" data-trigger="manual" data-popover-status="0"> </i>'
        return html
        #return self.to.tree
        #return get_to_parents(self.to_id)
    
    def __unicode__(self):
        return self.description
    
    def natural_key(self):
        return (self.id, self.description)
    
    @property
    def statusname(self):
        if self.status == 0:
            return 'Inactive'
        elif self.status == 1:
            return 'Active'
        
    @property
    def categoryname(self):
        if self.category == 1:
            return 'General Associate'
        elif self.category == 2:
            return 'Supervisor'
        elif self.category == 3:
            return 'Manager'
        elif self.category == 4:
            return 'Board Of Director'
        else:
            return '-'
    
    @property
    def ctrlbtn_r(self):
        return ''
    
    @property
    def ctrlbtn_w(self):
        if self.status == 1:
            write_icons = '''
                        <a title="Edit" target="" href="'''+ reverse('positionclassificationedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                        '''
        elif self.status == 0:
            write_icons = '''
                        <a title="Edit" target="" href="'''+ reverse('positionclassificationedit',kwargs={'id': self.id}) +'''"><i class="icon-edit icon-large"></i></a>
                        <a title="Delete" target="" modal-link="'''+ reverse('positionclassificationdelete',kwargs={'id': self.id}) +'''" href="#" modal-body="Are you sure to delete this entry?" modal-title="Confirm Delete:" class="confirm_page_link"><i class="icon-trash icon-large"></i></a>
                        '''
        return write_icons