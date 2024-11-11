from django.shortcuts import render_to_response
from django.template import RequestContext

#models
from apps.intent.pes.miscellaneous.models.pesmisc_upload_documents import PesMiscUploadDocuments
#helpers
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
from apps.intent.pes.base.helpers.pes_session import get_person_id
from apps.intent.pes.pis.models.pespiscds import PesPisCds

@access.has_access('kg-ud-ls',1)
def index(request):
    s = {'is_dos__in':[0,2]}
    person_id = get_person_id(request)
    cds = PesPisCds.objects.get(person_id=person_id)
    if cds.rpb_id:
        if cds.rpb.hierarchy.company_id == 433:
            s = {'is_dos__in':[0,1]}
    filter_dic = {}
    filter_dic['type__lte'] = cds.position.category
    #print filter_dic
    val = {}
    val['title'] = "PES - Planning & Development - Documents"
    val['feature'] = 'documentation'
    val['tabgroup'] = 'listgroup'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesMiscUploadDocuments.objects.filter(module=4).filter(**s).filter(**filter_dic), val['feature'], val['gridgroup'])
    return render_to_response('documentation/list.html',{'page':val},context_instance=RequestContext(request))