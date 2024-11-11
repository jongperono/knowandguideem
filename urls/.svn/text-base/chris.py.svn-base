from django.conf.urls import patterns, url


urlpatterns = patterns('apps.intent.pes.knowandguideem.views.steppositionlevel',
	url(r'steppositionlevel/index/$', 'index', name='steppositionlevellist'),
	url(r'steppositionlevel/form/create/$', 'create', name='createstepposition'),
	url(r'steppositionlevel/form/edit/(?P<id>\d+)', 'edit', name='editstepposition'),
	url(r'steppositionlevel/form/delete/(?P<id>\d+)', 'delete', name='deletestepposition'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.peskgmhierarchy',
	url(r'update_hierarchy/update_hierarchy/$', 'update_hierarchy', name='update_hierarchy'),
	
)


urlpatterns += patterns('apps.intent.pes.knowandguideem.views.peskgmpositionlevel',
	url(r'positionlevel/index/$', 'index', name='positionlevellist'),
	url(r'positionlevel/form/create/$', 'create', name='createposition'),
	url(r'positionlevel/form/edit/(?P<id>\d+)', 'edit', name='editposition'),
	url(r'positionlevel/form/delete/(?P<id>\d+)', 'delete', name='deleteposition'),
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.peskgmcompanyscope',
	url(r'pescompanyscope/$', 'index', name='pescompanyscopelist'),
	url(r'pescompanyscope/create/$', 'create', name='pescompanyscopecreate'),
	url(r'pescompanyscope/edit/(?P<id>\d+)', 'edit', name='pescompanyscopeedit'),
	url(r'pescompanyscope/delete/(?P<id>\d+)', 'delete', name='pescompanyscopedelete'),	
)


urlpatterns += patterns('apps.intent.pes.knowandguideem.views.peskgmpositionclassification',
	url(r'positionclassification/index/$', 'index', name='positionclassificationlist'),
	url(r'positionclassification/form/create/$', 'create', name='positionclassificationcreate'),
	url(r'positionclassification/form/edit/(?P<id>\d+)', 'edit', name='positionclassificationedit'),
	url(r'positionclassification/form/delete/(?P<id>\d+)', 'delete', name='positionclassificationdelete'),
	url(r'reports/positionclassification/', 'report', name='positionclassificationreport'),		
)

urlpatterns += patterns('apps.intent.pes.knowandguideem.views.peskgmhierarchy',
    url(r'peskgmhierarchy/index/$', 'index', name='peskgmhierarchylist'),
    url(r'peskgmhierarchy/treeview$', 'tree_view', name='peskgmhierarchytreeviewlist'),
    url(r'peskgmhierarchy/form/create/$', 'create', name='peskgmhierarchycreate'),
    url(r'peskgmhierarchy/form/edit/(?P<id>\d+)', 'edit', name='peskgmhierarchyeedit'),
    
    url(r'peskgmhierarchy/form/edit_treeview/(?P<id>\d+)', 'edit_treeview', name='peskgmhierarchyeedittreeview'),
    

    url(r'peskgmhierarchy/form/treeview/add/(?P<id>\d+)/', 'tree_view_add', name='peskgmhierarchytreeviewaddlist'),
    
    url(r'peskgmhierarchy/form/delete/(?P<id>\d+)', 'delete', name='peskgmhierarchydelete'),    
    url(r'peskgmhierarchy/form/deletetree/(?P<id>\d+)', 'delete_tree', name='peskgmhierarchydeletetree'),
    url(r'reports/hierarchy/$', 'report', name='kgm_companystructure_report'),
    
    
)


urlpatterns += patterns('apps.intent.pes.knowandguideem.views.peskgmhierarchytype',
    url(r'hierarchytype/index/$', 'index', name='hierarchytypelist'),
    url(r'hierarchytype/form/create/$', 'create', name='hierarchytypecreate'),
    url(r'hierarchytype/form/edit/(?P<id>\d+)', 'edit', name='hierarchytypeedit'),
    url(r'hierarchytype/form/delete/(?P<id>\d+)', 'delete', name='hierarchytypedelete'),    
)