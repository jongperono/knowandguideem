from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.db import transaction
import datetime
from django.db.models import Q
#models
from apps.intent.pes.knowandguideem.models.peskgmviewrpb import PesKgmViewRpb

#forms
from apps.intent.pes.knowandguideem.forms.peskgmviewrpbform import PesKgmViewRpbForm
#helpers
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
from apps.intent.pes.base.helpers.pesfilters import get_filter_operator2
from apps.intent.pes.base.helpers.pes_session import get_person_id

@access.has_access('kg-ot-ra-ls',1)
def index(request):
    p=Q()
    my_param = request.GET.get('i_e')
    if my_param:
        p= get_filter_operator2(request,'e',['last_name', 'first_name'], 'person', my_param)
    val = {}
    val['title'] = "PES - Planning & Development - View RPB"
    val['feature'] = 'viewrpb'
    val['tabgroup'] = 'listgroup'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmViewRpb.objects.filter(p), val['feature'], val['gridgroup'])
    return render_to_response('viewrpb/list.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-ot-ra-ls',2)
@transaction.commit_on_success
def create(request):
    person_id = get_person_id(request)
    val = {}
    val['title'] = "PES - Planning & Development - View RPB"
    val['feature'] = 'viewrpb'
    val['tabgroup'] = 'creategroup'
    try:
        if request.method == 'POST':
            form = PesKgmViewRpbForm(request.POST)
            if form.is_valid():
                rpb = form.save(commit=False)
                rpb.applied_by_id = person_id
                rpb.date_applied = datetime.date.today()
                rpb.save()
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form = PesKgmViewRpbForm()
                    return render_to_response('viewrpb/form.html',{'form':form,'page':val,'message':1},context_instance=RequestContext(request))
            else:
                return render_to_response('viewrpb/form.html',{'form':form,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            form = PesKgmViewRpbForm()
        return render_to_response('viewrpb/form.html',{'form':form,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form = PesKgmViewRpbForm()
        return render_to_response('viewrpb/form.html',{'form':form,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-ot-ra-ls',2)
@transaction.commit_on_success
def edit(request,id):
    person_id = get_person_id(request)
    val = {}
    val['title'] = "PES - Planning & Development - View RPB"
    val['feature'] = 'viewrpb'
    val['tabgroup'] = 'creategroup'
    Step = PesKgmViewRpb.objects.get(pk=id)
    try:
        if request.method == 'POST':
            form=PesKgmViewRpbForm(request.POST,instance=Step)
            if form.is_valid():
                rpb = form.save(commit=False)
                rpb.applied_by_id = person_id
                rpb.date_applied = datetime.date.today()
                rpb.save()
                transaction.commit()
                return redirect(index)
            else:
                return render_to_response('viewrpb/form.html',{'form':form,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            form = PesKgmViewRpbForm(instance=Step)
        return render_to_response('viewrpb/form.html',{'form':form,'Edit':Step,'id':id,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        transaction.rollback()
        form = PesKgmViewRpbForm(instance=Step)
        return render_to_response('viewrpb/form.html',{'form':form,'Edit':Step,'id':id,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-ot-ra-ls',2)
@transaction.commit_on_success
def delete(request,id):
    val = {}
    val['title'] = "PES - Planning & Development - View RPB"
    val['feature'] = 'viewrpb'
    val['tabgroup'] = 'listgroup'
    try:
        PesKgmViewRpb.objects.get(pk=id).delete()
        transaction.commit()
        return redirect(index)
    except Exception as error:
        transaction.rollback()
        Step = PesKgmViewRpb.objects.all()
        return render_to_response('viewrpb/list.html',{'list': Step,'error':error,'page':val,'display_error':1},context_instance=RequestContext(request))
        #return render_to_response('address/list.html',{'error':1},context_instance=RequestContext(request))
