from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'knowandguideem/', include('apps.intent.pes.knowandguideem.urls.chris')),
    (r'knowandguideem/', include('apps.intent.pes.knowandguideem.urls.nethan')),
    (r'knowandguideem/', include('apps.intent.pes.knowandguideem.urls.rechie')),
)
urlpatterns += patterns('apps.intent.pes.knowandguideem.views.index',
    url(r'knowandguideem/', 'index', name='knowandguideemindex'),
    
)