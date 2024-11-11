from django.shortcuts import render_to_response, HttpResponse, redirect,HttpResponseRedirect
from django.template import RequestContext
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from django.db import transaction
from django.core.urlresolvers import reverse
from apps.intent.pes.security.decorator import access
import datetime
#models
from apps.intent.pes.comben.models.pescbmcompensationaccounts import PesCbmCompensationAccounts,PesCbmCompensationAccountsDtls,PesCbmAccountDtls,PesCbmPADtl
#forms
from apps.intent.pes.comben.forms.pescbmcompenaccountsform import PesCbmCompensationAccountsDtlsFormset
from apps.intent.pes.knowandguideem.forms.peskgmcompentmpldtl import PesCbmAccountDtlsForm
from apps.intent.pes.knowandguideem.forms.peskgmcompenpatmpldtl import PesCbmPADtlForm

@access.has_access('kg-cm-al-ls',1)
def index(request):
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'list'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesCbmCompensationAccountsDtls.objects.filter(compensation_id=1).order_by('id'), val['feature'], val['gridgroup'])
    return render_to_response('compentemplates/list.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',2)
@transaction.commit_on_success
def add(request):
    hdr = PesCbmCompensationAccounts.objects.get(pk=1)
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'create'
    val['urlargs'] = {}
    forms = {}
    try:
        if request.method == 'POST':
            forms['mortuary_dts'] = PesCbmCompensationAccountsDtlsFormset(request.POST, instance=hdr, prefix='mortuarydts')
            if forms['mortuary_dts'].is_valid():
                forms['mortuary_dts'].save()
                return redirect(index)
            else:
                return render_to_response('compentemplates/form.html',{'forms':forms,'page':val, 'display_error':1},context_instance=RequestContext(request))
        else:
            forms['mortuary_dts'] = PesCbmCompensationAccountsDtlsFormset(instance=hdr, prefix='mortuarydts')
        return render_to_response('compentemplates/form.html',{'forms':forms,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        forms['mortuary_dts'] = PesCbmCompensationAccountsDtlsFormset(instance=hdr, prefix='mortuarydts')
        return render_to_response('compentemplates/form.html',{'forms':forms,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',1)
def allow_index(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'detail'
    val['urlargs'] = {'urlarg1':{'id':id}}
    try:
        hdr = PesCbmCompensationAccountsDtls.objects.get(pk=id)
    except Exception as error:
        return render_to_response('compentemplates/list.html',{'page':val,'display_error':1,'error':error},context_instance=RequestContext(request))
    val['gridgroup'] = 'grid2'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesCbmAccountDtls.objects.filter(compenacct_id=id,deleted=0).order_by('id'), val['feature'], val['gridgroup'])
    return render_to_response('compentemplates/list.html',{'page':val,'hdr':hdr},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',2)
@transaction.commit_on_success
def allow_create(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'detailcreate'
    val['urlargs'] = {'urlarg1':{'id':id}}
    try:
        message = request.GET['message']
    except:
        message = None
    link = reverse('compen_dtl_create',kwargs={'id': id})
    try:
        if request.method == 'POST':
            form = PesCbmAccountDtlsForm(request.POST)
            if form.is_valid():
                dtl = form.save(commit=False)
                dtl.compenacct_id = id
                dtl.save()
                transaction.commit()
                if request.POST['save']=="save":
                    return HttpResponseRedirect(reverse('compen_dtl',kwargs={'id': id}))
                else:
                    return HttpResponseRedirect(str(link)+"?message=True")
                    #form = PesCbmAccountDtlsForm()
                    #return render_to_response('compentemplates/dtlform.html',{'form':form,'page':val,'message':1},context_instance=RequestContext(request))
            else:
                return render_to_response('compentemplates/dtlform.html',{'form':form,'page':val,'display_error':1,'id':id,'message':message},context_instance=RequestContext(request))
        else:
            form = PesCbmAccountDtlsForm()
        return render_to_response('compentemplates/dtlform.html',{'form':form,'page':val,'id':id,'message':message},context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form = PesCbmAccountDtlsForm()
        return render_to_response('compentemplates/dtlform.html',{'form':form,'page':val,'error':error,'display_error':1,'id':id,'message':message},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',2)
@transaction.commit_on_success
def allow_edit(request,id):
    hdr = PesCbmAccountDtls.objects.get(pk=id)
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'detailcreate'
    val['urlargs'] = {'urlarg1':{'id':hdr.compenacct.id}}
    try:
        if request.method == 'POST':
            form = PesCbmAccountDtlsForm(request.POST,instance=hdr)
            if form.is_valid():
                dtl = form.save(commit=False)
                dtl.save()
                transaction.commit()
                return HttpResponseRedirect(reverse('compen_dtl',kwargs={'id': hdr.compenacct_id}))
            else:
                return render_to_response('compentemplates/dtlform.html',{'Edit':hdr,'form':form,'page':val,'display_error':1,'id':id},context_instance=RequestContext(request))
        else:
            form = PesCbmAccountDtlsForm(instance=hdr)
        return render_to_response('compentemplates/dtlform.html',{'Edit':hdr,'form':form,'page':val,'id':id},context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form = PesCbmAccountDtlsForm(instance=hdr)
        return render_to_response('compentemplates/dtlform.html',{'Edit':hdr,'form':form,'page':val,'error':error,'display_error':1,'id':id},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',2)
@transaction.commit_on_success
def allow_delete(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'create'
    val['urlargs'] = {}
    try:
        hdr = PesCbmAccountDtls.objects.get(pk=id)
        hdr.deleted = 1
        hdr.date_del = datetime.date.today()
        hdr.save()
        transaction.commit()
        return HttpResponseRedirect(reverse('compen_dtl',kwargs={'id':hdr.compenacct_id}))
    except Exception as error:
        transaction.rollback()
        return render_to_response('compentemplates/list.html',{'error':error,'page':val,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',1)
def allow_pa_index(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'padetail'
    val['urlargs'] = {'urlarg1':{'id':id}}
    try:
        hdr = PesCbmCompensationAccountsDtls.objects.get(pk=id)
    except Exception as error:
        return render_to_response('compentemplates/list.html',{'page':val,'display_error':1,'error':error},context_instance=RequestContext(request))
    val['gridgroup'] = 'grid3'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesCbmPADtl.objects.filter(compenacct_id=id,deleted=0).order_by('id'), val['feature'], val['gridgroup'])
    return render_to_response('compentemplates/list.html',{'page':val,'hdr':hdr},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',2)
@transaction.commit_on_success
def allow_pa_create(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'padetailcreate'
    val['urlargs'] = {'urlarg1':{'id':id}}
    try:
        message = request.GET['message']
    except:
        message = None
    link = reverse('compen_pa_dtl_create',kwargs={'id': id})
    try:
        if request.method == 'POST':
            form = PesCbmPADtlForm(request.POST)
            if form.is_valid():
                dtl = form.save(commit=False)
                dtl.compenacct_id = id
                dtl.save()
                transaction.commit()
                if request.POST['save']=="save":
                    return HttpResponseRedirect(reverse('compen_pa_dtl',kwargs={'id': id}))
                else:
                    return HttpResponseRedirect(str(link)+"?message=True")
            else:
                return render_to_response('compentemplates/padtlform.html',{'form':form,'page':val,'display_error':1,'id':id,'message':message},context_instance=RequestContext(request))
        else:
            form = PesCbmPADtlForm()
        return render_to_response('compentemplates/padtlform.html',{'form':form,'page':val,'id':id,'message':message},context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form = PesCbmPADtlForm()
        return render_to_response('compentemplates/padtlform.html',{'form':form,'page':val,'error':error,'display_error':1,'id':id,'message':message},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',2)
@transaction.commit_on_success
def allow_pa_edit(request,id):
    hdr = PesCbmPADtl.objects.get(pk=id)
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'padetailcreate'
    val['urlargs'] = {'urlarg1':{'id':hdr.compenacct.id}}
    try:
        if request.method == 'POST':
            form = PesCbmPADtlForm(request.POST,instance=hdr)
            if form.is_valid():
                dtl = form.save(commit=False)
                dtl.save()
                transaction.commit()
                return HttpResponseRedirect(reverse('compen_pa_dtl',kwargs={'id': hdr.compenacct_id}))
            else:
                return render_to_response('compentemplates/padtlform.html',{'Edit':hdr,'form':form,'page':val,'display_error':1,'id':id},context_instance=RequestContext(request))
        else:
            form = PesCbmPADtlForm(instance=hdr)
        return render_to_response('compentemplates/padtlform.html',{'Edit':hdr,'form':form,'page':val,'id':id},context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form = PesCbmPADtlForm(instance=hdr)
        return render_to_response('compentemplates/padtlform.html',{'Edit':hdr,'form':form,'page':val,'error':error,'display_error':1,'id':id},context_instance=RequestContext(request))

@access.has_access('kg-cm-al-ls',2)
@transaction.commit_on_success
def allow_pa_delete(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - Allowances"
    val['feature'] = 'compentemplates'
    val['tabgroup'] = 'create'
    val['urlargs'] = {}
    try:
        hdr = PesCbmPADtl.objects.get(pk=id)
        hdr.deleted = 1
        hdr.date_del = datetime.date.today()
        hdr.save()
        transaction.commit()
        return HttpResponseRedirect(reverse('compen_pa_dtl',kwargs={'id':hdr.compenacct_id}))
    except Exception as error:
        transaction.rollback()
        return render_to_response('compentemplates/list.html',{'error':error,'page':val,'display_error':1},context_instance=RequestContext(request))
