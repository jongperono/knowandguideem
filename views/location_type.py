from apps.intent.warehouse.models.location import Locationtype, Location

from apps.intent.warehouse.forms.locationtypeform import LocationTypeForm
from apps.intent.warehouse.forms.locationform import LocationForm

from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.configs.helpers.session import Get_Session
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
import datetime

@access.has_access('pi-cs-lc-ls',1)
def index(request):
    val = {}
    val['title'] = 'PES - HRIS - Location Type'
    val['feature'] = 'locationtype'
    val['tabgroup'] = 'listgroup'
    val['gridgroup'] = 'subgrid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, Locationtype.objects.filter(deleted=0), val['feature'], val['gridgroup'])
    return render_to_response('locationtype/list.html',{'page' : val},context_instance=RequestContext(request))

@access.has_access('pi-cs-lc-ls',2)
def create(request):
    val = {}
    val['title'] = 'PES - HRIS - Location Type'
    val['feature'] = 'locationtype'
    val['tabgroup'] = 'formgroup'
    
    if request.method == 'POST':
        form = LocationTypeForm(request.POST)
        if form.is_valid():
            locationtype = form.save(commit=False)
            locationtype.deleted = 0
            locationtype.save()
            detailed_log(locationtype,request,1)
            return redirect(index)
        else:
            form = LocationTypeForm()
    else:
        form = LocationTypeForm()
    return render_to_response('locationtype/form.html',{'form':form, 'create':form ,'page' : val},context_instance=RequestContext(request))

@access.has_access('pi-cs-lc-ls',2)
def edit(request,id):
    val = {}
    val['title'] = 'PES - HRIS - Location Type'
    val['feature'] = 'locationtype'
    val['tabgroup'] = 'formgroup'
    locationtype = Locationtype.objects.get(pk=id)
    form = LocationTypeForm(request.POST,instance=locationtype)
    if request.method == 'POST':
        form.save()
        detailed_log(form,request,2)
        return redirect(index)
    else:
        form = LocationTypeForm(instance=locationtype)
    return render_to_response('locationtype/form.html',{'form':form,'edit':locationtype,'id':id,'page' : val},context_instance=RequestContext(request))

@access.has_access('pi-cs-lc-ls',2)
def delete(request,id):
    try:
        try:
            form=Locationtype.objects.get(pk=id)
            detailed_log(form,request,3)
            form.delete()
        except:
            a = Locationtype.objects.get(pk=id)
            desc = a.description + "- (DELETED)"
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        return redirect(index)
    except:
        return render_to_response('locationtype/list.html',{'error':1},context_instance=RequestContext(request))