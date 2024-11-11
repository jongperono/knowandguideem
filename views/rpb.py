from django.shortcuts import render_to_response,redirect,HttpResponse
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
import xlwt
#models
from apps.intent.pes.knowandguideem.models.peskgmrpb import PesKgmRpb
from apps.intent.upload.models.upload import Fileupload
from apps.intent.pes.pis.models.pespiscds import PesPisCds
from apps.intent.pes.knowandguideem.models.peskgmto import PesKgmTo
from apps.intent.pes.knowandguideem.models.peskgmhierarchy import PesKgmHierarchy
#forms
from apps.intent.pes.knowandguideem.forms.rpbform import RPBForm,RPBReportForm
from apps.intent.upload.forms.uploadform import FileuploadForm
#helpers
from apps.intent.upload.helpers.upload import downloadfile
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
from django.db.models import Q
from apps.intent.pes.base.helpers.pesfilters import get_filter_operator2
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.pes.pis.views.pespisemployeeinfo import rpb_info2
from apps.intent.pes.base.helpers.universal import display_view_err


@access.has_access('kg-rb-ls',1)
def pes_rpb_list(request):
    p = Q()
    l = Q()
    to_param = request.GET.get('i_n')
    cs_param = request.GET.get('i_i')
    if to_param:
        p = get_filter_operator2(request,'n',['description',], 'to', to_param)
    if cs_param:
        l = get_filter_operator2(request,'n',['description',], 'hierarchy', cs_param)
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'listrpb'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmRpb.objects.filter(deleted=0,temp=0).filter(p).filter(l), val['feature'], val['gridgroup'])
    return render_to_response('rpb/rpblist.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-rb-ls',1)
def pes_rpb_list_dummy(request):
    p = Q()
    l = Q()
    to_param = request.GET.get('i_n')
    cs_param = request.GET.get('i_i')
    if to_param:
        p = get_filter_operator2(request,'n',['description',], 'to', to_param)
    if cs_param:
        l = get_filter_operator2(request,'n',['description',], 'hierarchy', cs_param)
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'listrpb'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmRpb.objects.filter(deleted=0,temp=1).filter(p).filter(l), val['feature'], val['gridgroup'])
    return render_to_response('rpb/rpblist.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-rb-ls',2)
@transaction.commit_on_success
def pes_rpb_create(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'createrpb'
    val['urlargs'] = {}
    try:
        if request.method == 'POST':
            form = RPBForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['datefrom'] > form.cleaned_data['dateto']:
                    raise Exception("Your effectivity date from is later than effectivity date to.")
                rpb = form.save(commit=False)
                rpb.deleted = 0
                rpb.save()
                detailed_log(rpb,request,1)
                transaction.commit()
                if request.POST['save']=="save":
                    if rpb.temp == 1:
                        return redirect(pes_rpb_list_dummy)
                    return redirect(pes_rpb_list)
                else:
                    form = RPBForm()
                    return render_to_response('rpb/rpbform.html',{'form':form,'page':val,'message':1},context_instance=RequestContext(request))
            else:
                return render_to_response('rpb/rpbform.html',{'form':form,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            form = RPBForm()
        return render_to_response('rpb/rpbform.html',{'form':form,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form = RPBForm()
        return render_to_response('rpb/rpbform.html',{'form':form,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-rb-ls',2)
@transaction.commit_on_success
def pes_rpb_modify(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'createrpb'
    val['urlargs'] = {}
    RPB = PesKgmRpb.objects.get(pk=id)
    vals = []
    cds = PesPisCds.objects.filter(rpb_id=id)
    if cds:
        vals = []
    try:
        if request.method == 'POST':
            form=RPBForm(request.POST,instance=RPB)
            if form.is_valid():
                if form.cleaned_data['datefrom'] > form.cleaned_data['dateto']:
                    raise Exception("Your effectivity date from is later than effectivity date to.")
                form.save()
                detailed_log(RPB,request,2)
                transaction.commit()
                RPB = PesKgmRpb.objects.get(pk=id)
                if RPB.temp == 1:
                    return redirect(pes_rpb_list_dummy)
                return redirect(pes_rpb_list)
            else:
                return render_to_response('rpb/rpbform.html',{'form':form,'page':val,'display_error':1,'val':vals},context_instance=RequestContext(request))
        else:
            form = RPBForm(instance=RPB)
        return render_to_response('rpb/rpbform.html',{'form':form,'Edit':RPB,'id':id,'page':val,'val':vals},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        RPB = PesKgmRpb.objects.get(pk=id)
        form = RPBForm(instance=RPB)
        return render_to_response('rpb/rpbform.html',{'form':form,'Edit':RPB,'id':id,'page':val,'error':error,'display_error':1,'val':vals},context_instance=RequestContext(request))

@access.has_access('kg-rb-ls',2)
@transaction.commit_on_success
def pes_rpb_delete(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'listrpb'
    try:
        try:
            rbb=PesKgmRpb.objects.get(pk=id)
            detailed_log(rbb,request,3)
            rbb.delete()
        except:
            a = PesKgmRpb.objects.get(pk=id)
            if a.present_count > 0:
                raise Exception('You cannot delete this entry. Please check the Balance count.')
            desc = a.description + "- (DELETED)"
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        transaction.commit()
        return redirect(pes_rpb_list)
    except Exception as error:
        error = display_view_err(error)
        p = Q()
        l = Q()
        to_param = request.GET.get('i_n')
        cs_param = request.GET.get('i_i')
        if to_param:
            p = get_filter_operator2(request,'n',['description',], 'to', to_param)
        if cs_param:
            l = get_filter_operator2(request,'n',['description',], 'hierarchy', cs_param)
        transaction.rollback()
        val['gridgroup'] = 'grid'
        val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmRpb.objects.filter(deleted=0,temp=0).filter(p).filter(l), val['feature'], val['gridgroup'])
        return render_to_response('rpb/rpblist.html',{'page':val,'display_error':True,'error':error},context_instance=RequestContext(request))

@access.has_access('kg-rb-ls',1)
def pes_rpb_info(request,id):
    fileupload = Fileupload.objects.filter(reference_key=id,uploadname="RPB Upload",status='1')
    rpb = PesKgmRpb.objects.get(pk=id)
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'rpbinfo'
    val['urlargs'] = {'urlarg1':{'id':id}}
    return render_to_response('rpb/rpbinfo.html',{'list': fileupload,'id':id,'rpb':rpb,'page':val},context_instance=RequestContext(request))

@access.has_access('kg-rp-ls',1)
def pes_rpb_hierarchy(request,id):
    rpb = PesKgmRpb.objects.get(pk=id)
    return HttpResponseRedirect(reverse('peskgmhierarchytreeviewlist')+str("#txtid-"+str(rpb.hierarchy_id)))

@access.has_access('kg-rb-ls',2)
@transaction.commit_on_success
def pes_rpb_info_upload(request,id):
    rpb = PesKgmRpb.objects.get(pk=id)
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'rpbupload'
    val['urlargs'] = {'urlarg1':{'id':rpb.id}}
    try:
        if request.POST:
            form = FileuploadForm(request.POST, request.FILES)        
            if form.is_valid():
                obj = form.save(commit=False)
                rpb = PesKgmRpb.objects.get(pk=id)
                obj.useraccount_id = 33
                obj.file_type = request.FILES['file'].content_type
                obj.file_size = request.FILES['file'].size
                obj.subsystem="PES"
                obj.module="KnowAndGuideEm"
                obj.submodule="Required Present Balance"
                obj.uploadname="RPB Upload"
                obj.reference_key = id
                obj.status = 1
                obj.save()
                transaction.commit()
                return HttpResponseRedirect(reverse('rpb_info',kwargs={'id': rpb.id}))
            else:
                raise Http404
        else:
            form = FileuploadForm()
            return render_to_response('rpb/rpbupload.html', {'form': form,'id':rpb.id,'page':val}, context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form = FileuploadForm()
        return render_to_response('rpb/rpbupload.html', {'form': form,'id':rpb.id,'page':val,'error':error}, context_instance=RequestContext(request))

@access.has_access('kg-rb-ls',1)
def pes_rpb_file_download(request,id):
    return downloadfile(request,id)

@access.has_access('kg-rb-ac',1)
def pes_rpb_archive(request):
    fileupload = Fileupload.objects.filter(uploadname="RPB Upload",status='0')
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'rpbarchive'
    val['urlargs'] = {}
    return render_to_response('rpb/rpbarchive.html',{'list': fileupload,'page':val},context_instance=RequestContext(request))

@access.has_access('kg-rb-ls',2)
@transaction.commit_on_success
def pes_rpb_archive_upload(request,rpb_id,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'rpbinfo'
    val['urlargs'] = {'urlarg1':{'id':rpb_id}}
    rpb = PesKgmRpb.objects.get(pk=rpb_id)
    try:
        upload = Fileupload.objects.get(pk=id)
        upload.status = 0
        upload.save()
        transaction.commit()
        return HttpResponseRedirect(reverse('rpb_info',kwargs={'id': rpb.id}))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        fileupload = Fileupload.objects.filter(reference_key=rpb_id,uploadname="RPB Upload")
        rpb = PesKgmRpb.objects.get(pk=rpb_id)
        return render_to_response('rpb/rpbinfo.html',{'list': fileupload,'id':id,'rpb':rpb,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-rb-ac',2)
@transaction.commit_on_success
def pes_rpb_restore_upload(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'rpbarchive'
    val['urlargs'] = {}
    try:
        upload = Fileupload.objects.get(pk=id)
        upload.status = 1
        upload.save()
        transaction.commit()
        return redirect(pes_rpb_archive)
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        fileupload = Fileupload.objects.filter(uploadname="RPB Upload",status='0')
        return render_to_response('rpb/rpbarchive.html',{'list': fileupload,'id':id,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

def to_info(request,uid):
    info = []
    rpb = PesKgmRpb.objects.get(pk=uid)
    to = PesKgmTo.objects.get(pk=rpb.to_id)
    parent = to.parent_id
    info.append(to.description)
    while True:
        if parent:
            val = get_parent(parent)
            if val[1]:
                info.append(val[1])
            else:
                info.append(get_description(parent,True))
            if val[0]:
                parent = val[2]
            else:
                parent = None
        else:
            break
    print info,info.reverse()
    return render_to_response('rpb/toinfo.html',{'info':info,'id':uid},context_instance=RequestContext(request))

def to_info2(request,uid):
    info = []
    to = PesKgmTo.objects.get(pk=uid)
    parent = to.parent_id
    info.append(to.description)
    while True:
        if parent:
            val = get_parent(parent)
            if val[1]:
                info.append(val[1])
            else:
                info.append(get_description(parent,True))
            if val[0]:
                parent = val[2]
            else:
                parent = None
        else:
            break
    print info,info.reverse()
    return render_to_response('rpb/toinfo.html',{'info':info,'id':uid},context_instance=RequestContext(request))

def rpb_report(request):
    lists = PesKgmRpb.objects.all()
    book = xlwt.Workbook(encoding='utf8',style_compression=2)
    sheet = book.add_sheet('Sheet 1')
    row = 0
    sheet.write(0,0,'CODE')
    sheet.write(0,1,'DESCRIPTION')
    sheet.write(0,2,'T.O')
    sheet.write(0,3,'REQUIRED')
    sheet.write(0,4,'PRESENT')
    sheet.write(0,5,'BALANCE')
    sheet.write(0,6,'EMPLOYMENT STATUS')
    sheet.write(0,7,'AUTO-REPLENISH')
    sheet.write(0,8,'COMPANY STRUCTURE')
    sheet.write(0,9,'BRANCH')
    sheet.write(0,10,'DATE FROM')
    sheet.write(0,11,'DATE TO')
    for i in lists:
        print i.id
        row += 1
        sheet.write(row,0,i.code)
        sheet.write(row,1,i.description)
        sheet.write(row,2,i.to.description)
        sheet.write(row,3,i.required_count)
        sheet.write(row,4,i.present_count)
        sheet.write(row,5,i.balance_count)
        sheet.write(row,6,i.empoyment_status.description)
        sheet.write(row,7,i.auto)
        sheet.write(row,8,i.hierarchy.description)
        sheet.write(row,9,i.pes_location.branch_code)
        sheet.write(row,10,date_to_str(i.datefrom))
        sheet.write(row,11,date_to_str(i.dateto))
    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % "PES_RPB_LIST.xls"
    book.save(response)
    return response

@access.has_access('kg-rp-rs',2)
def rpb_report2(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Required Present Balance Report'
    val['feature'] = 'rpb'
    val['tabgroup'] = 'report'
    val['urlargs'] = {}
    company = {}
    autoreplenish = {}
    area = {}
    branch = {}
    division = {}
    department = {}
    employstatus = {}
    try:
        if request.method == 'POST':
            form = RPBReportForm(request.POST)
            if form.is_valid():
                try:
                    company = {'hierarchy__company_id':int(form.cleaned_data['company'])}
                except:
                    pass
                if form.cleaned_data['area']:
                    area = {'pes_location__region_id':int(form.cleaned_data['area'])}
                if form.cleaned_data['autoreplenish']:
                    autoreplenish = {'autoreplenish':form.cleaned_data['autoreplenish']}
                try:
                    branch = {'pes_location_id':int(form.cleaned_data['branch'])}
                except:
                    pass
                try:
                    division = int(form.cleaned_data['division'])
                except:
                    pass
                try:
                    department = int(form.cleaned_data['department'])
                except:
                    pass
                try:
                    employstatus = {'empoyment_status':int(form.cleaned_data['employment_status'])}
                except:
                    pass
            lists = PesKgmRpb.objects.filter(deleted=0).filter(**company).filter(**autoreplenish).filter(**area).filter(**branch).filter(**employstatus)
            book = xlwt.Workbook(encoding='utf8',style_compression=2)
            sheet = book.add_sheet('Sheet 1')
            row = 0
            sheet.write(0,0,'CODE',xlwt.easyxf('font: bold on;'))
            sheet.write(0,1,'DESCRIPTION',xlwt.easyxf('font: bold on;'))
            sheet.write(0,2,'T.O',xlwt.easyxf('font: bold on;'))
            sheet.write(0,3,'REQUIRED',xlwt.easyxf('font: bold on;'))
            sheet.write(0,4,'PRESENT',xlwt.easyxf('font: bold on;'))
            sheet.write(0,5,'BALANCE',xlwt.easyxf('font: bold on;'))
            sheet.write(0,6,'EMPLOYMENT STATUS',xlwt.easyxf('font: bold on;'))
            sheet.write(0,7,'AUTO-REPLENISH',xlwt.easyxf('font: bold on;'))
            sheet.write(0,8,'COMPANY STRUCTURE',xlwt.easyxf('font: bold on;'))
            sheet.write(0,9,'BRANCH',xlwt.easyxf('font: bold on;'))
            sheet.write(0,10,'DATE FROM',xlwt.easyxf('font: bold on;'))
            sheet.write(0,11,'DATE TO',xlwt.easyxf('font: bold on;'))
            sheet.col(0).width = 40 * 256
            sheet.col(1).width = 45 * 256
            sheet.col(2).width = 45 * 256
            sheet.col(8).width = 45 * 256
            for i in lists:
                rpbinfo = rpb_info2(i.id)
                if division:
                    if rpbinfo['division'] != division:
                        continue
                if department:
                    if rpbinfo['department'] != department:
                        continue
                row += 1
                sheet.write(row,0,i.code)
                sheet.write(row,1,i.description)
                sheet.write(row,2,i.to.description)
                sheet.write(row,3,i.required_count)
                sheet.write(row,4,i.present_count)
                sheet.write(row,5,i.balance_count)
                sheet.write(row,6,i.empoyment_status.description)
                sheet.write(row,7,i.auto)
                sheet.write(row,8,i.hierarchy.description)
                sheet.write(row,9,i.pes_location.branch_code)
                sheet.write(row,10,date_to_str(i.datefrom))
                sheet.write(row,11,date_to_str(i.dateto))
            response = HttpResponse(mimetype='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' % "PES_RPB_LIST.xls"
            book.save(response)
            return response
        else:
            form = RPBReportForm()
        return render_to_response('rpb/rpbreport.html',{'page':val,'form':form},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = RPBReportForm()
        return render_to_response('rpb/rpbreport.html',{'page':val,'form':form,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-rb-ls',1)
def rpb_tagged_associates(request, id):
    book = xlwt.Workbook(encoding='utf8',style_compression=2)
    sheet = book.add_sheet('Sheet 1')
    cds = PesPisCds.objects.filter(rpb_id=id).filter(Q(contract_end_date__isnull=True)|Q(contract_end_date__gte=datetime.date.today()))
    #print cds,cds.count()
    row = 0
    sheet.col(0).width = 12 * 256
    sheet.col(1).width = 25 * 256
    sheet.col(2).width = 25 * 256
    sheet.col(3).width = 25 * 256
    sheet.write(row,0,'Company ID')
    sheet.write(row,1,'Last Name')
    sheet.write(row,2,'First Name')
    sheet.write(row,3,'Middle Name')
    row += 1
    for cd in cds:
        sheet.write(row,0,cd.person.company_id)
        sheet.write(row,1,cd.person.last_name)
        sheet.write(row,2,cd.person.first_name)
        sheet.write(row,3,cd.person.middle_name)
        row += 1
    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=RPBReport.xls'
    book.save(response)
    return response

def hierarchy_info(request,uid):
    info = []
    rpb = PesKgmRpb.objects.get(pk=uid)
    to = PesKgmHierarchy.objects.get(pk=rpb.hierarchy_id)
    parent = to.parent_id
    info.append(to.description)
    while True:
        if parent:
            val = get_parent(parent,True)
            if val[1]:
                info.append(val[1])
            else:
                info.append(get_description(parent))
            if val[0]:
                parent = val[2]
            else:
                parent = None
        else:
            break
        print info
    print info,info.reverse()
    return render_to_response('rpb/toinfo.html',{'info':info,'id':uid},context_instance=RequestContext(request))

def get_parent(uid,hierarchy=None):
    if hierarchy:
        to = PesKgmHierarchy.objects.get(pk=uid)
        if to.parent:
            return True,to.description,to.parent_id
    else:
        to = PesKgmTo.objects.get(pk=uid)
        if to.parent:
            return True,to.description,to.parent_id
    return False,None,to.id

def get_description(uid,to=None):
    if to:
        return PesKgmTo.objects.get(pk=uid).description
    return PesKgmHierarchy.objects.get(pk=uid).description

def date_to_str(date):
    try:
        yr = date.year
        mo = date.month
        dy = date.day
        return str(yr) + '-' + str(mo) + '-' + str(dy)
    except:
        return ''