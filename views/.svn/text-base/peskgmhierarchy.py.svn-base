from django.http import HttpResponse
from apps.intent.pes.knowandguideem.models.peskgmhierarchy import PesKgmHierarchy
from apps.intent.pes.knowandguideem.forms.peskgmhierarchy import PesKgmHierarchyForm,PesKgmHierarchyGPForm
from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext
from apps.intent.base.helpers.errormsg import BootStrapErrorList
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.pes.security.helpers.access import get_extra_par
from apps.intent.pes.knowandguideem.forms.peskgmhierarchy import CompanyFilterForm
from apps.intent.pes.knowandguideem.helpers.hierarchy import Hierarchy
from apps.intent.pes.knowandguideem.forms.rpbform import RPBReportForm
from apps.intent.pes.knowandguideem.models.peskgmrpb import PesKgmRpb
import xlwt
from apps.intent.pes.pis.views.pespisemployeeinfo import rpb_info2
from apps.intent.pes.knowandguideem.views.rpb import date_to_str
from apps.intent.pes.base.helpers.pes_session import get_person_id
from apps.intent.pes.security.models.logs import PesSecLogs
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-cs-cs-ls',1)
def index(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy'
    val['feature'] = 'peshierarchy'
    val['tabgroup'] = 'listgroup'
    gp = get_extra_par(request,"gp_encoder")
    if gp:
        val['gridgroup'] = 'hierarchy_gp'
    else:
        val['gridgroup'] = 'hierarchy_grid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmHierarchy.objects.filter(deleted=0), val['feature'], val['gridgroup'])
    return render_to_response('peshierarchy/list.html',{'page' : val},context_instance=RequestContext(request))

@access.has_access('kg-cs-cs-tv',1)
def tree_view(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy'
    val['feature'] = 'peshierarchy'
    val['tabgroup'] = 'listgroup'
    
    c = request.GET.get('hierarchy', None)
    if c:
      print 'x ', c
      #hierarchy = PesKgmHierarchy.objects.filter(id=c).order_by('id').exclude(parent_id__isnull=False)
      return render_to_response('peshierarchy/treeview.html',{'page' : val, 'cid':c},context_instance=RequestContext(request))
    else:
      form = CompanyFilterForm()
      return render_to_response('peshierarchy/treeview_form.html',{'page' : val, 'form':form},context_instance=RequestContext(request))

def update_hierarchy(request):
    id=request.POST['hierarchy_id']
    hierarchytype_id=request.POST['new_hierarchy_value']
    
    hierarchy=PesKgmHierarchy.objects.get(pk=id)
    hierarchy.hierarchytype_id=hierarchytype_id
    hierarchy.save()
    detailed_log(hierarchy,request,2)
    return HttpResponse(str(hierarchy.numcode)+"-"+str(hierarchytype_id))

@access.has_access('kg-cs-cs-ls',2)
def create(request):  
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy'
    val['feature'] = 'peshierarchy'
    val['tabgroup'] = 'formgroup'
    try:
        gp = get_extra_par(request,"gp_encoder")
        if(request.method=='POST'):
            form=PesKgmHierarchyForm(request.POST)
            if(form.is_valid()):
                if form.cleaned_data['datefrom'] > form.cleaned_data['dateto']:
                    raise Exception("Your effectivity date from is later than effectivity date to.")
                if form.cleaned_data['parent']:
                    if form.cleaned_data['hierarchytype'].sequence <= form.cleaned_data['parent'].hierarchytype.sequence:
                        raise Exception("Your parent's hierarchy level is lower than your hierarchy level")
                if gp:
                    raise Exception("You cannot add a new hierarchy. Please check your access.")
                h=form.save(commit=False)
                h.deleted = 0
                h.save()
                detailed_log(h,request,1)
                if request.POST['save']=="save":
                    #return redirect(tree_view)
                    id=h.id
                    cid = Hierarchy.get_hierarchy_top_parent(id)
                    return HttpResponseRedirect(reverse('peskgmhierarchytreeviewlist')+str("?hierarchy="+str(cid)+"#txtid-"+str(id)))
                else:
                    #form=PesKgmHierarchyForm()
                    
                    #return HttpResponseRedirect(reverse('peskgmhierarchytreeviewaddlist',kwargs={form.id}))
                
                    return render_to_response('peshierarchy/form.html',{'form':form, 'create':form,'page' : val,'message':'Hierarchy has been saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('peshierarchy/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=PesKgmHierarchyForm()
            if gp:
                raise Exception("You cannot add a new hierarchy. Please check your access.")
            return render_to_response('peshierarchy/form.html',{'form':form, 'create':form,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form=PesKgmHierarchyForm()
        return render_to_response('peshierarchy/form.html',{'form':form, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-cs-cs-ls',2)
def tree_view_add(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy'
    val['feature'] = 'peshierarchy'
    val['tabgroup'] = 'formgroup'
    try:
        gp = get_extra_par(request,"gp_encoder")
        if(request.method=='POST'):
            form=PesKgmHierarchyForm(request.POST)
            if(form.is_valid()):
                if form.cleaned_data['datefrom'] > form.cleaned_data['dateto']:
                    raise Exception("Your effectivity date from is later than effectivity date to.")
                if form.cleaned_data['parent']:
                    if form.cleaned_data['hierarchytype'].sequence <= form.cleaned_data['parent'].hierarchytype.sequence:
                        raise Exception("Your parent's hierarchy level is lower than your hierarchy level")
                if gp:
                    raise Exception("You cannot add a new hierarchy. Please check your access.")
                h=form.save(commit=False)
                h.deleted = 0
                h.save()
                detailed_log(h,request,1)
                if request.POST['save']=="save":
                    #return redirect(index)
                    id=h.id
                    cid = Hierarchy.get_hierarchy_top_parent(id)
                    return HttpResponseRedirect(reverse('peskgmhierarchytreeviewlist')+str("?hierarchy="+str(cid)+"#txtid-"+str(id)))
                else:
                    hierarchy = get_object_or_404(PesKgmHierarchy, pk=id)
                    form = PesKgmHierarchyForm(instance=hierarchy) 
                    return render_to_response('peshierarchy/add.html',{'form':form, 'create':form,'page' : val,'parent':id,'message':'Hierarchy has been saved.'},context_instance=RequestContext(request)) 
            else:
                return render_to_response('peshierarchy/add.html',{'form':form, 'create':form,'page' : val,'parent':id,'display_error':'true'},context_instance=RequestContext(request))
        else:
            hierarchy = get_object_or_404(PesKgmHierarchy, pk=id)
            form = PesKgmHierarchyForm(instance=hierarchy) 
            if gp:
                raise Exception("You cannot add a new hierarchy. Please check your access.")
            return render_to_response('peshierarchy/add.html',{'form':form, 'create':form,'page' : val,'parent':id},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        hierarchy = get_object_or_404(PesKgmHierarchy, pk=id)
        form = PesKgmHierarchyForm(instance=hierarchy)
        return render_to_response('peshierarchy/add.html',{'form':form, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-cs-cs-ls',2)
def edit_treeview(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy'
    val['feature'] = 'peshierarchy'
    val['tabgroup'] = 'formgroup'
    try:
        gp = get_extra_par(request,"gp_encoder")
        hierarchy=PesKgmHierarchy.objects.get(pk=id)
        if request.method=='POST':
            if gp:
                form = PesKgmHierarchyGPForm(request.POST,instance=hierarchy)
            else:
                form = PesKgmHierarchyForm(request.POST,instance=hierarchy)
            if form.is_valid():
                if gp:
                    pass
                else:
                    if form.cleaned_data['datefrom'] > form.cleaned_data['dateto']:
                        raise Exception("Your effectivity date from is later than effectivity date to.")
                    if form.cleaned_data['parent']:
                        if form.cleaned_data['hierarchytype'].sequence <= form.cleaned_data['parent'].hierarchytype.sequence:
                            raise Exception("Your parent's hierarchy level is lower than your hierarchy level")
                form=form.save(commit=True) 
                detailed_log(hierarchy,request,2)
                if request.POST['save']=="save":
                    cid = Hierarchy.get_hierarchy_top_parent(form.id)
                    return HttpResponseRedirect(reverse('peskgmhierarchytreeviewlist')+str("?hierarchy="+str(cid)+"#txtid-"+str(form.id)))
                else:
                    form = PesKgmHierarchyForm(instance=hierarchy)
                    if gp:
                        form = PesKgmHierarchyGPForm(instance=hierarchy)
                    return render_to_response('peshierarchy/editreeviewform.html',{'form':form, 'edit':form,'id':id,'page' : val,'message':'Hierarchy has been Saved.','gp':gp,'list':hierarchy},context_instance=RequestContext(request))
            else:
                return render_to_response('peshierarchy/editreeviewform.html',{'form':form, 'edit':form,'id':id,'page' : val,'display_error':'true','gp':gp,'list':hierarchy},context_instance=RequestContext(request))
        else:
            form = PesKgmHierarchyForm(instance=hierarchy)
            if gp:
                form = PesKgmHierarchyGPForm(instance=hierarchy)
            return render_to_response('peshierarchy/editreeviewform.html',{'form':form, 'edit':form,'id':id,'page' : val,'gp':gp,'list':hierarchy},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmHierarchyForm(instance=hierarchy)
        if gp:
            form = PesKgmHierarchyGPForm(instance=hierarchy)
        return render_to_response('peshierarchy/form.html',{'form':form, 'edit':form,'id':id,'error':error,'page' : val,'display_error':'true','gp':gp,'list':hierarchy},context_instance=RequestContext(request))

@access.has_access('kg-cs-cs-ls',2)
def edit(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy'
    val['feature'] = 'peshierarchy'
    val['tabgroup'] = 'formgroup'
    try:
        gp = get_extra_par(request,"gp_encoder")
        hierarchy = PesKgmHierarchy.objects.get(pk=id)
        if request.method=='POST':
            if gp:
                form = PesKgmHierarchyGPForm(request.POST,instance=hierarchy)
            else:
                form = PesKgmHierarchyForm(request.POST,instance=hierarchy)
            if form.is_valid():
                if gp:
                    pass
                else:
                    if form.cleaned_data['datefrom'] > form.cleaned_data['dateto']:
                        raise Exception("Your effectivity date from is later than effectivity date to.")
                    if form.cleaned_data['parent']:
                        if form.cleaned_data['hierarchytype'].sequence <= form.cleaned_data['parent'].hierarchytype.sequence:
                            raise Exception("Your parent's hierarchy level is lower than your hierarchy level")
                form.save(commit=True) 
                detailed_log(hierarchy,request,2)
                if request.POST['save']:
                    cid = Hierarchy.get_hierarchy_top_parent(id)
                    return HttpResponseRedirect(reverse('peskgmhierarchytreeviewlist')+str("?hierarchy="+str(cid)+"#txtid-"+str(id)))
                else:
                    form = PesKgmHierarchyForm(instance=hierarchy)
                    if gp:
                        form = PesKgmHierarchyGPForm(instance=hierarchy)
                    return render_to_response('peshierarchy/form.html',{'form':form, 'edit':form,'id':id,'page' : val,'message':'Hierarchy has been Saved.','gp':gp,'list':hierarchy},context_instance=RequestContext(request))
            else:
                return render_to_response('peshierarchy/form.html',{'form':form, 'edit':form,'id':id,'page' : val,'display_error':'true','gp':gp,'list':hierarchy},context_instance=RequestContext(request))
        else:
            form = PesKgmHierarchyForm(instance=hierarchy)
            if gp:
                form = PesKgmHierarchyGPForm(instance=hierarchy)
            return render_to_response('peshierarchy/form.html',{'form':form, 'edit':form,'id':id,'page' : val,'gp':gp,'list':hierarchy},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PesKgmHierarchyForm(instance=hierarchy)
        if gp:
            form = PesKgmHierarchyGPForm(instance=hierarchy) 
        return render_to_response('peshierarchy/form.html',{'form':form, 'edit':form,'id':id,'error':error,'page' : val,'display_error':'true','gp':gp,'list':hierarchy},context_instance=RequestContext(request))

@access.has_access('kg-cs-cs-ls',2)
def delete(request,id):
    uid = id
    try:
        #hierarchy=get_object_or_404(PesKgmHierarchy, pk=id)
        #parent_id=hierarchy.parent_id
        #hierarchy.delete()
        try:
            p=PesKgmHierarchy.objects.get(pk=id)
            detailed_log(p,request,3)
            p.delete()
          
        except:
            a = PesKgmHierarchy.objects.get(pk=id)
            desc = a.description + "- (DELETED)"
            parent_id = a.parent_id
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        cid = Hierarchy.get_hierarchy_top_parent(parent_id)
        remarks = request.GET['remarks']
        PesSecLogs(person_id=get_person_id(request),table="pes_kgm_hierarchy", table_id=uid, type=5, value='Delete Reason: '+remarks,table2_id=34).save()
        return HttpResponseRedirect(reverse('peskgmhierarchytreeviewlist')+str("?hierarchy="+str(cid)+"#txtid-"+str(parent_id)))
    except Exception as error:
        val = {}
        val['title'] = 'PES - Planning & Development - Hierarchy'
        val['feature'] = 'peshierarchy'
        val['tabgroup'] = 'listgroup'
        hierarchy = PesKgmHierarchy.objects.all().order_by('id')
        return render_to_response('peshierarchy/list.html',{'list':hierarchy,'error':error,'display_error':'true','page':val},context_instance=RequestContext(request))

@access.has_access('kg-cs-cs-ls',2)
def delete_tree(request,id):
    uid = id
    try:
        #hierarchy=get_object_or_404(PesKgmHierarchy, pk=id)
        #parent_id=hierarchy.parent_id
        #hierarchy.delete()
        try:
            p=PesKgmHierarchy.objects.get(pk=id)
            detailed_log(p,request,3)
            p.delete()
        except:
            a = PesKgmHierarchy.objects.get(pk=id)
            desc = a.description + "- (DELETED)"
            parent_id = a.parent_id
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        cid = Hierarchy.get_hierarchy_top_parent(parent_id)
        remarks = request.GET['remarks']
        PesSecLogs(person_id=get_person_id(request),table="pes_kgm_hierarchy", table_id=uid, type=5, value='Delete Reason: '+remarks,table2_id=34).save()
        return HttpResponseRedirect(reverse('peskgmhierarchytreeviewlist')+str("?hierarchy="+str(cid)+"#txtid-"+str(parent_id)))
    except Exception as error:
        val = {}
        val['title'] = 'PES - Planning & Development - Hierarchy'
        val['feature'] = 'peshierarchy'
        val['tabgroup'] = 'listgroup'
        hierarchy = PesKgmHierarchy.objects.all().order_by('id')
        return render_to_response('peshierarchy/list.html',{'list':hierarchy,'error':error,'display_error':'true','page':val},context_instance=RequestContext(request))

@access.has_access('kg-rp-cs',1)
def report(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Hierarchy'
    val['feature'] = 'peshierarchy'
    val['tabgroup'] = 'reportgroup'
    val['urlargs'] = {}
    company = {}
    code = {}
    description = {}
    gpdiv = {}
    gpdpt = {}
    parent = {}
    employstatus = {}
    try:
        if request.method == 'POST':
            try:
                company = {'company_id':int(request.POST['company'])}
            except:
                pass
            try:
                if request.POST['code'] != '':
                    code = {'numcode':request.POST['code']}
            except:
                pass
            try:
                if request.POST['description'] != '':
                    description = {'description':request.POST['description']}
            except:
                pass
            try:
                if request.POST['gpdiv'] != '':
                    gpdiv = {'gpcode_div':request.POST['gpdiv']}
            except:
                pass
            try:
                if request.POST['gpdpt'] != '':
                    gpdpt = {'gpcode_dept':request.POST['gpdpt']}
            except:
                pass
            try:
                parent = {'parent_id':int(request.POST['parent'])}
            except:
                pass
            try:
                employstatus = {'hierarchytype_id':int(request.POST['type'])}
            except:
                pass
            print company,code,description,gpdiv,gpdpt,parent,employstatus
            lists = PesKgmHierarchy.objects.filter(deleted=0).filter(**company).filter(**code).filter(**description).filter(**gpdiv).filter(**gpdpt).filter(**parent).filter(**employstatus)
            print lists,'---------------'
            book = xlwt.Workbook(encoding='utf8',style_compression=2)
            sheet = book.add_sheet('Sheet 1')
            row = 0
            sheet.write(0,0,'CODE',xlwt.easyxf('font: bold on;'))
            sheet.write(0,1,'DESCRIPTION',xlwt.easyxf('font: bold on;'))
            sheet.write(0,2,'GP-CODE DIV',xlwt.easyxf('font: bold on;'))
            sheet.write(0,3,'GP-CODE DEPT',xlwt.easyxf('font: bold on;'))
            sheet.write(0,4,'PARENT',xlwt.easyxf('font: bold on;'))
            sheet.write(0,5,'LEVEL',xlwt.easyxf('font: bold on;'))
            sheet.write(0,6,'COMPANY',xlwt.easyxf('font: bold on;'))
            sheet.write(0,7,'DATE FROM',xlwt.easyxf('font: bold on;'))
            sheet.write(0,8,'DATE TO',xlwt.easyxf('font: bold on;'))
            sheet.col(0).width = 40 * 256
            sheet.col(1).width = 45 * 256
            sheet.col(4).width = 45 * 256
            sheet.col(5).width = 15 * 256
            sheet.col(6).width = 30 * 256
            for i in lists:
                row += 1
                sheet.write(row,0,i.numcode)
                sheet.write(row,1,i.description)
                sheet.write(row,2,i.gpcode_div)
                sheet.write(row,3,i.gpcode_dept)
                sheet.write(row,4,i.parentname)
                sheet.write(row,5,i.hierarchytype.description)
                sheet.write(row,6,i.company.name)
                sheet.write(row,7,str(i.datefrom))
                sheet.write(row,8,str(i.dateto))
            response = HttpResponse(mimetype='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' % "PES_COMPANY_STRUCTURE_LIST.xls"
            book.save(response)
            return response
        else:
            return render_to_response('peshierarchy/report.html',{'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        return render_to_response('peshierarchy/report.html',{'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))


