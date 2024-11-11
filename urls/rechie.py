from django.conf.urls import patterns,url

urlpatterns = patterns('apps.intent.pes.knowandguideem.views.peskgmcashgift',
    url(r'pmsrating/list/$', 'ls', name='pes_kgm_cg_list'),
    url(r'pmsrating/add/$', 'add', name='pes_kgm_cg_add'),
    url(r'pmsrating/assoc/$', 'associates', name='pes_kgm_cg_assoc'),
    url(r'pmsrating/ul/$', 'upload', name='pes_kgm_cg_upload'),
    url(r'pmsrating/del/(?P<uid>\d+)$', 'delete', name='pes_kgm_cg_del'),
    url(r'pmsrating/edit/(?P<uid>\d+)$', 'edit', name='pes_kgm_cg_edit'),
    url(r'pmsrating/filesubmit/(?P<uid>\d+)$', 'filesubmit', name='pes_kgm_cg_submit'),
    url(r'pmscgtbl/list/$', 'tbl', name='pes_kgm_cg_table'),
    url(r'pmscgtbl/listedit/(?P<uid>\d+)$', 'tbl_edit', name='pes_kgm_cg_table_edit'),
    url(r'pmscgtbl/view/(?P<uid>\d+)$', 'tblview', name='pes_kgm_cg_tableview'),
    url(r'pmscgtbl/viewform/(?P<uid>\d+)$', 'tblview_add', name='pes_kgm_cg_tableview_add'),
    url(r'pmscgtbl/viewform/edit/(?P<uid>\d+)$', 'tblview_edit', name='pes_kgm_cg_tableview_edit'),
    url(r'pmscgtbl/lockdate/$', 'lockdate', name='pes_kgm_cg_lockdate'),
    url(r'pmscgtbl/lockdate/edit/$', 'lockdateedit', name='pes_kgm_cg_lockdateedit'),
    url(r'pmscgtbl/rating/$', 'ratetbl', name='pes_kgm_cg_ratetbl'),
    url(r'pmscgtbl/ratingadd/$', 'ratetbl_add', name='pes_kgm_cg_ratetbl_add'),
    url(r'pmscgtbl/ratingadd/(?P<uid>\d+)$', 'ratetbl_edit', name='pes_kgm_cg_ratetbl_edit'),
    
    url(r'reports/cg/$', 'masterlist', name='pes_kgm_cg_masterlist'),
    
    url(r'newcgtbl/list/$', 'company_dtl', name='pes_kgm_cg_cmpy_dtl'),
    url(r'newcgtbl/listedit/(?P<uid>\d+)$', 'company_dtl_edit', name='pes_kgm_cg_cmpy_dtl_edit'),
    url(r'newcgtbl/lockdate/$', 'new_lockdate', name='pes_kgm_cg_new_lockdate'),
    url(r'newcgtbl/lockdate/edit/$', 'new_lockdateedit', name='pes_kgm_cg_new_lockdateedit'),
    url(r'newcgtbl/rating/$', 'new_ratetbl', name='pes_kgm_cg_new_ratetbl'),
    url(r'newcgtbl/ratingedit/(?P<uid>\d+)$', 'new_ratetbl_edit', name='pes_kgm_cg_new_ratetbl_edit'),
    
    # PAF automation URL
    url(r'paf/list/$', 'ls_paf', name='pes_kgm_cg_list_paf'),
    url(r'paf/add/$', 'add_paf', name='pes_kgm_cg_add_paf'),
    
    
)