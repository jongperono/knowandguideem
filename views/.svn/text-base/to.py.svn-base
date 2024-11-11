from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.db import transaction
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#models
from apps.intent.pes.knowandguideem.models.peskgmto import PesKgmTo
from apps.intent.pes.knowandguideem.models.peskgmrpb import PesKgmRpb
from apps.intent.upload.models.upload import Fileupload
#forms
from apps.intent.pes.knowandguideem.forms.toform import TOForm,TOForm1,PesKgmPositionClassificationFormset
from apps.intent.upload.forms.uploadform import FileuploadForm
#helpers
from apps.intent.upload.helpers.upload import downloadfile
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.knowandguideem.models.peskgmpositionclassification import PesKgmPositionClassification
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-po-ti-ls',1)
def pes_to_list(request):
    v = 0
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'listgroup'
    val['urlargs'] = {}
    val['gridgroup'] = 'gridgroup_list'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmTo.objects.filter(deleted=0), val['feature'], val['gridgroup'])
    return render_to_response('to/tolist.html',{'y':v,'page':val},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',2)
@transaction.commit_on_success
def pes_to_create(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'createto'
    val['urlargs'] = {}
    forms = {}
    try:
        if request.method == 'POST':
            #form = TOForm(request.POST)
            #print request.POST
            forms['to'] = TOForm(request.POST, prefix='to')
            to_hdr = forms['to'].save(commit=False)
            forms['to_class'] = PesKgmPositionClassificationFormset(request.POST, instance=to_hdr, prefix='table_org_class')
            if forms['to'].is_valid() and forms['to_class'].is_valid():
                to_hdr.deleted = 0
                to_hdr.save()
                to_class = forms['to_class'].save(commit=False)
                for toclass in to_class:
                    #toclass.code = to_hdr.code + ' - ' + toclass.code
                    toclass.save()
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(pes_to_list)
                else:
                    forms['to'] = TOForm(prefix='to')
                    forms['to_class'] = PesKgmPositionClassificationFormset(prefix='table_org_class')
                    return render_to_response('to/toform.html',{'forms':forms,'page':val,'message':1},context_instance=RequestContext(request))
            else:
                return render_to_response('to/toform.html',{'forms':forms,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            forms['to'] = TOForm(prefix='to')
            forms['to_class'] = PesKgmPositionClassificationFormset(prefix='table_org_class')
        return render_to_response('to/toform.html',{'forms':forms,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        forms['to'] = TOForm(prefix='to')
        forms['to_class'] = PesKgmPositionClassificationFormset(prefix='table_org_class')
        return render_to_response('to/toform.html',{'forms':forms,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',2)
@transaction.commit_on_success
def pes_to_modify(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'createto'
    val['urlargs'] = {}
    forms = {}
    TO = PesKgmTo.objects.get(pk=id)
    try:
        if request.method == 'POST':
            forms['to'] = TOForm(request.POST,instance=TO,prefix='to')
            forms['to_class'] = PesKgmPositionClassificationFormset(request.POST,instance=TO,prefix='table_org_class')
            #form=TOForm(request.POST,instance=TO)
            if forms['to'].is_valid() and forms['to_class'].is_valid():
                forms['to'].save()
                to_class = forms['to_class'].save(commit=False)
                for toclass in to_class:
                    #toclass.code = forms['to'].code + ' - ' + toclass.code
                    toclass.save()
                return redirect(pes_to_list)
            else:
                return render_to_response('to/toform.html',{'forms':forms,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            forms['to'] = TOForm(instance=TO,prefix='to')
            forms['to_class'] = PesKgmPositionClassificationFormset(instance=TO,prefix='table_org_class')
        return render_to_response('to/toform.html',{'forms':forms,'Edit':TO,'id':id,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        TO = PesKgmTo.objects.get(pk=id)
        forms['to'] = TOForm(instance=TO,prefix='to')
        forms['to_class'] = PesKgmPositionClassificationFormset(instance=TO,prefix='table_org_class')
        return render_to_response('to/toform.html',{'forms':forms,'Edit':TO,'id':id,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-rp-ls',1)
def pes_rpb_to(request,id):
    rpb = PesKgmRpb.objects.get(pk=id)
    return HttpResponseRedirect(reverse('to_treeview')+str("#ul-"+str(rpb.to_id)))

@access.has_access('kg-po-ti-ls',2)
@transaction.commit_on_success
def pes_to_delete(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'listgroup'
    val['urlargs'] = {}
    try:
        try:
            PesKgmTo.objects.get(pk=id).delete()
        except:
            a = PesKgmTo.objects.get(pk=id)
            desc = a.description + "- (DELETED)"
            code = a.code + "- (DELETED)"
            a.description = desc
            a.code = code
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        transaction.commit()
        return redirect(pes_to_list)
    except Exception as error:
        transaction.rollback()
        TO = PesKgmTo.objects.all()
        return render_to_response('to/tolist.html',{'list': TO,'error':error,'display_error':1,'page':val},context_instance=RequestContext(request))
        #return render_to_response('address/list.html',{'error':1},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-tv',1)
def pes_to_treeview(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'listgroup'
    val['urlargs'] = {}
    #TO = PesKgmTo.objects.all()
    return render_to_response('to/totreeview.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',2)
@transaction.commit_on_success
def pes_to_treeview_create(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'createto1'
    val['urlargs'] = {}
    forms = {}
    TO = PesKgmTo.objects.get(pk=id)
    try:
        if request.method == 'POST':
            forms['to'] = TOForm(request.POST,prefix='to')
            forms['to_class'] = PesKgmPositionClassificationFormset(request.POST,prefix='table_org_class')
            #form = TOForm(request.POST)
            if forms['to'].is_valid() and forms['to_class'].is_valid():
                to_hdr = forms['to'].save(commit=False)
                to_hdr.deleted = 0
                to_hdr.parent_id = TO.id
                to_hdr.save()
                to_class = forms['to_class'].save(commit=False)
                for toclass in to_class:
                    toclass.to_id = to_hdr.id
                    toclass.save()
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(pes_to_treeview)
                else:
                    forms['to'] = TOForm(prefix='to')
                    forms['to_class'] = PesKgmPositionClassificationFormset(prefix='table_org_class')
                    return render_to_response('to/totreeviewform.html',{'forms':forms,'page':val,'list':TO,'message':1},context_instance=RequestContext(request))
            else:
                return render_to_response('to/totreeviewform.html',{'forms':forms,'page':val,'list':TO,'display_error':1},context_instance=RequestContext(request))
        else:
            forms['to'] = TOForm(prefix='to')
            forms['to_class'] = PesKgmPositionClassificationFormset(prefix='table_org_class')
            #form = TOForm()
        return render_to_response('to/totreeviewform.html',{'forms':forms,'page':val,'list':TO},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        forms['to'] = TOForm(prefix='to')
        forms['to_class'] = PesKgmPositionClassificationFormset(prefix='table_org_class')
        #form = TOForm()
        return render_to_response('to/totreeviewform.html',{'forms':forms,'page':val,'list':TO,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',2)
@transaction.commit_on_success
def pes_to_treeview_edit(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'createto1'
    val['urlargs'] = {}
    forms = {}
    TO = PesKgmTo.objects.get(pk=id)
    #position = PesKgmPositionClassification.objects.filter(to_id=id)
    try:
        if request.method == 'POST':
            #form = TOForm1(request.POST,instance=TO)
            forms['to'] = TOForm1(request.POST,instance=TO,prefix='to')
            forms['to_class'] = PesKgmPositionClassificationFormset(request.POST,instance=TO,prefix='to_class')
            if forms['to'].is_valid() and forms['to_class'].is_valid():
                to_hdr = forms['to'].save(commit=False)
                to_hdr.parent_id = TO.parent_id
                to_hdr.deleted = 0
                to_hdr.save()
                to_class = forms['to_class'].save(commit=False)
                for toclass in to_class:
                    toclass.to_id = to_hdr.id
                    toclass.save()
                transaction.commit()
                return redirect(pes_to_treeview)
            else:
                return render_to_response('to/totreeviewform.html',{'forms':forms,'Edit':TO,'id':id,'page':val,'list':TO,'display_error':1},context_instance=RequestContext(request))
        else:
            forms['to'] = TOForm1(instance=TO,prefix='to')
            forms['to_class'] = PesKgmPositionClassificationFormset(instance=TO,prefix='to_class')
        return render_to_response('to/totreeviewform.html',{'forms':forms,'Edit':TO,'id':id,'page':val,'list':TO},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        forms['to'] = TOForm1(instance=TO,prefix='to')
        forms['to_class'] = PesKgmPositionClassificationFormset(instance=TO,prefix='to_class')
        return render_to_response('to/totreeviewform.html',{'forms':forms,'Edit':TO,'id':id,'page':val,'list':TO,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',2)
@transaction.commit_on_success
def pes_to_treeview_del(request,id):
    try:
        PesKgmTo.objects.filter(pk=id).delete()
        transaction.commit()
        return redirect(pes_to_treeview)
    except Exception as error:
        transaction.rollback()
        TO = PesKgmTo.objects.all()
        return render_to_response('to/totreeview.html',{'list':TO,'error':error},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',1)
def pes_to_info(request,id):
    fileupload = Fileupload.objects.filter(reference_key=id,uploadname="TO Upload",status='1')
    to = PesKgmTo.objects.get(pk=id)
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'toinfo'
    val['urlargs'] = {'urlarg1':{'id':id}}
    return render_to_response('to/toinfo.html',{'list': fileupload,'id':id,'to':to,'page':val},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',2)
@transaction.commit_on_success
def pes_to_info_upload(request,id):
    to = PesKgmTo.objects.get(pk=id)
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'toupload'
    val['urlargs'] = {'urlarg1':{'id':to.id}}
    try:
        if request.POST:
            form = FileuploadForm(request.POST, request.FILES)        
            if form.is_valid():
                obj = form.save(commit=False)
                to = PesKgmTo.objects.get(pk=id)
                obj.useraccount_id = 33
                obj.file_type = request.FILES['file'].content_type
                obj.file_size = request.FILES['file'].size
                obj.subsystem="PES"
                obj.module="KnowAndGuideEm"
                obj.submodule="Table of Organization"
                obj.uploadname="TO Upload"
                obj.reference_key = id
                obj.status = 1
                obj.save()
                transaction.commit()
                return HttpResponseRedirect(reverse('to_info',kwargs={'id':id}))
            else:
                raise Http404
        else:
            form = FileuploadForm()
            return render_to_response('to/toupload.html', {'form': form,'id':id,'page':val}, context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form = FileuploadForm()
        return render_to_response('to/toupload.html', {'form': form,'id':id,'page':val,'error':error}, context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',1)
def pes_to_file_download(request,id):
    return downloadfile(request,id)

@access.has_access('kg-po-ti-ac',1)
def pes_to_archive(request):
    fileupload = Fileupload.objects.filter(uploadname="TO Upload",status='0')
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'toarchive'
    val['urlargs'] = {}
    return render_to_response('to/toarchive.html',{'list': fileupload,'page':val},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ls',2)
@transaction.commit_on_success
def pes_to_archive_upload(request,to_id,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'toinfo'
    val['urlargs'] = {'urlarg1':{'id':to_id}}
    to = PesKgmTo.objects.get(pk=to_id)
    try:
        upload = Fileupload.objects.get(pk=id)
        upload.status = 0
        upload.save()
        transaction.commit()
        return HttpResponseRedirect(reverse('to_info',kwargs={'id': to.id}))
    except Exception as error:
        transaction.rollback()
        fileupload = Fileupload.objects.filter(reference_key=to_id,uploadname="TO Upload")
        to = PesKgmTo.objects.get(pk=to_id)
        return render_to_response('rpb/rpbinfo.html',{'list': fileupload,'id':id,'to':to,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-po-ti-ac',2)
@transaction.commit_on_success
def pes_to_restore_upload(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Table of Organization'
    val['feature'] = 'to'
    val['tabgroup'] = 'toarchive'
    val['urlargs'] = {}
    try:
        upload = Fileupload.objects.get(pk=id)
        upload.status = 1
        upload.save()
        transaction.commit()
        return redirect(pes_to_archive)
    except Exception as error:
        transaction.rollback()
        fileupload = Fileupload.objects.filter(uploadname="TO Upload",status='0')
        return render_to_response('to/toarchive.html',{'list': fileupload,'id':id,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))
    