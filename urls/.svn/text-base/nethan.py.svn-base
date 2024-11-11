from django.conf.urls import patterns,url

urlpatterns = patterns('apps.intent.pes.knowandguideem.views.step',
    url(r'step/index/$', 'pes_step_list', name='step_list'),
    url(r'step/create$', 'pes_step_create', name='step_create'),
    url(r'step/modify/(?P<id>\d+)$', 'pes_step_modify', name='step_modify'),
    url(r'step/delete/(?P<id>\d+)$', 'pes_step_delete', name='step_delete'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.to',
    url(r'to/index/$', 'pes_to_list', name='to_list'),
    url(r'to/create$', 'pes_to_create', name='to_create'),
    url(r'to/modify/(?P<id>\d+)$', 'pes_to_modify', name='to_modify'),
    url(r'to/delete/(?P<id>\d+)$', 'pes_to_delete', name='to_delete'),
    url(r'to/treeview/$', 'pes_to_treeview', name='to_treeview'),
    url(r'to/treeview/(?P<id>\d+)$', 'pes_to_treeview_create', name='to_treeview_create'),
    url(r'to/treeview/edit/(?P<id>\d+)$', 'pes_to_treeview_edit', name='to_treeview_edit'),
    url(r'to/treeview/delete/(?P<id>\d+)$', 'pes_to_treeview_del', name='to_treeview_del'),
    url(r'to/(?P<id>\d+)$', 'pes_to_info', name='to_info'),
    url(r'to/(?P<id>\d+)/upload$', 'pes_to_info_upload', name='to_info_upload'),
    url(r'to/download/(?P<id>\d+)$', 'pes_to_file_download', name='to_file_download'),
    url(r'to/archive/$', 'pes_to_archive', name='to_archive'),
    url(r'to/archive/(?P<to_id>\d+)/(?P<id>\d+)$', 'pes_to_archive_upload', name='to_archive_upload'),
    url(r'to/restore/(?P<id>\d+)$', 'pes_to_restore_upload', name='to_restore_upload'),
    url(r'to/rpb/(?P<id>\d+)$', 'pes_rpb_to', name='pes_rpb_to'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.rpb',
    url(r'rpb/index/$', 'pes_rpb_list', name='rpb_list'),
    url(r'rpb/dummy/$', 'pes_rpb_list_dummy', name='rpb_list_dummy'),
    url(r'rpb/create/$', 'pes_rpb_create', name='rpb_create'),
    url(r'rpb/modify/(?P<id>\d+)$', 'pes_rpb_modify', name='rpb_modify'),
    url(r'rpb/delete/(?P<id>\d+)$', 'pes_rpb_delete', name='rpb_delete'),
    url(r'rpb/(?P<id>\d+)$', 'pes_rpb_info', name='rpb_info'),
    url(r'rpb/(?P<id>\d+)/upload$', 'pes_rpb_info_upload', name='rpb_info_upload'),
    url(r'rpb/download/(?P<id>\d+)$', 'pes_rpb_file_download', name='rpb_file_download'),
    url(r'rpb/archive/$', 'pes_rpb_archive', name='rpb_archive'),
    url(r'rpb/archive/(?P<rpb_id>\d+)/(?P<id>\d+)$', 'pes_rpb_archive_upload', name='rpb_archive_upload'),
    url(r'rpb/restore/(?P<id>\d+)$', 'pes_rpb_restore_upload', name='rpb_restore_upload'),
    url(r'rpb/hierarchy/(?P<id>\d+)$', 'pes_rpb_hierarchy', name='pes_rpb_hierarchy'),
    url(r'rpb/toinfo/(?P<uid>\d+)$', 'to_info', name='pes_rpb_toinfo'),
    url(r'rpb/toinfo2/(?P<uid>\d+)$', 'to_info2', name='pes_rpb_toinfo2'),
    url(r'rpb/hierarchyinfo/(?P<uid>\d+)$', 'hierarchy_info', name='pes_rpb_hierarchyinfo'),
    url(r'rpb/report/$', 'rpb_report', name='pes_rpb_report'),
    url(r'rpb/assocdl/(?P<id>\d+)/$', 'rpb_tagged_associates', name='rpb_tagged_associates_dl'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.salarycategory',
    url(r'salarycat/index/$', 'pes_salarycat_list', name='salarycat_list'),
    url(r'salarycat/create/$', 'pes_salarycat_create', name='salarycat_create'),
    url(r'salarycat/modify/(?P<id>\d+)$', 'pes_salarycat_modify', name='salarycat_modify'),
    url(r'salarycat/delete/(?P<id>\d+)$', 'pes_salarycat_delete', name='salarycat_delete'),
    url(r'salarycat/archive/(?P<id>\d+)$', 'pes_salarycat_archive', name='salarycat_archive'),
    url(r'reports/salarycat/$', 'report', name='salarycat_report'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.jobdescription',
    url(r'jobdesc/index/$', 'pes_jobdesc_list', name='jobdesc_list'),
    url(r'jobdesc/create$', 'pes_jobdesc_create', name='jobdesc_create'),
    url(r'jobdesc/modify/(?P<id>\d+)$', 'pes_jobdesc_modify', name='jobdesc_modify'),
    url(r'jobdesc/delete/(?P<id>\d+)$', 'pes_jobdesc_delete', name='jobdesc_delete'),
    url(r'jobdesc/(?P<id>\d+)$', 'pes_jobdesc_info', name='jobdesc_info'),
    url(r'jobdesc/(?P<id>\d+)/upload$', 'pes_jobdesc_info_upload', name='jobdesc_info_upload'),
    url(r'jobdesc/download/(?P<id>\d+)$', 'pes_jobdesc_file_download', name='jobdesc_file_download'),
    url(r'jobdesc/archive/$', 'pes_jobdesc_archive', name='jobdesc_archive'),
    url(r'jobdesc/archive/(?P<jd_id>\d+)/(?P<id>\d+)$', 'pes_jobdesc_archive_upload', name='jobdesc_archive_upload'),
    url(r'jobdesc/restore/(?P<id>\d+)$', 'pes_jobdesc_restore_upload', name='jobdesc_restore_upload'),
    url(r'jobdesc/arch_del/(?P<id>\d+)$', 'jd_archive_delete', name='jobdesc_archive_delete'),
    url(r'jobdesc/print/(?P<uid>\d+)$', 'pes_jobdesc_print', name='jobdesc_print_pdf'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.steppositionlevel_cat',
    url(r'salarycat/splcat/(?P<id>\d+)$', 'pes_splcat_list', name='splcat_list'),
    url(r'salarycat/splcat/create/(?P<id>\d+)$', 'pes_splcat_create', name='splcat_create'),
    url(r'salarycat/splcat/modify/(?P<id>\d+)$', 'pes_splcat_modify', name='splcat_modify'),
    url(r'salarycat/splcat/delete/(?P<id>\d+)$', 'pes_splcat_delete', name='splcat_delete'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.compenmaintenance',
    url(r'compen/list/$', 'index', name='compen_list'),
    url(r'compen/edit/$', 'add', name='compen_add'),
    url(r'compen/dtl/(?P<id>\d+)/$', 'allow_index', name='compen_dtl'),
    url(r'compen/dtl_create/(?P<id>\d+)/$', 'allow_create', name='compen_dtl_create'),
    url(r'compen/dtl_edit/(?P<id>\d+)/$', 'allow_edit', name='compen_dtl_edit'),
    url(r'compen/dtl_delete/(?P<id>\d+)/$', 'allow_delete', name='compen_dtl_delete'),
    url(r'compen/dtlpa/(?P<id>\d+)/$', 'allow_pa_index', name='compen_pa_dtl'),
    url(r'compen/dtlpa_create/(?P<id>\d+)/$', 'allow_pa_create', name='compen_pa_dtl_create'),
    url(r'compen/dtlpa_edit/(?P<id>\d+)/$', 'allow_pa_edit', name='compen_pa_dtl_edit'),
    url(r'compen/dtlpa_delete/(?P<id>\d+)/$', 'allow_pa_delete', name='compen_pa_dtl_delete'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.peskgmviewrpb',
    url(r'viewrpb/list/$', 'index', name='viewrpb_list'),
    url(r'viewrpb/add/$', 'create', name='viewrpb_create'),
    url(r'viewrpb/edit/(?P<id>\d+)/$', 'edit', name='viewrpb_modify'),
    url(r'viewrpb/delete/(?P<id>\d+)/$', 'delete', name='viewrpb_delete'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.rpb',
    url(r'reports/rpb/$', 'rpb_report2', name='kgm_rpb_report2'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.peskgmreport',
    url(r'reports/generic/$', 'report', name='kgm_report_generic'),
)

urlpatterns += patterns('apps.intent.pes.selectem.views.pes_selectem_masterfile',
    url(r'skillset/masterfile/list/(?P<uid>\d+)/$', 'index', name='selectem_master_list'),
    url(r'skillset/masterfile/add/(?P<uid>\d+)/$', 'create', name='selectem_master_create'),
    url(r'skillset/masterfile/edit/(?P<id>\d+)/$', 'edit', name='selectem_master_edit'),
    url(r'skillset/masterfile/delete/(?P<id>\d+)/$', 'delete', name='selectem_master_delete'),
    url(r'skillset/list/$', 'index1', name='selectem_skillset_list'),
    url(r'skillset/add/$', 'create1', name='selectem_skillset_create'),
    url(r'skillset/edit/(?P<id>\d+)/$', 'edit1', name='selectem_skillset_edit'),
    url(r'skillset/delete/(?P<id>\d+)/$', 'delete1', name='selectem_skillset_delete'),
    )

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.documentation',
    url(r'documentation/list/$', 'index', name='kgm_documentation_list'),
)