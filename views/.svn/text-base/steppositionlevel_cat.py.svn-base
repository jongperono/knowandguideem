from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.core.urlresolvers import reverse
from django.db import transaction
#models
from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevecategory import PesKgmSteppositionlevelCategory
from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevecategory import PesKgmSalarycategory
#forms
from apps.intent.pes.knowandguideem.forms.steppositionlevel_catform import StepPositionLevelCatForm
#helper
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
from apps.intent.pes.security.helpers.access import get_extra_par
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-cm-ss-ls',1)
def pes_splcat_list(request,id):
    temp = get_extra_par(request,"max_band_level")
    val = {}
    val['title'] = "PES - Planning & Development - Salary Structure Details"
    val['feature'] = 'steppositionlevel_cat'
    val['tabgroup'] = 'listspl'
    val['urlargs'] = {'urlarg1':{'id':id}}
    val['gridgroup'] = 'grid'
    if temp:
        val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmSteppositionlevelCategory.objects.filter(salary_category=id,deleted=0).filter(salary_category__band__lte=temp), val['feature'], val['gridgroup'])
    else:
        val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmSteppositionlevelCategory.objects.filter(salary_category=id,deleted=0), val['feature'], val['gridgroup'])
    salary_cat = PesKgmSalarycategory.objects.get(pk=id)
    return render_to_response('steppositionlevel_cat/list.html',{'page':val,'x':salary_cat},context_instance=RequestContext(request))

@access.has_access('kg-cm-ss-ls',2)
@transaction.commit_on_success
def pes_splcat_create(request,id):
    salary_cat = PesKgmSalarycategory.objects.get(pk=id)
    val = {}
    val['title'] = "PES - Planning & Development - Salary Structure Details"
    val['feature'] = 'steppositionlevel_cat'
    val['tabgroup'] = 'createspl'
    val['urlargs'] = {'urlarg1':{'id':salary_cat.id}}
    try:
        if request.method == 'POST':
            form = StepPositionLevelCatForm(request.POST)
            if form.is_valid():
                splcat = form.save(commit=False)
                if form.cleaned_data['basic'] < 0 or form.cleaned_data['cola'] < 0 or form.cleaned_data['allowance'] < 0 or form.cleaned_data['maximum'] < 0:
                    raise Exception("You have a negative value. Please check your entry.")
                if form.cleaned_data['maximum'] >= form.cleaned_data['basic']:
                    splcat.salary_category_id = id
                    splcat.deleted = 0
                    splcat.save()
                    detailed_log(splcat,request,1)
                    transaction.commit()
                    if request.POST['save']=="save":
                        return HttpResponseRedirect(reverse('splcat_list',kwargs={'id': id}))
                    else:
                        form = StepPositionLevelCatForm()
                        return render_to_response('steppositionlevel_cat/form.html',{'form':form,'page':val,'x':salary_cat,'id':id,'message':1},context_instance=RequestContext(request))
                else:
                    error = 'Hiring/Minimum is greater than Maximum. Please check your entry.'
                    return render_to_response('steppositionlevel_cat/form.html',{'form':form,'page':val,'x':salary_cat,'id':id,'error':error,'display_error':1},context_instance=RequestContext(request))
            else:
                return render_to_response('steppositionlevel_cat/form.html',{'form':form,'page':val,'x':salary_cat,'id':id,'display_error':1},context_instance=RequestContext(request))
        else:
            form = StepPositionLevelCatForm()
        return render_to_response('steppositionlevel_cat/form.html',{'form':form,'page':val,'x':salary_cat,'id':id},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form = StepPositionLevelCatForm()
        return render_to_response('steppositionlevel_cat/form.html',{'form':form,'page':val,'x':salary_cat,'id':id,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-cm-ss-ls',2)
@transaction.commit_on_success
def pes_splcat_modify(request,id):
    SPLCAT = PesKgmSteppositionlevelCategory.objects.get(pk=id)
    val = {}
    val['title'] = "PES - Planning & Development - Salary Structure Details"
    val['feature'] = 'steppositionlevel_cat'
    val['tabgroup'] = 'createspl'
    val['urlargs'] = {'urlarg1':{'id':SPLCAT.salary_category.id}}
    pid = SPLCAT.salary_category.id
    form=StepPositionLevelCatForm(request.POST,instance=SPLCAT)
    try:
        if request.method == 'POST':
            form=StepPositionLevelCatForm(request.POST,instance=SPLCAT)
            if form.is_valid():
                x = form.save(commit=False)
                if form.cleaned_data['basic'] < 0 or form.cleaned_data['cola'] < 0 or form.cleaned_data['allowance'] < 0 or form.cleaned_data['maximum'] < 0:
                    raise Exception("You have a negative value. Please check your entry.")
                if form.cleaned_data['maximum'] >= form.cleaned_data['basic']:
                    x.save()
                    detailed_log(SPLCAT,request,1)
                    transaction.commit()
                    return HttpResponseRedirect(reverse('splcat_list',kwargs={'id': SPLCAT.salary_category_id}))
                else:
                    error = 'Hiring/Minimum is greater than Maximum. Please check your entry.'
                    return render_to_response('steppositionlevel_cat/form.html',{'form':form,'Edit':SPLCAT,'id2':SPLCAT.salary_category_id,'id':id,'page':val,'error':error,'display_error':1,'id2':pid},context_instance=RequestContext(request))
            else:
                form = StepPositionLevelCatForm(instance=SPLCAT)
                return render_to_response('steppositionlevel_cat/form.html',{'form':form,'Edit':SPLCAT,'id':id,'page':val,'display_error':1,'id2':pid},context_instance=RequestContext(request))
        else:
            form = StepPositionLevelCatForm(instance=SPLCAT)
        return render_to_response('steppositionlevel_cat/form.html',{'form':form,'Edit':SPLCAT,'id':id,'page':val,'id2':pid},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        SPLCAT = PesKgmSteppositionlevelCategory.objects.get(pk=id)
        form = StepPositionLevelCatForm(instance=SPLCAT)
        return render_to_response('steppositionlevel_cat/form.html',{'form':form,'Edit':SPLCAT,'id2':SPLCAT.salary_category_id,'id':id,'page':val,'error':error,'display_error':1,'id2':pid},context_instance=RequestContext(request))

@access.has_access('kg-cm-ss-ls',2)
@transaction.commit_on_success
def pes_splcat_delete(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Salary Structure Details"
    val['feature'] = 'steppositionlevel_cat'
    val['tabgroup'] = 'listspl'
    val['urlargs'] = {'urlarg1':{'id':id}}
    try:
        spl = PesKgmSteppositionlevelCategory.objects.get(pk=id)
        detailed_log(spl,request,3)
        try:
            PesKgmSteppositionlevelCategory.objects.get(pk=id).delete()
        except:
            a = PesKgmSteppositionlevelCategory.objects.get(pk=id)
            #desc = a.description + "- (DELETED)"
            #a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        transaction.commit()
        return HttpResponseRedirect(reverse('splcat_list',kwargs={'id': spl.salary_category_id}))
    except Exception as error:
        transaction.rollback()
        salary_cat = PesKgmSalarycategory.objects.get(pk=id)
        SPLCAT = PesKgmSteppositionlevelCategory.objects.filter(salary_category=id)
        return render_to_response('steppositionlevel_cat/list.html',{'list': SPLCAT,'x':salary_cat,'error':error,'page':val,'display_error':1},context_instance=RequestContext(request))
        #return render_to_response('address/list.html',{'error':1},context_instance=RequestContext(request))