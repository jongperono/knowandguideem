from django.http import HttpResponse
from apps.intent.pes.knowandguideem.models.peskgmlocation import PesKgmLocation
from apps.intent.pes.knowandguideem.forms.peskgmlocation import PesKgmLocationForm
from apps.intent.warehouse.forms.locationform import LocationForm
#from apps.intent.party.models.Partyroletype import Partyroletype
#from apps.intent.party.forms.PartyTypeForm import PartyTypeForm
from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext    
from apps.intent.warehouse.models.location import Location
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from django.db.models import Q
from django.db import  transaction
from apps.intent.pes.base.helpers.pesfilters import is_filter_found, get_filter_operator
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('pi-cs-br-ls',1)
def index(request):
    val = {}
    val['title'] = 'PES - HRIS - Branch'
    val['feature'] = 'peskgmlocation'
    val['tabgroup'] = 'listgroup'
    val['gridgroup'] = 'subgrid'
    p={}
    my_param = request.GET.get('i_company')
    
    if my_param:
        p={get_filter_operator(request,'company','party__name', 'location'):request.GET['i_company']}
    
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmLocation.objects.filter(deleted=0).filter(**p), val['feature'], val['gridgroup'])
    return render_to_response('peskgmlocation/list.html',{'page' : val},context_instance=RequestContext(request))


def location_region(request,region_id):
    val = {}
    val['title'] = 'PES - HRIS - Branch'
    val['feature'] = 'peskgmlocation'
    val['tabgroup'] = 'listgroup'
    division = PesKgmLocation.objects.filter(region_id=region_id).order_by('id')
    return render_to_response('peskgmlocation/list.html',{'list':division,'page' : val},context_instance=RequestContext(request))

@access.has_access('pi-cs-br-ls',2)
@transaction.commit_on_success
def create(request):  
    
    val = {}
    val['title'] = 'PES - HRIS - Branch'
    val['feature'] = 'peskgmlocation'
    val['tabgroup'] = 'formgroup'

    try:
        if(request.method=='POST'):
            
            locationform=LocationForm(request.POST)
            peskgmlocationform=PesKgmLocationForm(request.POST)
            if(locationform.is_valid() and peskgmlocationform.is_valid()):
                location=locationform.save(commit=True)
                peskgmlocationform=peskgmlocationform.save(commit=False)
                peskgmlocationform.location_id=location.id
                location.save()
                peskgmlocationform.deleted = 0
                peskgmlocationform.save()
                detailed_log(peskgmlocationform,request,1)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=PesKgmLocationForm()
                    locationform=LocationForm()
                    return render_to_response('peskgmlocation/form.html',{'form':form, 'locationform':locationform, 'create':form,'page' : val,'message':'Location has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('peskgmlocation/form.html',{'form':peskgmlocationform, 'locationform':locationform, 'create':peskgmlocationform,'page' : val},context_instance=RequestContext(request))
        else:
            form=PesKgmLocationForm()
            locationform=LocationForm()
            return render_to_response('peskgmlocation/form.html',{'form':form, 'locationform':locationform, 'create':form,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form=PesKgmLocationForm()
        locationform=LocationForm()
        return render_to_response('peskgmlocation/form.html',{'form':form,'locationform':locationform, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('pi-cs-br-ls',2)
@transaction.commit_on_success
def edit(request,id):  
    val = {}
    val['title'] = 'PES - HRIS - Branch'
    val['feature'] = 'peskgmlocation'
    val['tabgroup'] = 'formgroup'
    try:
        if(request.method=='POST'):
            peskgmlocationform=PesKgmLocationForm(request.POST, instance=get_object_or_404(PesKgmLocation, pk=id))
            location_id=get_object_or_404(PesKgmLocation, pk=id).location_id
            locationform=LocationForm(request.POST, instance=get_object_or_404(Location, pk=location_id))
            if(locationform.is_valid() and peskgmlocationform.is_valid()):
                location=locationform.save(commit=True)
                peskgmlocationform=peskgmlocationform.save(commit=False)
                peskgmlocationform.location_id=location.id
                peskgmlocationform.save()
                detailed_log(peskgmlocationform,request,2)
                transaction.commit()
                return redirect(index)
            else:
                return render_to_response('peskgmlocation/form.html',{'form':peskgmlocationform, 'locationform':locationform, 'create':peskgmlocationform,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=PesKgmLocationForm(instance=get_object_or_404(PesKgmLocation, pk=id))
            location=get_object_or_404(Location, pk=get_object_or_404(PesKgmLocation, pk=id).location_id)
            locationform=LocationForm(instance=location)
            return render_to_response('peskgmlocation/form.html',{'form':form, 'edit':form,'id':id, 'locationform':locationform,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form=PesKgmLocationForm(instance=get_object_or_404(PesKgmLocation, pk=id))
        location_id=get_object_or_404(PesKgmLocation, pk=id).location_id
        locationform=LocationForm(instance=get_object_or_404(Location, pk=location_id))
        return render_to_response('peskgmlocation/form.html',{'form':form,'locationform':locationform, 'e':1,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('pi-cs-br-ls',2)
@transaction.commit_manually()
def delete(request,id):
    try:
        #division=PesKgmLocation.objects.get(pk=id)
        #location_id=division.location_id
        #division.delete()
        #location=Location.objects.get(pk=location_id)
        #location.delete()
        try:
            peskgmlocationform=PesKgmLocation.objects.get(pk=id)
            
            detailed_log(peskgmlocationform,request,2)
            peskgmlocationform.delete()
            
        except:
            a = PesKgmLocation.objects.get(pk=id)
            desc = a.branch_code + "- (DELETED)"
            a.branch_code = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        transaction.commit()
        return redirect(index)
    except Exception as error:
        division = PesKgmLocation.objects.all().order_by('id')
        val = {}
        val['title'] = 'PES - HRIS - Branch'
        val['feature'] = 'steppositionlevel'
        val['tabgroup'] = 'listgroup' 
        return render_to_response('peskgmlocation/list.html',{'list':division,'error':error,'display_error':'true','page':val},context_instance=RequestContext(request))

         
  

