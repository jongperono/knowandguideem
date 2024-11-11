from django.http import HttpResponse
from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevel import PesKgmSteppositionlevel
from apps.intent.pes.knowandguideem.forms.peskgmsteppositionlevel import peskgmsteppositionlevelForm
from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext    
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-po-bl-ls',1)
def index(request):
    val = {}
    val['title'] = "PES - Planning & Development - Band/Level Configuration"
    val['feature'] = 'steppositionlevel'
    val['tabgroup'] = 'listgroup' 
    val['gridgroup'] = 'subgrid'
    #'position_level__sequence','step__sequence'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmSteppositionlevel.objects.filter(deleted=0), val['feature'], val['gridgroup'])
    return render_to_response('steppositionlevel/list.html',{'page' : val},context_instance=RequestContext(request))

@access.has_access('kg-po-bl-ls',2)
def create(request): 
    val = {}
    val['title'] = "PES - Planning & Development - Band/Level Configuration"
    val['feature'] = 'steppositionlevel'
    val['tabgroup'] = 'formgroup' 
    try:
        if(request.method=='POST'):
            form=peskgmsteppositionlevelForm(request.POST)
            if(form.is_valid()):
                p = form.save(commit=False)
                p.deleted = 0
                p.save()
                detailed_log(p,request,1)
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=peskgmsteppositionlevelForm()
                    return render_to_response('steppositionlevel/form.html',{'form':form, 'create':form,'page' : val,'message':'Position Level configuration has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('steppositionlevel/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=peskgmsteppositionlevelForm()
            return render_to_response('steppositionlevel/form.html',{'form':form, 'create':form,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form=peskgmsteppositionlevelForm()
        return render_to_response('steppositionlevel/form.html',{'form':form, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-po-bl-ls',2)
def edit(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Band/Level Configuration"
    val['feature'] = 'steppositionlevel'
    val['tabgroup'] = 'formgroup'
    try:
        position_level=PesKgmSteppositionlevel(pk=id)
        form=peskgmsteppositionlevelForm(request.POST,instance=position_level)
        if(request.method=='POST'):
    
            if(form.is_valid()):
                form.save(commit=True) 
                detailed_log(position_level,request,2)
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    position_level = get_object_or_404(PesKgmSteppositionlevel, pk=id)
                    form = peskgmsteppositionlevelForm(instance=position_level)  
                    return render_to_response('steppositionlevel/form.html',{'form':form, 'edit':form,'id':id,'page' : val,'message':'Position Level configuration has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('steppositionlevel/form.html',{'form':form, 'edit':form,'id':id,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:        
            position_level = get_object_or_404(PesKgmSteppositionlevel, pk=id)
            form = peskgmsteppositionlevelForm(instance=position_level)  
            return render_to_response('steppositionlevel/form.html',{'form':form, 'edit':form,'id':id,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        position_level = get_object_or_404(PesKgmSteppositionlevel, pk=id)
        form = peskgmsteppositionlevelForm(instance=position_level)  
        return render_to_response('steppositionlevel/form.html',{'form':form, 'edit':form,'id':id,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-po-bl-ls',2)
def delete(request,id):
    try:
        #position_level=get_object_or_404(PesKgmSteppositionlevel, pk=id)
        #position_level.delete()
        try:
            p=PesKgmSteppositionlevel.objects.get(pk=id)
            detailed_log(p,request,3)
            p.delete
            
            
        except:
            a = PesKgmSteppositionlevel.objects.get(pk=id)
            #desc = a.description + "- (DELETED)"
            #a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        return redirect(index)
    except Exception as error:
        val = {}
        val['title'] = "PES - Planning & Development - Band/Level Configuration"
        val['feature'] = 'steppositionlevel'
        val['tabgroup'] = 'listgroup' 
        position_level = PesKgmSteppositionlevel.objects.all().order_by('id')
        return render_to_response('steppositionlevel/list.html',{'list':position_level,'error':error,'display_error':'true','page' : val},context_instance=RequestContext(request))

         
    

