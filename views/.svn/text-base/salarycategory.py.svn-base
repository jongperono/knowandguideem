from django.shortcuts import render_to_response,redirect, HttpResponse
from django.template import RequestContext
from django.db import transaction
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from django.http import HttpResponseRedirect,Http404
from apps.intent.pes.security.decorator import access
from apps.intent.pes.security.helpers.access import get_extra_par
import datetime
#models
from apps.intent.pes.knowandguideem.models.peskgmsalarycategory import PesKgmSalarycategory
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
#forms
from apps.intent.pes.knowandguideem.forms.salarycatform import SalaryCategoryForm,SalaryCategoryFormSet
import xlwt
from apps.intent.pes.knowandguideem.models.peskgmpositionlevel import PesKgmPositionLevel
from apps.intent.pes.knowandguideem.models.peskgmstep import PesKgmStep
from apps.intent.pes.knowandguideem.models.peskgmsteppositionlevecategory import PesKgmSteppositionlevelCategory
import collections
from xlwt.Style import XFStyle
from xlwt.Formatting import Borders
from apps.intent.pes.base.helpers.pes_session import get_person_id
from apps.intent.pes.security.models.access import PesSecUsrOrgpriv
from apps.intent.pes.base.helpers.universal import display_view_err

@access.has_access('kg-cm-ss-ls',1)
def pes_salarycat_list(request):
    temp = get_extra_par(request,"max_band_level")
    val = {}
    val['title'] = 'PES - Planning & Development - Salary Structure'
    val['feature'] = 'salarycategory'
    val['tabgroup'] = 'listsalarycat'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    area = {}
    subarea = {}
    p_id = get_person_id(request)
    orgpriv = PesSecUsrOrgpriv.objects.filter(person_id=p_id,module_name='kg-cm-ss-ls')
    if orgpriv:
        #print 'xxxxxxxxx'
        if orgpriv[0].area:
            area = {'area_id':orgpriv[0].area_id}
        if orgpriv[0].sub_area:
            subarea = {'subarea_id':orgpriv[0].sub_area_id}
        #print area,subarea
        #print temp
    if temp:
        val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmSalarycategory.objects.filter(band__lte=temp,deleted=0).filter(**area).filter(**subarea), val['feature'], val['gridgroup'])
    else:
        val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmSalarycategory.objects.filter(**area).filter(**subarea), val['feature'], val['gridgroup'])
    return render_to_response('salarycategory/salarycatlist.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-cm-ss-ls',2)
@transaction.commit_on_success
def pes_salarycat_create(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Salary Structure'
    val['feature'] = 'salarycategory'
    val['tabgroup'] = 'createsalarycat'
    try:
        if request.method == 'POST':
            form = SalaryCategoryForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['datefrom'] > form.cleaned_data['dateto']:
                    raise Exception("Your effectivity date from is later than effectivity date to.")
                salarycat = form.save(commit=False)
                salarycat.deleted = 0
                salarycat.save()
                detailed_log(salarycat,request,1)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(pes_salarycat_list)
                else:
                    form = SalaryCategoryForm()
                    return render_to_response('salarycategory/salarycatform.html',{'form':form,'page':val,'message':1},context_instance=RequestContext(request))
            else:
                return render_to_response('salarycategory/salarycatform.html',{'form':form,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            form = SalaryCategoryForm()
        return render_to_response('salarycategory/salarycatform.html',{'form':form,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form = SalaryCategoryForm()
        return render_to_response('salarycategory/salarycatform.html',{'form':form,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-cm-ss-ls',2)
@transaction.commit_on_success
def pes_salarycat_modify(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Salary Structure'
    val['feature'] = 'salarycategory'
    val['tabgroup'] = 'createsalarycat'
    SalaryCat = PesKgmSalarycategory.objects.get(pk=id)
    form=SalaryCategoryForm(request.POST,instance=SalaryCat)
    try:
        if request.method == 'POST':
            if form.is_valid():
                if form.cleaned_data['datefrom'] > form.cleaned_data['dateto']:
                    raise Exception("Your effectivity date from is later than effectivity date to.")
                form.save()
                detailed_log(SalaryCat,request,2)
                transaction.commit()
                return redirect(pes_salarycat_list)
            else:
                return render_to_response('salarycategory/salarycatform.html',{'form':form,'page':val,'display_error':1},context_instance=RequestContext(request))
        else:
            form = SalaryCategoryForm(instance=SalaryCat)
        return render_to_response('salarycategory/salarycatform.html',{'form':form,'Edit':SalaryCat,'id':id,'page':val},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        SalaryCat = PesKgmSalarycategory.objects.get(pk=id)
        form = SalaryCategoryForm(instance=SalaryCat)
        return render_to_response('salarycategory/salarycatform.html',{'form':form,'Edit':SalaryCat,'id':id,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-cm-ss-ls',2)
@transaction.commit_on_success
def pes_salarycat_delete(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Salary Structure'
    val['feature'] = 'salarycategory'
    val['tabgroup'] = 'listsalarycat'
    val['urlargs'] = {}
    try:
        try:
            p=PesKgmSalarycategory.objects.get(pk=id)
            p=detailed_log(p,request,3)
            p.delete()
            
         
        except:
            a = PesKgmSalarycategory.objects.get(pk=id)
            desc = a.description + "- (DELETED)"
            a.description = desc
            a.deleted = 1
            a.date_del = datetime.date.today()
            a.save()
        transaction.commit()
        return redirect(pes_salarycat_list)
    except Exception as error:
        transaction.rollback()
        SalaryCat = PesKgmSalarycategory.objects.all()
        return render_to_response('salarycategory/salarycatlist.html',{'list': SalaryCat,'error':error,'page':val,'display_error':1},context_instance=RequestContext(request))
        #return render_to_response('address/list.html',{'error':1},context_instance=RequestContext(request))

@access.has_access('kg-cm-ss-ls',2)
@transaction.commit_on_success
def pes_salarycat_archive(request,id):
    temp = get_extra_par(request,"max_band_level")
    val = {}
    val['title'] = 'PES - Planning & Development - Salary Structure'
    val['feature'] = 'salarycategory'
    val['tabgroup'] = 'listsalarycat'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    try:
        p = PesKgmSalarycategory.objects.get(pk=id)
        p.archived_date = datetime.date.today()
        p.status = 2
        p.save()
        p = detailed_log(p, request, 3)
        return redirect(pes_salarycat_list)
    except Exception as error:
        if temp:
            val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmSalarycategory.objects.filter(band__lte=temp,deleted=0), val['feature'], val['gridgroup'])
        else:
            val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmSalarycategory.objects.all(), val['feature'], val['gridgroup'])
        return render_to_response('salarycategory/salarycatlist.html',{'page':val,'display_error':True,'error':error},context_instance=RequestContext(request))


@access.has_access('kg-rp-sc',2)
def report(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Salary Structure Report'
    val['feature'] = 'salarycategory'
    val['tabgroup'] = 'reportsalarycat'
    val['urlargs'] = {}
    code = {}
    to = {}
    status = {}
    description = {}
    bandlevel = {}
    row = 0
    try:
        if request.method == 'POST':
            form = SalaryCategoryFormSet(request.POST,prefix='salarycategory')
            bandlist = PesKgmPositionLevel.objects.filter(deleted=0).order_by('description')
            levellist = PesKgmStep.objects.filter(deleted=0).order_by('description')
            book = xlwt.Workbook(encoding='utf8',style_compression=2)
            numstyle = XFStyle()
            numstyle.num_format_str = "#,##0.00"
            numstyle.alignment.horz = xlwt.Alignment.HORZ_RIGHT
            numstyleleft = XFStyle()
            numstyleleft.num_format_str = "#,##0.00"
            numstyleleft.alignment.horz = xlwt.Alignment.HORZ_RIGHT
            numstyleleft.borders.left = Borders.THIN
            numstyleright = XFStyle()
            numstyleright.num_format_str = "#,##0.00"
            numstyleright.alignment.horz = xlwt.Alignment.HORZ_RIGHT
            numstyleright.borders.right = Borders.THIN
            numstylemin = XFStyle()
            numstylemin.num_format_str = "#,##0.00"
            numstylemin.alignment.horz = xlwt.Alignment.HORZ_RIGHT
            numstylemin.font.height = 150
            numstylemin.borders.left = Borders.THIN
            sheet = book.add_sheet('Sheet 1')
            sheet.col(0).width = 15 * 256
            sheet.col(1).width = 10 * 256
            sheet.write_merge(row,row+2,0,1,'BAND/LEVEL',xlwt.easyxf('font: bold on, height 230; border: left thin,top thin; align: horiz center, vert center;'))
            dic = {}
            lists = []
            pluscol = 4
            column_f = 2
            column_t = 5
            col1 = 2
            col2 = 3
            col3 = 4
            col4 = 5
            for s in form:
                if s.is_valid():
                    try:
                        sc = PesKgmSteppositionlevelCategory.objects.filter(salary_category_id=int(s.cleaned_data['salarycat']))
                        if sc.count() > 0:
                            dic[sc.count()] = sc
                            lists.append(sc[0].salary_category_id)
                            sheet.write_merge(row,row,column_f,column_t,sc[0].salary_category.code,xlwt.easyxf('align: horiz center;font: bold on,height 270; border: left thin, right thin,top thin, bottom thin;'))
                            sheet.write(row+1,col1,sc[0].salary_category.minimum_wage,numstylemin)
                            sheet.write(row+1,col2,sc[0].salary_category.statusname,xlwt.easyxf('align: horiz center, vert center; font: height 150;'))
                            sheet.write(row+1,col3,str(sc[0].salary_category.datefrom),xlwt.easyxf('align: horiz center, vert center; font: height 150;'))
                            sheet.write(row+1,col4,str(sc[0].salary_category.dateto),xlwt.easyxf('align: horiz center, vert center; font: height 150; border: right thin;'))
                            sheet.write(row+2,col1,'MINIMUM',xlwt.easyxf('align: horiz center, vert center; font: height 150; border: left thin, top thin;'))
                            sheet.write(row+2,col2,'MAXIMUM',xlwt.easyxf('align: horiz center, vert center; font: height 150; border: top thin;'))
                            sheet.write(row+2,col3,'COLA',xlwt.easyxf('align: horiz center, vert center; font: height 150; border: top thin;'))
                            sheet.write(row+2,col4,'ALLOWANCE',xlwt.easyxf('align: horiz center, vert center; font: height 150; border: right thin, top thin;'))
                            column_f += 4
                            column_t += 4
                            col1 += pluscol
                            col2 += pluscol
                            col3 += pluscol
                            col4 += pluscol
                    except Exception as error:
                        print error
            #print dic
            #print lists
            #lists.reverse()
            col1 = 2
            col2 = 3
            col3 = 4
            col4 = 5
            totalcol = 1 + (4 * len(lists))
            row += 2
            for b in bandlist:
                row += 1
                sheet.write_merge(row,row,0,totalcol,b.description.upper(),xlwt.easyxf('font: italic on; border: left thin,right thin, top thin, bottom thin;'))
                #print row,'BAND'
                for l in levellist:
                    row += 1
                    sheet.write(row,1,l.description.upper(),xlwt.easyxf('align: horiz center; border: left thin;'))
                    #print row,'LEVEL'
                    lss = PesKgmSteppositionlevelCategory.objects.filter(step_position_level__position_level_id=b.id,step_position_level__step_id=l.id)
                    if lss:
                        #print lss.count(),'COUNT'
                        for ls in lists:
                            spc = lss.filter(salary_category_id=ls)
                            if spc:
                                #print row,'------------3'
                                sheet.write(row,col1,spc[0].basic,numstyleleft)
                                sheet.write(row,col2,spc[0].maximum,numstyle)
                                sheet.write(row,col3,spc[0].cola,numstyle)
                                sheet.write(row,col4,spc[0].allowance,numstyleright)
                                #print spc[0].salary_category.code,b.description,l.description,spc[0].basic,spc[0].cola,spc[0].allowance
                            else:
                                #print 'pass'
                                sheet.write(row,col1,'',numstyleleft)
                                sheet.write(row,col2,'',numstyle)
                                sheet.write(row,col3,'',numstyle)
                                sheet.write(row,col4,'',numstyleright)
                            col1 += pluscol
                            col2 += pluscol
                            col3 += pluscol
                            col4 += pluscol
                    else:
                        for ls in lists:
                            sheet.write(row,col1,' ',numstyleleft)
                            sheet.write(row,col2,' ',numstyle)
                            sheet.write(row,col3,' ',numstyle)
                            sheet.write(row,col4,' ',numstyleright)
                            col1 += pluscol
                            col2 += pluscol
                            col3 += pluscol
                            col4 += pluscol
                    
                    col1 = 2
                    col2 = 3
                    col3 = 4
                    col4 = 5
                    '''
                    for sc in lists:
                        if continuenow == True:
                            for d in dic[sc]:
                                if b.id == d.step_position_level.position_level_id and l.id == d.step_position_level.step_id:
                                    print d.salary_category.code,b.description,l.description,d.basic,d.cola,d.allowance
                                #else:
                                #    print d.salary_category.code,b.description,l.description
                                    #continuenow = False
                                    #break
                        #else:
                            #continuenow = True
                            #break
                    '''
            #pass
            #print collections.OrderedDict(sorted(dic.items()))
            #return HttpResponse(dic)
            #print code,description,bandlevel,status,to
            #lists = PesKgmSalarycategory.objects.filter(deleted=0)
            sheet.write_merge(row+1,row+1,0,totalcol,'',xlwt.easyxf('border: top thin;'))
            #row = 0
            '''
            sheet.write(0,0,'CODE',xlwt.easyxf('font: bold on;'))
            sheet.write(0,1,'DESCRIPTION',xlwt.easyxf('font: bold on;'))
            sheet.write(0,2,'T.O',xlwt.easyxf('font: bold on;'))
            sheet.write(0,3,'BAND/LEVEL',xlwt.easyxf('font: bold on;'))
            sheet.write(0,4,'STATUS',xlwt.easyxf('font: bold on;'))
            sheet.col(0).width = 20 * 256
            sheet.col(1).width = 40 * 256
            sheet.col(2).width = 45 * 256
            sheet.col(3).width = 25 * 256
            sheet.col(4).width = 10 * 256
            for i in lists:
                print i.id
                row += 1
                sheet.write(row,0,i.code)
                sheet.write(row,1,i.description)
                sheet.write(row,2,i.to.description)
                sheet.write(row,3,i.start_step_position_level.position_level.description + i.start_step_position_level.step.description)
                sheet.write(row,4,i.statusname)
            '''
            response = HttpResponse(mimetype='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' % "PES_SALARY_CATEGORY_REPORT.xls"
            book.save(response)
            return response
        else:
            form = SalaryCategoryFormSet(prefix='salarycategory')
        return render_to_response('salarycategory/salarycatreport.html',{'page':val,'form':form},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        form = SalaryCategoryFormSet(prefix='salarycategory')
        return render_to_response('salarycategory/salarycatreport.html',{'page':val,'form':form,'error':error,'display_error':1},context_instance=RequestContext(request))

