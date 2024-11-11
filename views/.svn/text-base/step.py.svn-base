from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.db import transaction
from django.http import Http404
from django.db.models import Max
import datetime
#models
from apps.intent.pes.knowandguideem.models.peskgmstep import PesKgmStep

#forms
from apps.intent.pes.knowandguideem.forms.step import StepForm
#helpers
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-po-lv-ls',1)
def pes_step_list(request):
    val = {}
    val['title'] = "PES - Planning & Development - Level"
    val['feature'] = 'step'
    val['tabgroup'] = 'listgroup'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmStep.objects.filter(deleted=0), val['feature'], val['gridgroup'])
    return render_to_response('step/steplist.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-po-lv-ls',2)
@transaction.commit_on_success
def pes_step_create(request):
    val = {}
    val['title'] = "PES - Planning & Development - Level"
    val['feature'] = 'step'
    val['tabgroup'] = 'creategroup'
    try:
        if request.method == 'POST':
            form = StepForm(request.POST)
            if form.is_valid():
                step = form.save(commit=False)
                step.deleted = 0
                step.save()
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(pes_step_list)
                else:
                    form = StepForm()
                    return render_to_response('step/stepform.html',{'form':form,'page':val,'message':1},context_instance=RequestContext(request))
            else:
                return render_to_response('step/stepform.html',{'form':form,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            #form = StepForm()
            #step = PesKgmStep.objects.all().aggregate(Max('sequence'))['sequence__max']+1
            form = StepForm()
        return render_to_response('step/stepform.html',{'form':form,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form = StepForm()
        return render_to_response('step/stepform.html',{'form':form,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-po-lv-ls',2)
@transaction.commit_on_success
def pes_step_modify(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Level"
    val['feature'] = 'step'
    val['tabgroup'] = 'creategroup'
    Step = PesKgmStep.objects.get(pk=id)
    form=StepForm(request.POST,instance=Step)
    try:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                transaction.commit()
                return redirect(pes_step_list)
            else:
                return render_to_response('step/stepform.html',{'form':form,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            form = StepForm(instance=Step)
        return render_to_response('step/stepform.html',{'form':form,'Edit':Step,'id':id,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        Step = PesKgmStep.objects.get(pk=id)
        form = StepForm(instance=Step)
        return render_to_response('step/stepform.html',{'form':form,'Edit':Step,'id':id,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-po-lv-ls',2)
@transaction.commit_on_success
def pes_step_delete(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Level'
    val['feature'] = 'step'
    val['tabgroup'] = 'listgroup'
    try:
        try:
            PesKgmStep.objects.get(pk=id,status=0).delete()
        except:
            a = PesKgmStep.objects.get(pk=id,status=0)
            desc = a.description + "- (DELETED)"
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        transaction.commit()
        return redirect(pes_step_list)
    except Exception as error:
        transaction.rollback()
        Step = PesKgmStep.objects.all()
        return render_to_response('step/steplist.html',{'list': Step,'error':error,'page':val,'display_error':1},context_instance=RequestContext(request))
        #return render_to_response('address/list.html',{'error':1},context_instance=RequestContext(request))
