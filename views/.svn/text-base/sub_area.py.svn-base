from django.http import HttpResponse
from apps.intent.pes.knowandguideem.models.peskgmlocation import PesSubArea
from apps.intent.pes.knowandguideem.forms.sub_area import PesSubAreaForm

#from apps.intent.party.models.Partyroletype import Partyroletype
#from apps.intent.party.forms.PartyTypeForm import PartyTypeForm
from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext    
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from django.db import  transaction
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('pi-cs-ar-ls',1)
def index(request):
    val = {}
    val['title'] = 'PES - HRIS - Sub-Area'
    val['feature'] = 'sub_area'
    val['tabgroup'] = 'listgroup'
    val['gridgroup'] = 'subgrid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesSubArea.objects.filter(deleted=0), val['feature'], val['gridgroup'])
    return render_to_response('sub_area/list.html',{'page' : val},context_instance=RequestContext(request))

@access.has_access('pi-cs-ar-ls',2)
@transaction.commit_on_success
def create(request):  
    
    val = {}
    val['title'] = 'PES - HRIS - Sub-Area'
    val['feature'] = 'sub_area'
    val['tabgroup'] = 'formgroup'

    try:
        if(request.method=='POST'):
            form=PesSubAreaForm(request.POST)
    
            if(form.is_valid()):
                r = form.save(commit=False)
                r.deleted = 0
                r.save()
                detailed_log(r,request,1)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=PesSubAreaForm()
                    return render_to_response('sub_area/form.html',{'form':form, 'create':form,'page' : val,'message':'Region has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('sub_area/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=PesSubAreaForm()
            return render_to_response('sub_area/form.html',{'form':form, 'create':form,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form=PesSubAreaForm()
        return render_to_response('sub_area/form.html',{'form':form, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('pi-cs-ar-ls',2)
@transaction.commit_on_success
def edit(request,id):  
    val = {}
    val['title'] = 'PES - HRIS - Sub-Area'
    val['feature'] = 'sub_area'
    val['tabgroup'] = 'formgroup'
    try:
        if(request.method=='POST'):
            form=PesSubAreaForm(request.POST, instance=get_object_or_404(PesSubArea, pk=id))
            if form.is_valid() :
                form.save()
                detailed_log(form,request,2)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=PesSubAreaForm(instance=get_object_or_404(PesSubArea, pk=id))
                    return render_to_response('sub_area/form.html',{'form':form, 'edit':form,'id':id, 'page' : val,'message':'Region has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('sub_area/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=PesSubAreaForm(instance=get_object_or_404(PesSubArea, pk=id))
            return render_to_response('sub_area/form.html',{'form':form, 'edit':form,'id':id, 'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form=PesSubAreaForm(instance=get_object_or_404(PesSubArea, pk=id))
        return render_to_response('sub_area/form.html',{'form':form,'e':1,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))


@access.has_access('pi-cs-ar-ls',2)
@transaction.commit_on_success
def delete(request,id):
    try:
        try:
            r=PesSubArea.objects.get(pk=id)
            detailed_log(r,request,2)
            
            PesSubArea.objects.get(pk=id).delete()
        except:
            a = PesSubArea.objects.get(pk=id)
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
        region = PesSubArea.objects.all().order_by('id')
        val = {}
        val['title'] = 'PES - HRIS - Sub-Area'
        val['feature'] = 'sub_area'
        val['tabgroup'] = 'listgroup' 
        return render_to_response('sub_area/list.html',{'list':region,'error':error,'display_error':'true','page':val},context_instance=RequestContext(request))

         
  

