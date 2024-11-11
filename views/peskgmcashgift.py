from django.shortcuts import render_to_response, HttpResponse, redirect
from django.template import RequestContext
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset,get_filter_operator2
from django.db.models import Q
from apps.intent.pes.payroll.models.cashgift import PesKgmCashgiftAmount, PesKgmCashgiftX,\
    PesKgmCashgiftMatrix, PesKgmCashGiftLockDates, PesKgmCashgiftDtlsX
from apps.intent.pes.knowandguideem.forms.peskgmgc import PesPayrollCGForm,\
    PesPayrollCGUploadForm, PesPayrollCGMasteListForm, PesPayrollCGForm2,\
    PesKgmCashGiftLockDatesForm, PesKgmCashgiftXForm, PesKgmCashgiftMatrixForm,\
    PesKgmCashgiftDtlsXForm, PesKgmCgCompanyForm, PesKgmCashgiftRatingForm, PesKgmCgParamDatesForm
    
from apps.intent.pes.base.helpers.pes_session import get_person_id,\
    get_people_id_list
from apps.intent.pes.payroll.helpers.cashgift import calc_cash_gift,\
    gen_cashgift, export_cg_masterlist
from decimal import Decimal
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import datetime, date
from apps.intent.pes.security.models.logs import PesSecLogs
import json
from django.db import transaction
from apps.intent.pes.security.decorator import access
from apps.intent.pes.security.helpers.access import has_restriction,\
    get_target_org_mod_id, get_extra_par
from apps.intent.party.models.Person import Person
from apps.intent.pes.pis.models.pespiscds import PesPisCds
from apps.intent.pes.knowandguideem.models.peskgmcashgift import PesCGCompany, PesKgmCashGiftRating, PesKgmCgParamDates
from apps.intent.pes.base.helpers.universal import display_view_err

#LOCK_PERIOD = date(2015, 12, 7)
@access.has_access('kg-pms-cgt',1)
def company_dtl(request):
    val = {'title':'PES - Planning & Development - Cash Gift Table', 'feature':'kgm_cg', 'tabgroup':'cmdtltbl', 'urlargs':{}, 'gridgroup':'cmdtltbl'}
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesCGCompany.objects.all(), val['feature'], val['gridgroup'])
    #raise Exception(val)
    return render_to_response('kgm_cg/cmptdtl_list.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',3)
def company_dtl_edit(request, uid):
    company = PesCGCompany.objects.get(id=uid)
    val = {'title':'PES - Planning & Development - Cash Gift Company Table', 'feature':'kgm_cg', 'tabgroup':'cmdtltbledit', 'urlargs':{}, 'gridgroup':'cmdtltbl'}
    try:
        if request.method == 'POST':
            form = PesKgmCgCompanyForm(request.POST,instance=company)
            if form.is_valid():
                companydtl = form.save(commit=False)
                companydtl.save()
                return redirect(company_dtl)
                '''
                if form.cleaned_data['from_rate'] > form.cleaned_data['to_rate']:
                    raise Exception('Rate From is greater than Rate To. Please check your entry.')
                rating.save()
                return redirect(ratetbl)
                '''
            else:
                return render_to_response('kgm_cg/companydtlform.html',{'Edit':True,'page':val,'form':form,'display_error':True,'id':uid},context_instance=RequestContext(request))
        else:
            form = PesKgmCgCompanyForm(instance=company)
        return render_to_response('kgm_cg/companydtlform.html',{'Edit':True,'page':val,'form':form,'id':uid},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCgCompanyForm(instance=company)
        return render_to_response('kgm_cg/companydtlform.html',{'Edit':True,'page':val,'form':form,'display_error':True,'id':uid,'error':error},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',2)
def new_lockdate(request):
    val = {'title':'PES - Planning & Development - Performance Ratings', 'feature':'kgm_cg', 'tabgroup':'cmdtltbl', 'urlargs':{}}
    info = PesKgmCgParamDates.objects.get(pk=1)
    return render_to_response('kgm_cg/new_lockdate.html',{'page':val,'info':info},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',3)
def new_lockdateedit(request):
    val = {'title':'PES - Planning & Development - Performance Ratings', 'feature':'kgm_cg', 'tabgroup':'cmdtltbl', 'urlargs':{}}
    lockd = PesKgmCgParamDates.objects.get(pk=1)
    try:
        if request.method == 'POST':
            form = PesKgmCgParamDatesForm(request.POST,instance=lockd)
            if form.is_valid():
                form.save()
                return redirect(new_lockdate)
            else:
                return render_to_response('kgm_cg/new_lockdate.html',{'page':val,'form':form,'display_error':True,'Edit':True},context_instance=RequestContext(request))
        else:
            form = PesKgmCgParamDatesForm(instance=lockd)
        return render_to_response('kgm_cg/new_lockdate.html',{'page':val,'form':form,'Edit':True},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCgParamDatesForm(instance=lockd)
        return render_to_response('kgm_cg/new_lockdate.html',{'page':val,'form':form,'display_error':True,'error':error,'Edit':True},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',2)
def new_ratetbl(request):
    val = {'title':'PES - Planning & Development - Cash Gift Rating Table', 'feature':'kgm_cg', 'tabgroup':'cmdtltbl', 'urlargs':{}, 'gridgroup':'ratetbl'}
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashGiftRating.objects.all(), val['feature'], val['gridgroup'])
    return render_to_response('kgm_cg/rate_list.html',{'page':val},context_instance=RequestContext(request))


@access.has_access('kg-pms-cgt',3)
def new_ratetbl_edit(request, uid):
    rate = PesKgmCashGiftRating.objects.get(id=uid)
    val = {'title':'PES - Planning & Development - Cash Gift Rating Table', 'feature':'kgm_cg', 'tabgroup':'ratetbledit', 'urlargs':{}, 'gridgroup':'ratetbl'}
    try:
        if request.method == 'POST':
            form = PesKgmCashgiftRatingForm(request.POST,instance=rate)
            if form.is_valid():
                rating = form.save(commit=False)
                '''
                if form.cleaned_data['from_rate'] > form.cleaned_data['to_rate']:
                    raise Exception('Rate From is greater than Rate To. Please check your entry.')
                '''
                rating.save()
                return redirect(new_ratetbl)
            else:
                return render_to_response('kgm_cg/new_ratingform.html',{'Edit':True,'page':val,'form':form,'display_error':True,'id':uid},context_instance=RequestContext(request))
        else:
            form = PesKgmCashgiftRatingForm(instance=rate)
        return render_to_response('kgm_cg/new_ratingform.html',{'Edit':True,'page':val,'form':form,'id':uid},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCashgiftRatingForm(instance=rate)
        return render_to_response('kgm_cg/ratingform.html',{'Edit':True,'page':val,'form':form,'display_error':True,'id':uid,'error':error},context_instance=RequestContext(request))



@access.has_access('kg-pms-cgt',1)
def tbl(request):
    val = {'title':'PES - Planning & Development - Cash Gift Table', 'feature':'kgm_cg', 'tabgroup':'cgtbl', 'urlargs':{}, 'gridgroup':'cgtbl'}
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashgiftX.objects.all(), val['feature'], val['gridgroup'])
    return render_to_response('kgm_cg/list.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',1)
def tblview(request, uid):
    val = {'title':'PES - Planning & Development - Cash Gift Table Details', 'feature':'kgm_cg', 'tabgroup':'cgtblvw', 'urlargs':{'uid':{'uid':uid}}, 'gridgroup':'cgtblvw'}
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashgiftMatrix.objects.filter(scheme_id=uid).order_by('lvl_f', 'lvl2_f', 'rate_id'), val['feature'], val['gridgroup'])
    return render_to_response('kgm_cg/list2.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',3)
def tbl_edit(request, uid):
    val = {'title':'PES - Planning & Development - Cash Gift Table', 'feature':'kgm_cg', 'tabgroup':'cgtbledit', 'urlargs':{}, 'gridgroup':'cgtbl'}
    cgtbl = PesKgmCashgiftX.objects.get(id=uid)
    try:
        if request.method == 'POST':
            form = PesKgmCashgiftXForm(request.POST,instance=cgtbl)
            if form.is_valid():
                form.save()
                return redirect(tbl)
            else:
                return render_to_response('kgm_cg/tblform.html',{'page':val,'form':form,'display_error':True,'id':uid},context_instance=RequestContext(request))
        else:
            form = PesKgmCashgiftXForm(instance=cgtbl)
        return render_to_response('kgm_cg/tblform.html',{'page':val,'form':form,'id':uid},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCashgiftXForm(instance=cgtbl)
        return render_to_response('kgm_cg/tblform.html',{'page':val,'form':form,'display_error':True,'error':error,'id':uid},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',3)
def tblview_add(request, uid):
    val = {'title':'PES - Planning & Development - Cash Gift Table Details', 'feature':'kgm_cg', 'tabgroup':'cgtblvwgroup', 'urlargs':{'uid':{'uid':uid}}, 'gridgroup':'cgtblvw'}
    try:
        if request.method == 'POST':
            form = PesKgmCashgiftMatrixForm(request.POST)
            if form.is_valid():
                cgmatrix = form.save(commit=False)
                if form.cleaned_data['lvl_f'] > form.cleaned_data['lvl_t']:
                    raise Exception('Level From is greater than Level To. Please check your entry.')
                if form.cleaned_data['lvl2_f'] > form.cleaned_data['lvl2_t']:
                    raise Exception('Band From is greater than Band To. Please check your entry.')
                cgmatrix.scheme_id = uid
                cgmatrix.save()
                return HttpResponseRedirect(reverse('pes_kgm_cg_tableview',kwargs={'uid': uid}))
            else:
                return render_to_response('kgm_cg/tblviewform.html',{'page':val,'form':form,'display_error':True,'id':uid},context_instance=RequestContext(request))
        else:
            form = PesKgmCashgiftMatrixForm()
        return render_to_response('kgm_cg/tblviewform.html',{'page':val,'form':form,'id':uid},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCashgiftMatrixForm()
        return render_to_response('kgm_cg/tblviewform.html',{'page':val,'form':form,'display_error':True,'id':uid,'error':error},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',3)
def tblview_edit(request, uid):
    matrix = PesKgmCashgiftMatrix.objects.get(id=uid)
    plusrate = int(matrix.plus_rate_id)
    mid = matrix.scheme_id
    val = {'title':'PES - Planning & Development - Cash Gift Table Details', 'feature':'kgm_cg', 'tabgroup':'cgtblvwgroup', 'urlargs':{'uid':{'uid':mid}}, 'gridgroup':'cgtblvw'}
    try:
        if request.method == 'POST':
            form = PesKgmCashgiftMatrixForm(request.POST,instance=matrix)
            if form.is_valid():
                cgmatrix = form.save(commit=False)
                if form.cleaned_data['lvl_f'] > form.cleaned_data['lvl_t']:
                    raise Exception('Level From is greater than Level To. Please check your entry.')
                if form.cleaned_data['lvl2_f'] > form.cleaned_data['lvl2_t']:
                    raise Exception('Band From is greater than Band To. Please check your entry.')
                cgmatrix.save()
                return HttpResponseRedirect(reverse('pes_kgm_cg_tableview',kwargs={'uid': matrix.scheme_id}))
            else:
                return render_to_response('kgm_cg/tblviewform.html',{'page':val,'Edit':True,'form':form,'display_error':True,'uid':uid,'id':mid},context_instance=RequestContext(request))
        else:
            form = PesKgmCashgiftMatrixForm(instance=matrix,initial={'plus_rate_id':plusrate})
        return render_to_response('kgm_cg/tblviewform.html',{'page':val,'Edit':True,'form':form,'uid':uid,'id':mid},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCashgiftMatrixForm(instance=matrix,initial={'plus_rate_id':plusrate})
        return render_to_response('kgm_cg/tblviewform.html',{'page':val,'Edit':True,'form':form,'display_error':True,'uid':uid,'id':mid,'error':error},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',2)
def ratetbl(request):
    val = {'title':'PES - Planning & Development - Cash Gift Rating Table', 'feature':'kgm_cg', 'tabgroup':'cgtbl', 'urlargs':{}, 'gridgroup':'grid3'}
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashgiftDtlsX.objects.all(), val['feature'], val['gridgroup'])
    return render_to_response('kgm_cg/list.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',3)
def ratetbl_add(request):
    val = {'title':'PES - Planning & Development - Cash Gift Rating Table', 'feature':'kgm_cg', 'tabgroup':'ratingtbl', 'urlargs':{}, 'gridgroup':'cgtblvw'}
    try:
        if request.method == 'POST':
            form = PesKgmCashgiftDtlsXForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                if form.cleaned_data['from_rate'] > form.cleaned_data['to_rate']:
                    raise Exception('Rate From is greater than Rate To. Please check your entry.')
                rating.save()
                return redirect(ratetbl)
            else:
                return render_to_response('kgm_cg/ratingform.html',{'page':val,'form':form,'display_error':True},context_instance=RequestContext(request))
        else:
            form = PesKgmCashgiftDtlsXForm()
        return render_to_response('kgm_cg/ratingform.html',{'page':val,'form':form},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCashgiftDtlsXForm()
        return render_to_response('kgm_cg/ratingform.html',{'page':val,'form':form,'display_error':True,'error':error},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',3)
def ratetbl_edit(request, uid):
    rate = PesKgmCashgiftDtlsX.objects.get(id=uid)
    val = {'title':'PES - Planning & Development - Cash Gift Rating Table', 'feature':'kgm_cg', 'tabgroup':'ratingtbl', 'urlargs':{'uid':{'uid':uid}}, 'gridgroup':'cgtblvw'}
    try:
        if request.method == 'POST':
            form = PesKgmCashgiftDtlsXForm(request.POST,instance=rate)
            if form.is_valid():
                rating = form.save(commit=False)
                if form.cleaned_data['from_rate'] > form.cleaned_data['to_rate']:
                    raise Exception('Rate From is greater than Rate To. Please check your entry.')
                rating.save()
                return redirect(ratetbl)
            else:
                return render_to_response('kgm_cg/ratingform.html',{'Edit':True,'page':val,'form':form,'display_error':True,'id':uid},context_instance=RequestContext(request))
        else:
            form = PesKgmCashgiftDtlsXForm(instance=rate)
        return render_to_response('kgm_cg/ratingform.html',{'Edit':True,'page':val,'form':form,'id':uid},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCashgiftDtlsXForm(instance=rate)
        return render_to_response('kgm_cg/ratingform.html',{'Edit':True,'page':val,'form':form,'display_error':True,'id':uid,'error':error},context_instance=RequestContext(request))


#----------------------------------------------------------#
@access.has_access('kg-pms-cg',1)
def ls(request):
    p=Q()
    my_param = request.GET.get('i_n')
    if my_param:
        p= get_filter_operator2(request,'n',['last_name', 'first_name'], 'person', my_param)
    s=Q()
    my_param2 = request.GET.get('i_eb')
    if my_param2:
        s= get_filter_operator2(request,'eb',['last_name', 'first_name'], 'encodedby', my_param2) 
    val = {'title':'PES - Planning & Development - Performance Ratings List', 'feature':'kgm_cg', 'tabgroup':'listgroup', 'urlargs':{}, 'gridgroup':'ls'}
    cg_admin = get_extra_par(request, 'kgm_cashgift_admin')
    cg_admin2 = get_extra_par(request, 'kgm_cashgift_adminsub')
    if cg_admin == '1':
        val['gridgroup'] = 'ls2'
    if cg_admin2 == '1':
        val['gridgroup'] = 'ls3'
    if has_restriction(request,'kg-pms-cg'):
        subs_id=get_people_id_list(request, get_target_org_mod_id(request,'kg-pms-cg'), False, False, True)
        if subs_id:
            val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashgiftAmount.objects.filter(p).filter(s).filter(person_id__in=subs_id), val['feature'], val['gridgroup'])
        else:
            val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashgiftAmount.objects.filter(p).filter(s), val['feature'], val['gridgroup'])
    elif has_restriction(request,'tk-dt-ad-ls'):
        #subs_id=get_people_id_list(request, get_target_org_mod_id(request,'tk-dt-ad-ls'))
        #val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashgiftAmount.objects.filter(p).filter(person_id__in=subs_id), val['feature'], val['gridgroup'])
        val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashgiftAmount.objects.filter(encodedby_id=get_person_id(request)), val['feature'], val['gridgroup'])
    
    else:
        val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmCashgiftAmount.objects.filter(p).filter(s), val['feature'], val['gridgroup'])
    
    
    return render_to_response('kgm_cg/list.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-pms-cg',1)
@transaction.commit_manually()
def add(request):
    person = None
    susp_access = None
    #global LOCK_PERIOD
    info = PesKgmCashGiftLockDates.objects.get(pk=1)
    LOCK_PERIOD = info.datefrom, info.dateto
    val = {'title':'PES - Planning & Development - Performance Ratings Form', 'feature':'kgm_cg', 'tabgroup':'formgroup', 'urlargs':{}}
    forms = {}
    pid = get_person_id(request)
    person_id = request.GET.get('pid')
    if person_id:
        person = Person.objects.get(id=person_id)
        #print person,'yeah'
    try:
        cg_admin = get_extra_par(request, 'kgm_cashgift_admin')
        cg_admin2 = get_extra_par(request, 'kgm_cashgift_adminsub')
        if cg_admin2 or cg_admin:
            susp_access = True
        if request.method == 'POST':
            forms['cg'] = PesPayrollCGForm(request.POST)
            if cglocked() and cg_admin != '1' and cg_admin2 != '1':
                raise Exception('Submission or modification of ratings has been closed.')
            if forms['cg'].is_valid():
                tmp = forms['cg'].save(commit=False)
                tmp.encodedby_id = get_person_id(request)
                if person:
                    assoc = person
                else:
                    assoc = tmp.person
                if has_restriction(request,'kg-pms-cg'):
                    subs_id=get_people_id_list(request, get_target_org_mod_id(request,'kg-pms-cg'), False, False, True)
                    if subs_id:
                        if assoc.id not in subs_id:
                            raise Exception('*This employee is not your subordinate.')
                elif has_restriction(request,'tk-dt-ad-ls'):
                    subs_id=get_people_id_list(request, get_target_org_mod_id(request,'tk-dt-ad-ls'))
                    if assoc.id not in subs_id:
                        raise Exception('This employee is not your subordinate.')
                txn_id = calc_cash_gift(pid, assoc.company_id, Decimal(tmp.score), int(tmp.suspension), tmp.year, None, None)
                dtls = {'year':tmp.year, 'person':assoc.company_id, 'score': str(tmp.score), 'suspension':tmp.suspension}
                PesSecLogs(person_id=get_person_id(request),table='pes_kgm_cashgift_amount', table_id=txn_id, value=json.dumps(dtls), type=1, table2_id=100).save()
                transaction.commit()
                #return redirect(ls)
                yearnow = date.today().year
                url = reverse('pes_kgm_cg_list')+'?i_y='+str(yearnow)
                return HttpResponseRedirect(url)
            else:
                return render_to_response('kgm_cg/form.html',{'forms':forms,'page':val,'display_error':1,'LOCK_PERIOD':LOCK_PERIOD},context_instance=RequestContext(request))
        else:
            #print 'Person',person
            if person:
                forms['cg'] = PesPayrollCGForm2(initial={'suspension':0, 'year':datetime.now().year})
            else:
                forms['cg'] = PesPayrollCGForm(initial={'suspension':0, 'year':datetime.now().year})
            if cglocked() and cg_admin != '1' and cg_admin2 != '1':
                raise Exception('Submission or modification of ratings has been closed.')
        transaction.commit()
        return render_to_response('kgm_cg/form.html',{'forms':forms,'page':val,'person':person,'LOCK_PERIOD':LOCK_PERIOD,'susp_access':susp_access},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        return render_to_response('kgm_cg/form.html',{'forms':forms,'page':val,'error':error,'display_error':1,'person':person,'LOCK_PERIOD':LOCK_PERIOD,'susp_access':susp_access},context_instance=RequestContext(request))
    finally:
        transaction.commit()
        
@access.has_access('kg-pms-cg',1)
@transaction.commit_manually()
def edit(request, uid):
    susp_access = None
    info = PesKgmCashGiftLockDates.objects.get(pk=1)
    LOCK_PERIOD = info.datefrom, info.dateto
    val = {'title':'PES - Planning & Development - Performance Ratings Form', 'feature':'kgm_cg', 'tabgroup':'formgroup3', 'urlargs':{}}
    forms = {}
    req = PesKgmCashgiftAmount.objects.get(pk=uid)
    name = req.person.last_name+', '+req.person.first_name
    pid = get_person_id(request)
    try:        
        cg_admin = get_extra_par(request, 'kgm_cashgift_admin') 
        cg_admin2 = get_extra_par(request, 'kgm_cashgift_adminsub')
        if cg_admin2 or cg_admin:
            susp_access = True
        cg = PesKgmCashgiftAmount.objects.get(pk=uid, is_final=0)
        if request.method == 'POST':
            forms['cg'] = PesPayrollCGForm(request.POST, instance=cg)
            if cglocked() and cg_admin != '1' and cg_admin2 != '1':
                raise Exception('Submission or modification of ratings has been closed.')
            if forms['cg'].is_valid():
                tmp = forms['cg'].save(commit=False)
                tmp.encodedby_id = get_person_id(request)
                cid = req.person.company_id
                #req.delete()
                txn_id = calc_cash_gift(pid, cid, Decimal(tmp.score), int(tmp.suspension), tmp.year, None, req)
                dtls = {'year':tmp.year, 'person':cid, 'score': str(tmp.score), 'suspension':tmp.suspension}
                PesSecLogs(person_id=get_person_id(request),table='pes_kgm_cashgift_amount', table_id=txn_id, value=json.dumps(dtls), type=2, table2_id=100).save()
                transaction.commit()
                #return redirect(ls)
                yearnow = date.today().year
                url = reverse('pes_kgm_cg_list')+'?i_y='+str(yearnow)
                return HttpResponseRedirect(url)
            else:
                return render_to_response('kgm_cg/form.html',{'forms':forms,'page':val,'display_error':1, 'edit':True, 'id':uid, 'name':name,'LOCK_PERIOD':LOCK_PERIOD,'susp_access':susp_access},context_instance=RequestContext(request))
        else:
            forms['cg'] = PesPayrollCGForm(instance=cg)
            if cglocked() and cg_admin != '1' and cg_admin2 != '1':
                raise Exception('Submission or modification of ratings has been closed.')
        transaction.commit()
        return render_to_response('kgm_cg/form.html',{'forms':forms,'page':val, 'edit':True, 'id':uid, 'name':name,'LOCK_PERIOD':LOCK_PERIOD,'susp_access':susp_access},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        return render_to_response('kgm_cg/form.html',{'forms':forms,'page':val,'error':error,'display_error':1, 'edit':True, 'id':uid, 'name':name,'LOCK_PERIOD':LOCK_PERIOD,'susp_access':susp_access},context_instance=RequestContext(request))
    finally:
        transaction.commit()

@access.has_access('kg-pms-cg',1)
@transaction.commit_on_success()
def delete(request, uid):
    #global LOCK_PERIOD
    cg_admin = get_extra_par(request, 'kgm_cashgift_admin') 
    cg_admin2 = get_extra_par(request, 'kgm_cashgift_adminsub') 
    
    if cglocked() and cg_admin != '1' and cg_admin2 != '1':
        raise Exception('Submission or modification of ratings has been closed.')
        
    j = PesKgmCashgiftAmount.objects.get(pk=uid, is_final=0)
    j.delete()
    return HttpResponseRedirect(reverse('pes_kgm_cg_list'))

@access.has_access('kg-pms-cg',2)
@transaction.commit_on_success()
def filesubmit(request, uid):
    val = {'title':'PES - Planning & Development - Performance Ratings List', 'feature':'kgm_cg', 'tabgroup':'listgroup', 'urlargs':{}, 'gridgroup':'ls'}
    try:
        reg = PesKgmCashgiftAmount.objects.get(pk=uid)
        if reg.file_submission == 1:
            raise Exception('This entry has a submitted file already.')
        reg.file_submission = 1
        reg.save()
        yearnow = date.today().year
        url = reverse('pes_kgm_cg_list')+'?i_y='+str(yearnow)
        return HttpResponseRedirect(url)
    except Exception as error:
        return render_to_response('kgm_cg/list.html',{'page':val,'display_error':True,'error':error},context_instance=RequestContext(request))

def upload(request):
    val = {'title':'PES - Planning & Development - Performance Ratings Batch Upload', 'feature':'kgm_cg', 'tabgroup':'formgroup2', 'urlargs':{}}
    forms = {}
    try:
        print 'wews1'
        if request.method == 'POST':
            print 'wews2'
            forms['cg'] = PesPayrollCGUploadForm(request.POST, request.FILES)
            if forms['cg'].is_valid():
                fl = forms['cg'].save(commit=False)
                fl.save()
                res = gen_cashgift(forms['cg'].cleaned_data['year'], None, settings.MEDIA_ROOT+str(fl.file))
                return render_to_response('kgm_cg/summary.html',{'summary':res, 'page':val},context_instance=RequestContext(request))
            else:
                return render_to_response('kgm_cg/form2.html',{'forms':forms,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            forms['cg'] = PesPayrollCGUploadForm()
        return render_to_response('kgm_cg/form2.html',{'forms':forms,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        return render_to_response('kgm_cg/form2.html',{'forms':forms,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-rpkg-cg',1)
def masterlist(request):
    val = {'title':'PES - Planning & Development - Reports - Cash Gift Master List', 'feature':'kgm_cg', 'tabgroup':'formgroup4', 'urlargs':{}}
    forms = {}
    if request.method == 'POST':
        forms['cg'] = PesPayrollCGMasteListForm(request.POST)
        if forms['cg'].is_valid():
            cg_admin = get_extra_par(request, 'kgm_cashgift_admin')
            typ = 0
            if cg_admin == '1':
                typ = 1
        
            entry_ids = []
            if has_restriction(request,'kg-pms-cg'):
                print 'kg-pms-cg----------------------'
                subs_id=get_people_id_list(request, get_target_org_mod_id(request,'kg-pms-cg'), False, False, True)
                print subs_id
                if subs_id:
                    entry_ids = PesKgmCashgiftAmount.objects.filter(person_id__in=subs_id).values_list('id', flat=True)
                    entry_ids = list(entry_ids)
                print 'entries', entry_ids
                
            elif has_restriction(request,'tk-dt-ad-ls'):
                entry_ids = PesKgmCashgiftAmount.objects.filter(encodedby_id=get_person_id(request)).values_list('id', flat=True)
                entry_ids = list(entry_ids)
            
            return export_cg_masterlist(forms['cg'].cleaned_data['year'], typ, entry_ids)
                
            
        else:
            print 'all------------'
            return render_to_response('kgm_cg/form3.html',{'forms':forms,'page':val,'display_error':1},context_instance=RequestContext(request))
    else:
        forms['cg'] = PesPayrollCGMasteListForm()
    return render_to_response('kgm_cg/form3.html',{'forms':forms,'page':val},context_instance=RequestContext(request))

@access.has_access('kg-pms-as',1)
def associates(request):
    #pids = {}
    time_keeping_people_id_list = []
    yr = date.today().year
    dto = date(yr,12,28)
    dfrom = date(yr,11,30)
    
    #print cds.query
    if has_restriction(request,'kg-pms-cg'):
        time_keeping_people_id_list=get_people_id_list(request, get_target_org_mod_id(request,'kg-pms-cg'), False, False, True)  
    elif has_restriction(request,'tk-dt-ds'):
        time_keeping_people_id_list = get_people_id_list(request, get_target_org_mod_id(request,'tk-dt-ds'))
    cds = PesPisCds.objects.filter(person_id__in=time_keeping_people_id_list).filter(Q(contract_end_date__isnull=True)|Q(contract_end_date__gte=dto)).filter(Q(datehired__lte=dfrom)).values_list('person_id',flat=True)
    pids = {'id__in':list(cds)}
    val = {'title':'PES - Planning & Development - Performance Ratings', 'feature':'kgm_cg', 'tabgroup':'listgroup', 'urlargs':{}, 'gridgroup':'grid2'}
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, Person.objects.filter(**pids).exclude(id=206), val['feature'], val['gridgroup'])
    return render_to_response('kgm_cg/list.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',2)
def lockdate(request):
    val = {'title':'PES - Planning & Development - Performance Ratings', 'feature':'kgm_cg', 'tabgroup':'cgtbl', 'urlargs':{}}
    info = PesKgmCashGiftLockDates.objects.get(pk=1)
    return render_to_response('kgm_cg/lockdate.html',{'page':val,'info':info},context_instance=RequestContext(request))

@access.has_access('kg-pms-cgt',3)
def lockdateedit(request):
    val = {'title':'PES - Planning & Development - Performance Ratings', 'feature':'kgm_cg', 'tabgroup':'cgtbl', 'urlargs':{}}
    lockd = PesKgmCashGiftLockDates.objects.get(pk=1)
    try:
        if request.method == 'POST':
            form = PesKgmCashGiftLockDatesForm(request.POST,instance=lockd)
            if form.is_valid():
                form.save()
                return redirect(lockdate)
            else:
                return render_to_response('kgm_cg/lockdate.html',{'page':val,'form':form,'display_error':True,'Edit':True},context_instance=RequestContext(request))
        else:
            form = PesKgmCashGiftLockDatesForm(instance=lockd)
        return render_to_response('kgm_cg/lockdate.html',{'page':val,'form':form,'Edit':True},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmCashGiftLockDatesForm(instance=lockd)
        return render_to_response('kgm_cg/lockdate.html',{'page':val,'form':form,'display_error':True,'error':error,'Edit':True},context_instance=RequestContext(request))

def cglocked():
    info = PesKgmCashGiftLockDates.objects.get(pk=1)
    if info.datefrom <= date.today() <= info.dateto:
        return False
    return True

def ls_paf(request):
    val = {'title':'PES - Planning & Development - Performance Appraisal List (PAF)', 'feature':'kgm_cg', 'tabgroup':'listgrouppaf', 'urlargs':{}, 'gridgroup':'ls'}
    return render_to_response('kgm_cg/listpaf.html',{'page':val},context_instance=RequestContext(request))

def add_paf(request):
    raise Exception('add paf') 