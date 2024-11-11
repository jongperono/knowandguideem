from django.shortcuts import render_to_response
from django.template import RequestContext
#from apps.intent.pes.security.decorator import access

#@access.has_access('kg',1)  
def home(request):
    val = {'title':'PES - Planning & Development', 'feature':'pis_default', 'tabgroup':'listgroup', 'urlargs':{}, 'gridgroup':'jobls'}
    return render_to_response('kgm_default/home.html',{'page':val},context_instance=RequestContext(request))
    #return render_to_response('pis_default/home.html', context_instance=RequestContext(request));

#@access.has_access('kg',1)
def reports(request):
    val = {'title':'PES - Planning & Development - Reports', 'feature':'pis_default', 'tabgroup':'listgroup', 'urlargs':{}, 'gridgroup':'jobls'}
    return render_to_response('kgm_default/home.html',{'page':val},context_instance=RequestContext(request))
    #return render_to_response('kgm_default/reports.html', context_instance=RequestContext(request));