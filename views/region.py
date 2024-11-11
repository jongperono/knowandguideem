from django.http import HttpResponse
from apps.intent.pes.knowandguideem.models.region import Region
from apps.intent.pes.knowandguideem.forms.region import RegionForm
#from apps.intent.party.models.Partyroletype import Partyroletype
#from apps.intent.party.forms.PartyTypeForm import PartyTypeForm
from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext    
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from django.db import  transaction
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log

@access.has_access('pi-cs-ar-ls',1)
def index(request):
    val = {}
    val['title'] = 'PES - HRIS - Area'
    val['feature'] = 'region'
    val['tabgroup'] = 'listgroup'
    val['gridgroup'] = 'subgrid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, Region.objects.filter(deleted=0), val['feature'], val['gridgroup'])

    return render_to_response('region/list.html',{'page' : val},context_instance=RequestContext(request))

@access.has_access('pi-cs-ar-ls',2)
@transaction.commit_on_success
def create(request):  
    
    val = {}
    val['title'] = 'PES - HRIS - Area'
    val['feature'] = 'region'
    val['tabgroup'] = 'formgroup'

    try:
        if(request.method=='POST'):
            form=RegionForm(request.POST)
    
            if(form.is_valid()):
                r = form.save(commit=False)
                r.deleted = 0
                r.save()
                detailed_log(r,request,1)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=RegionForm()
                    return render_to_response('region/form.html',{'form':form, 'create':form,'page' : val,'message':'Region has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('region/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=RegionForm()
            return render_to_response('region/form.html',{'form':form, 'create':form,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form=RegionForm()
        return render_to_response('region/form.html',{'form':form, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('pi-cs-ar-ls',2)
@transaction.commit_on_success
def edit(request,id):  
    val = {}
    val['title'] = 'PES - HRIS - Area'
    val['feature'] = 'region'
    val['tabgroup'] = 'formgroup'
    try:
        if(request.method=='POST'):
            form=RegionForm(request.POST, instance=get_object_or_404(Region, pk=id))
            if form.is_valid() :
                form.save()
                detailed_log(form,request,2)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=RegionForm(instance=get_object_or_404(Region, pk=id))
                    return render_to_response('region/form.html',{'form':form, 'edit':form,'id':id, 'page' : val,'message':'Region has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('region/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=RegionForm(instance=get_object_or_404(Region, pk=id))
            return render_to_response('region/form.html',{'form':form, 'edit':form,'id':id, 'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form=RegionForm(instance=get_object_or_404(Region, pk=id))
        return render_to_response('region/form.html',{'form':form,'e':1,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('pi-cs-ar-ls',2)
@transaction.commit_on_success
def delete(request,id):
    try:
        try:
            r=Region.objects.get(pk=id)
            detailed_log(r,request,2)
            r.delete()
        except:
            a = Region.objects.get(pk=id)
            #region.delete()
            desc = a.description + "- (DELETED)"
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        transaction.commit()
        return redirect(index)
    except Exception as error:
        transaction.rollback()
        region = Region.objects.all().order_by('id')
        val = {}
        val['title'] = 'PES - HRIS - Area'
        val['feature'] = 'steppositionlevel'
        val['tabgroup'] = 'listgroup' 
        return render_to_response('region/list.html',{'list':region,'error':error,'display_error':'true','page':val},context_instance=RequestContext(request))

         
  

