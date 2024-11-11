from django.http import HttpResponse
from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext    
from apps.intent.pes.knowandguideem.models.peskgmpositionclassification import PesKgmPositionClassification
from apps.intent.pes.knowandguideem.forms.peskgmpositionclassification import PesKgmPositionClassificationForm,\
    PositionReportForm
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from django.db import  transaction
from apps.intent.pes.base.helpers.pesfilters import is_filter_found, get_filter_operator
from apps.intent.pes.security.decorator import access
from django.db.models import Q
from apps.intent.pes.base.helpers.pesfilters import get_filter_operator2
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
import xlwt
from apps.intent.pes.pis.models.pespiscds import PesPisCds
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-po-cl-ls',1)
def index(request):
    p = Q()
    my_param = request.GET.get('i_n')
    if my_param:
        p = get_filter_operator2(request,'n',['description',], 'to', my_param)
    #a=is_filter_found(request, 'start_step_position_level')
    #p=get_filter_operator(request, 'start_step_position_level', 'step__description')


    # if is_filter_found(request, 'start_step_position_level') == True:
    #   array=request.GET['i_start_step_position_level']   
    #   array=array.split('-')
    #   l=str(array[0])
    
    
    # position_level='Level 2'
    #step='C'
     
    # f = {'start_step_position_level__position_level__description__icontains': position_level,'start_step_position_level__step__description__icontains': step}
    #return HttpResponse(f)
    val = {}
    val['title'] = "PES - Planning & Development - Position Classification"
    val['feature'] = 'positionclassification'
    val['tabgroup'] = 'listgroup'
    val['gridgroup'] = 'subgrid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmPositionClassification.objects.filter(deleted=0).filter(p), val['feature'], val['gridgroup'])
    return render_to_response('positionclassification/list.html',{'page' : val},context_instance=RequestContext(request))

@access.has_access('kg-po-cl-ls',2)
@transaction.commit_on_success
def create(request):  
    
    val = {}
    val['title'] = "PES - Planning & Development - Position Classification"
    val['feature'] = 'positionclassification'
    val['tabgroup'] = 'formgroup'

    try:
        if(request.method=='POST'):
            form=PesKgmPositionClassificationForm(request.POST)
    
            if(form.is_valid()):
                c = form.save(commit=False)
                c.deleted = 0
                c.save()
                detailed_log(c,request,1)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=PesKgmPositionClassificationForm()
                    return render_to_response('positionclassification/form.html',{'form':form, 'create':form,'page' : val,'message':'Region has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('positionclassification/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=PesKgmPositionClassificationForm()
            return render_to_response('positionclassification/form.html',{'form':form, 'create':form,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form=PesKgmPositionClassificationForm()
        return render_to_response('positionclassification/form.html',{'form':form, 'create':form,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-po-cl-ls',2)
@transaction.commit_on_success
def edit(request,id):  
    val = {}
    val['title'] = "PES - Planning & Development - Position Classification"
    val['feature'] = 'positionclassification'
    val['tabgroup'] = 'formgroup'
    try:
        if(request.method=='POST'):
            form=PesKgmPositionClassificationForm(request.POST, instance=get_object_or_404(PesKgmPositionClassification, pk=id))
            if form.is_valid() :
                form.save()
                detailed_log(form,request,2)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(index)
                else:
                    form=PesKgmPositionClassificationForm(instance=get_object_or_404(PesKgmPositionClassification, pk=id))
                    return render_to_response('positionclassification/form.html',{'form':form, 'edit':form,'id':id, 'page' : val,'message':'Region has been Saved.'},context_instance=RequestContext(request))
            else:
                return render_to_response('positionclassification/form.html',{'form':form, 'create':form,'page' : val,'display_error':'true'},context_instance=RequestContext(request))
        else:
            form=PesKgmPositionClassificationForm(instance=get_object_or_404(PesKgmPositionClassification, pk=id))
            return render_to_response('positionclassification/form.html',{'form':form, 'edit':form,'id':id, 'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form=PesKgmPositionClassificationForm(instance=get_object_or_404(PesKgmPositionClassification, pk=id))
        return render_to_response('positionclassification/form.html',{'form':form,'e':1,'error':error,'page' : val,'display_error':'true'},context_instance=RequestContext(request))

@access.has_access('kg-po-cl-ls',2)
@transaction.commit_on_success
def delete(request,id):
    try:
        try:
            _class = PesKgmPositionClassification.objects.get(pk=id,status=0)
            detailed_log(_class,request,3)
            _class.delete()
        except:
            a = PesKgmPositionClassification.objects.get(pk=id,status=0)
            #region.delete()
            cds = PesPisCds.objects.filter(position_id=id).filter(Q(contract_end_date__isnull=True)|Q(contract_end_date__gte=datetime.date.today())).count()
            if cds > 0:
                raise Exception('You cannot delete this entry. Please check the Balance count.')
            desc = a.description + "- (DELETED)"
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
            detailed_log(a,request,3)
        transaction.commit()
        return redirect(index)
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        region = PesKgmPositionClassification.objects.all().order_by('id')
        val = {}
        val['title'] = "PES - Planning & Development - Position Classification"
        val['feature'] = 'positionclassification'
        val['tabgroup'] = 'listgroup' 
        return render_to_response('positionclassification/list.html',{'list':region,'error':error,'display_error':'true','page':val},context_instance=RequestContext(request))

@access.has_access('kg-rp-pc',2)
def report(request):
    val = {}
    val['title'] = "PES - Planning & Development - Position Classification"
    val['feature'] = 'positionclassification'
    val['tabgroup'] = 'reportgroup'
    code = {}
    to = {}
    status = {}
    description = {}
    bandlevel = {}
    try:
        if request.method == 'POST':
            form = PositionReportForm(request.POST)
            print request.POST
            if form.is_valid():
                if form.cleaned_data['code'] != '':
                    code = {'code__icontains':form.cleaned_data['code']}
                if form.cleaned_data['description'] != '':
                    description = {'description__icontains':form.cleaned_data['description']}
                try:
                    to = {'to_id':int(form.cleaned_data['to'])}
                except:
                    pass
                try:
                    bandlevel = {'start_step_position_level_id':int(form.cleaned_data['bandlevel'])}
                except:
                    pass
                try:
                    status = {'status':int(form.cleaned_data['status'])}
                except:
                    pass
            print code,description,bandlevel,status,to
            lists = PesKgmPositionClassification.objects.filter(deleted=0).filter(**status).filter(**to).filter(**code).filter(**description).filter(**bandlevel)
            book = xlwt.Workbook(encoding='utf8',style_compression=2)
            sheet = book.add_sheet('Sheet 1')
            row = 0
            sheet.write(0,0,'CODE',xlwt.easyxf('font: bold on;'))
            sheet.write(0,1,'DESCRIPTION',xlwt.easyxf('font: bold on;'))
            sheet.write(0,2,'T.O',xlwt.easyxf('font: bold on;'))
            sheet.write(0,3,'BAND/LEVEL',xlwt.easyxf('font: bold on;'))
            sheet.write(0,4,'STATUS',xlwt.easyxf('font: bold on;'))
            sheet.write(0,5,'CATEGORY',xlwt.easyxf('font: bold on;'))
            sheet.col(0).width = 20 * 256
            sheet.col(1).width = 40 * 256
            sheet.col(2).width = 45 * 256
            sheet.col(3).width = 25 * 256
            sheet.col(4).width = 10 * 256
            sheet.col(5).width = 20 * 256
            for i in lists:
                print i.id
                row += 1
                sheet.write(row,0,i.code)
                sheet.write(row,1,i.description)
                sheet.write(row,2,i.to.description)
                sheet.write(row,3,i.start_step_position_level.position_level.description + i.start_step_position_level.step.description)
                sheet.write(row,4,i.statusname)
                sheet.write(row,5,i.categoryname)
            response = HttpResponse(mimetype='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' % "PES_POSITION_LIST.xls"
            book.save(response)
            return response
        else:
            form = PositionReportForm()
        return render_to_response('positionclassification/report.html',{'page':val,'form':form},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = PositionReportForm()
        return render_to_response('positionclassification/report.html',{'page':val,'form':form,'error':error,'display_error':1},context_instance=RequestContext(request))

