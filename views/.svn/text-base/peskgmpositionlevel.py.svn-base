from django.http import HttpResponse
from apps.intent.pes.knowandguideem.models.peskgmpositionlevel import PesKgmPositionLevel
from apps.intent.pes.knowandguideem.forms.peskgmpositionlevel import peskgmpositionlevelForm
from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext    
from django.db.models import Max
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-po-ba-ls',1)
def index(request):
    val = {}
    val['title'] = "PES - Planning & Development - Band"
    val['feature'] = 'positionlevel'
    val['tabgroup'] = 'listgroup'
    val['gridgroup'] = 'subgrid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmPositionLevel.objects.filter(deleted=0), val['feature'], val['gridgroup'])
    return render_to_response('positionlevel/list.html',{'page' : val},context_instance=RequestContext(request))

@access.has_access('kg-po-ba-ls',2)
def create(request):  
    val = {}
    val['title'] = "PES - Planning & Development - Band"
    val['feature'] = 'positionlevel'
    val['tabgroup'] = 'formgroup'
    try:
        if(request.method=='POST'):
            form=peskgmpositionlevelForm(request.POST)
            if(form.is_valid()):
                l = form.save(commit=False)
                l.deleted = 0
                l.save()
                detailed_log(l,request,1)
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=peskgmpositionlevelForm()
                    return render_to_response('positionlevel/form.html',{'form':form, 'create':form,'page' : val,'message':'Position Level has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('positionlevel/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=peskgmpositionlevelForm()
            sequence=PesKgmPositionLevel.objects.all().aggregate(Max('sequence'))['sequence__max']+1
            return render_to_response('positionlevel/form.html',{'form':form, 'create':form,'page' : val,'sequence':sequence},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form=peskgmpositionlevelForm()
        return render_to_response('positionlevel/form.html',{'form':form, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-po-ba-ls',2)
def edit(request,id):
    val = {}
    val['title'] = "PES - Know & Guide 'Em - Band"
    val['feature'] = 'positionlevel'
    val['tabgroup'] = 'formgroup'
    try:
        position_level=PesKgmPositionLevel(pk=id)
        form=peskgmpositionlevelForm(request.POST,instance=position_level)
        if(request.method=='POST'):
    
            if(form.is_valid()):
                form.save(commit=True)
                detailed_log(position_level,request,2)
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    position_level = get_object_or_404(PesKgmPositionLevel, pk=id)
                    form = peskgmpositionlevelForm(instance=position_level)  
                    return render_to_response('positionlevel/form.html',{'form':form, 'edit':form,'id':id,'page' : val,'message':'Position Level has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('positionlevel/form.html',{'form':form, 'edit':form,'id':id,'page' : val,'display_error':'true'},context_instance=RequestContext(request))       
        else:        
            position_level = get_object_or_404(PesKgmPositionLevel, pk=id)
            form = peskgmpositionlevelForm(instance=position_level)  
            sequence=position_level.sequence
            return render_to_response('positionlevel/form.html',{'form':form, 'edit':form,'id':id,'page' : val,'sequence':sequence},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        position_level = get_object_or_404(PesKgmPositionLevel, pk=id)
        form = peskgmpositionlevelForm(instance=position_level)  
        return render_to_response('positionlevel/form.html',{'form':form, 'edit':form,'id':id,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-po-ba-ls',2)
def delete(request,id):
    try:
        #position_level=get_object_or_404(PesKgmPositionLevel, pk=id)
        #position_level.delete()
        try:
            p=PesKgmPositionLevel.objects.get(pk=id).delete()
            detailed_log(p,request,3)
            p.delete()
        except:
            a = PesKgmPositionLevel.objects.get(pk=id)
            desc = a.description + "- (DELETED)"
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        return redirect(index)
    except Exception as error:
        val = {}
        val['title'] = "PES - Know & Guide 'Em - Band"
        val['feature'] = 'positionlevel'
        val['tabgroup'] = 'listgroup' 
        position_level = PesKgmPositionLevel.objects.all().order_by('id')
        return render_to_response('positionlevel/list.html',{'list':position_level,'error':error,'display_error':'true','page':val},context_instance=RequestContext(request))
      
         
    

