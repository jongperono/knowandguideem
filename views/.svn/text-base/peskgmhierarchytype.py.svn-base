from django.http import HttpResponse
from django.db.models import Max
from apps.intent.pes.knowandguideem.models.peskgmhierarchytype import PesKgmHierarchytype
from apps.intent.pes.knowandguideem.forms.peskgmhierarchytype import PesKgmHierarchytypeForm
#from apps.intent.party.models.Partyroletype import Partyroletype
#from apps.intent.party.forms.PartyTypeForm import PartyTypeForm
from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext    
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from django.db import  transaction
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-cs-ch-ls',1)
def index(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy Level'
    val['feature'] = 'hierarchytype'
    val['tabgroup'] = 'listgroup'
    val['gridgroup'] = 'subgrid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmHierarchytype.objects.filter(deleted=0), val['feature'], val['gridgroup'])

    return render_to_response('hierarchytype/list.html',{'page' : val},context_instance=RequestContext(request))

@access.has_access('kg-cs-ch-ls',2)
@transaction.commit_on_success
def create(request):  
    
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy Level'
    val['feature'] = 'hierarchytype'
    val['tabgroup'] = 'formgroup'
    max_id = PesKgmHierarchytype.objects.all().aggregate(Max('sequence'))['sequence__max']
    #return HttpResponse(max_id)
    try:
        if(request.method=='POST'):
            form=PesKgmHierarchytypeForm(request.POST)
    
            if(form.is_valid()):
                typ = form.save(commit=False)
                typ.deleted = 0
                typ.save()
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    max_id = PesKgmHierarchytype.objects.all().aggregate(Max('sequence'))['sequence__max']
                    form=PesKgmHierarchytypeForm(initial={'sequence': max_id+1})
                    return render_to_response('hierarchytype/form.html',{'form':form, 'create':form,'page' : val,'message':'Region has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('hierarchytype/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=PesKgmHierarchytypeForm(initial={'sequence': max_id+1})
            return render_to_response('hierarchytype/form.html',{'form':form, 'create':form,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form=PesKgmHierarchytypeForm()
        return render_to_response('hierarchytype/form.html',{'form':form, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-cs-ch-ls',2)
@transaction.commit_on_success
def edit(request,id):  
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy Level'
    val['feature'] = 'hierarchytype'
    val['tabgroup'] = 'formgroup'
    try:
        if(request.method=='POST'):
            form=PesKgmHierarchytypeForm(request.POST, instance=get_object_or_404(PesKgmHierarchytype, pk=id))
            if form.is_valid() :
                form.save()
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=PesKgmHierarchytypeForm(instance=get_object_or_404(PesKgmHierarchytype, pk=id))
                    return render_to_response('hierarchytype/form.html',{'form':form, 'edit':form,'id':id, 'page' : val,'message':'Region has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('hierarchytype/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=PesKgmHierarchytypeForm(instance=get_object_or_404(PesKgmHierarchytype, pk=id))
            return render_to_response('hierarchytype/form.html',{'form':form, 'edit':form,'id':id, 'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form=PesKgmHierarchytypeForm(instance=get_object_or_404(PesKgmHierarchytype, pk=id))
        return render_to_response('hierarchytype/form.html',{'form':form,'e':1,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-cs-ch-ls',2)
@transaction.commit_on_success
def delete(request,id):
    try:
        #hierarchytype=PesKgmHierarchytype.objects.get(pk=id)
        #hierarchytype.delete()
        #transaction.commit()
        try:
            PesKgmHierarchytype.objects.get(pk=id,status=0).delete()
        except:
            a = PesKgmHierarchytype.objects.get(pk=id,status=0)
            desc = a.description + "- (DELETED)"
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        return redirect(index)
    except Exception as error:
        transaction.rollback()
        hierarchytype = PesKgmHierarchytype.objects.all().order_by('id')
        val = {}
        val['title'] = 'PES - Planning & Development - Hierarchy Level'
        val['feature'] = 'hierarchytype'
        val['tabgroup'] = 'listgroup' 
        return render_to_response('hierarchytype/list.html',{'list':hierarchytype,'error':error,'display_error':'true','page':val},context_instance=RequestContext(request))

         
  

