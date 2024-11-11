from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.db import transaction
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
#models
from apps.intent.pes.knowandguideem.models.peskgmjd import PesKgmJd
from apps.intent.upload.models.upload import Fileupload
#forms
from apps.intent.pes.knowandguideem.forms.jdform import JobDescriptionForm,\
    JobDescriptionEditForm
from apps.intent.upload.forms.uploadform import FileuploadForm
#helpers
from apps.intent.upload.helpers.upload import downloadfile, downloadfile2
from apps.intent.pes.base.helpers.pesfilters import get_filtered_queryset
from apps.intent.pes.security.decorator import access
import datetime
from apps.intent.pes.base.helpers.pes_detailed_log import detailed_log
from apps.intent.pes.base.helpers.pdf import html_2_pdf
from django.conf import settings
from apps.intent.middleware.http import WatchMiddleware
from apps.intent.pes.base.helpers.universal import display_view_err


@access.has_access('kg-jd-ls',1)
def pes_jobdesc_list(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'listjd'
    val['urlargs'] = {}
    val['gridgroup'] = 'grid'
    val['gridlist'], val['gridlist_count'] = get_filtered_queryset(request, PesKgmJd.objects.filter(deleted=0), val['feature'], val['gridgroup'])
    return render_to_response('jobdescription/jobdesclist.html',{'page':val},context_instance=RequestContext(request))

@access.has_access('kg-jd-ls',2)
@transaction.commit_on_success
def pes_jobdesc_create(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'createjd'
    val['urlargs'] = {}
    temp = defaul_value()
    try:
        if request.method == 'POST':
            form = JobDescriptionForm(request.POST)
            #print request.POST
            #return HttpResponse('Test')
            if form.is_valid():
                salarycat = form.save(commit=False)
                salarycat.deleted = 0
                salarycat.save()
                detailed_log(salarycat,request,1)
                transaction.commit()
                if request.POST['save']=="save":
                    return redirect(pes_jobdesc_list)
                else:
                    form = JobDescriptionForm()
                    return render_to_response('jobdescription/jobdescform.html',{'form':form,'page':val,'message':1,'default':temp},context_instance=RequestContext(request))
            else:
                return render_to_response('jobdescription/jobdescform.html',{'form':form,'page':val,'display_error':1,'default':temp},context_instance=RequestContext(request))
        else:
            form = JobDescriptionForm()
        return render_to_response('jobdescription/jobdescform.html',{'form':form,'page':val,'default':temp},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form = JobDescriptionForm()
        return render_to_response('jobdescription/jobdescform.html',{'form':form,'page':val,'error':error,'display_error':1,'default':temp},context_instance=RequestContext(request))

@access.has_access('kg-jd-ls',2)
@transaction.commit_on_success
def pes_jobdesc_modify(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'createjd'
    val['urlargs'] = {}
    JobDesc = PesKgmJd.objects.get(pk=id)
    string = JobDesc.value#.replace('\n','').replace('&#39;',"'").replace('&quot;','"').replace('&gt;','>').replace('&lt;','<').replace('&amp;','&')
    #print str(string)
    try:
        if request.method == 'POST':
            form = JobDescriptionEditForm(request.POST,instance=JobDesc)
            #print str(request.POST['value'])
            if form.is_valid():
                jd = form.save(commit=False)
                jd.value = str(request.POST['value'])
                jd.save()
                detailed_log(JobDesc,request,2)
                transaction.commit()
                return redirect(pes_jobdesc_list)
            else:
                return render_to_response('jobdescription/jobdesceditform.html',{'form':form,'page':val,'display_error':1,'html':str(string)},context_instance=RequestContext(request))
        else:
            form = JobDescriptionEditForm(instance=JobDesc)
        return render_to_response('jobdescription/jobdesceditform.html',{'form':form,'Edit':JobDesc,'id':id,'page':val,'html':str(string)},context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form = JobDescriptionEditForm(instance=JobDesc)
        return render_to_response('jobdescription/jobdesceditform.html',{'form':form,'Edit':JobDesc,'id':id,'page':val,'error':error,'display_error':1,'html':str(string)},context_instance=RequestContext(request))

@access.has_access('kg-jd-ls',2)
@transaction.commit_on_success
def pes_jobdesc_delete(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'listjd'
    val['urlargs'] = {}
    try:
        try:
            JobDesc=PesKgmJd.objects.get(pk=id)
            detailed_log(JobDesc,request,3)
            JobDesc.delete()
        except:
            jd = PesKgmJd.objects.get(pk=id)
            desc = jd.description + "- (DELETED)"
            jd.description = desc
            jd.deleted = 1
            jd.date_del = datetime.date.today()
            jd.save()
        transaction.commit()
        return redirect(pes_jobdesc_list)
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        JobDesc = PesKgmJd.objects.all()
        return render_to_response('jobdescription/jobdesclist.html',{'list': JobDesc,'error':error,'page':val,'display_error':1},context_instance=RequestContext(request))
        #return render_to_response('address/list.html',{'error':1},context_instance=RequestContext(request))

@access.has_access('kg-jd-ls',1)
def pes_jobdesc_info(request,id):
    fileupload = Fileupload.objects.filter(reference_key=id,uploadname="JD Upload",status='1')
    jd = PesKgmJd.objects.get(pk=id)
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'jdinfo'
    val['urlargs'] = {'urlarg1':{'id':id}}
    return render_to_response('jobdescription/jdinfo.html',{'list': fileupload,'id':id,'jd':jd,'page':val},context_instance=RequestContext(request))

@access.has_access('kg-jd-ls',2)
@transaction.commit_on_success
def pes_jobdesc_info_upload(request,id):
    jd = PesKgmJd.objects.get(pk=id)
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'jdupload'
    val['urlargs'] = {'urlarg1':{'id':jd.id}}
    try:
        if request.POST:
            form = FileuploadForm(request.POST, request.FILES)        
            if form.is_valid():
                obj = form.save(commit=False)
                jd = PesKgmJd.objects.get(pk=id)
                obj.useraccount_id = 32
                obj.file_type = request.FILES['file'].content_type
                obj.file_size = request.FILES['file'].size
                obj.subsystem="PES"
                obj.module="KnowAndGuideEm"
                obj.submodule="Job Description"
                obj.uploadname="JD Upload"
                obj.status = 1
                obj.reference_key = id
                obj.save()
                transaction.commit()
                return HttpResponseRedirect(reverse('jobdesc_info',kwargs={'id': jd.id}))
            else:
                raise Http404
        else:
            form = FileuploadForm()
            return render_to_response('jobdescription/jdupload.html', {'form': form,'id':jd.id,'page':val}, context_instance=RequestContext(request))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        form = FileuploadForm()
        return render_to_response('jobdescription/jdupload.html', {'form': form,'id':jd.id,'page':val,'error':error}, context_instance=RequestContext(request))

@access.has_access('po',1)
def pes_jobdesc_file_download(request,id):
    wm = WatchMiddleware()
    if wm.get_host(request) == '10.33.11.121':
        return downloadfile(request,id)
    else:
        return downloadfile2(request,id)

@access.has_access('kg-jd-ls',2)
def pes_jobdesc_print(request,uid):
    data = {}
    jd = PesKgmJd.objects.get(pk=uid)
    data['object'] = jd
    data['html'] = jd.value
    data['count'] = 0
    data['staticroot'] = settings.STATIC_ROOT
    if jd.appr1:
        data['count'] += 1
    if jd.appr2:
        data['count'] += 1
    if jd.appr3:
        data['count'] += 1
    if jd.appr4:
        data['count'] += 1
    if jd.appr5:
        data['count'] += 1
    if jd.appr6:
        data['count'] += 1
    #print data
    return html_2_pdf(jd.code, 'jobdescription/jdprint.html', data)

@access.has_access('kg-jd-ls',1)
def pes_jobdesc_archive(request):
    fileupload = Fileupload.objects.filter(uploadname="JD Upload",status=0)
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'jdarchive'
    val['urlargs'] = {}
    return render_to_response('jobdescription/jdarchive.html',{'list': fileupload,'page':val},context_instance=RequestContext(request))

@access.has_access('kg-jd-ls',2)
@transaction.commit_on_success
def pes_jobdesc_archive_upload(request,jd_id,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'jdinfo'
    val['urlargs'] = {'urlarg1':{'id':jd_id}}
    jd = PesKgmJd.objects.get(pk=jd_id)
    try:
        upload = Fileupload.objects.get(pk=id)
        upload.status = 0
        upload.save()
        transaction.commit()
        return HttpResponseRedirect(reverse('jobdesc_info',kwargs={'id': jd.id}))
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        fileupload = Fileupload.objects.filter(reference_key=jd_id,uploadname="JD Upload")
        jd = PesKgmJd.objects.get(pk=jd_id)
        return render_to_response('jobdescription/jdinfo.html',{'list': fileupload,'id':id,'jd':jd,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@access.has_access('kg-jd-ls',2)
@transaction.commit_on_success
def pes_jobdesc_restore_upload(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'jdarchive'
    val['urlargs'] = {}
    try:
        upload = Fileupload.objects.get(pk=id)
        upload.status = 1
        upload.save()
        transaction.commit()
        return redirect(pes_jobdesc_archive)
    except Exception as error:
        error = display_view_err(error)
        transaction.rollback()
        fileupload = Fileupload.objects.filter(uploadname="JD Upload",status=0)
        return render_to_response('jobdescription/jdarchive.html',{'list': fileupload,'id':id,'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))

@transaction.commit_on_success
def jd_archive_delete(request,id):
    val = {}
    val['title'] = 'PES - Planning & Development - Job Description'
    val['feature'] = 'jobdescription'
    val['tabgroup'] = 'jdarchive'
    val['urlargs'] = {}
    try:
        upload = Fileupload.objects.get(pk=id)
        upload.status = 2
        upload.save()
        return redirect(pes_jobdesc_archive)
    except Exception as error:
        return render_to_response('jobdescription/jdarchive.html',{'list': upload,'page':val,'display_error':True,'error':error},context_instance=RequestContext(request))
    
def defaul_value():
    temp = '''<p><strong>ORGANIZATIONAL&nbsp;RELATIONSHIP:</strong></p>
            <p>Reports&nbsp;to&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; :&nbsp;</p>
            <p>Supervises &nbsp; &nbsp; &nbsp; &nbsp; :&nbsp;</p>
            <p>Coordinates&nbsp;with :&nbsp;</p>
            <p><strong>GENERAL&nbsp;JOB&nbsp;DEFINITION:</strong></p>
            <p>&nbsp;</p>
            <p><strong>DUTIES&nbsp;AND&nbsp;RESPONSIBILITIES/ACCOUNTABILITIES:</strong></p>
            <ol>
            <li>&nbsp;</li>
            </ol>
            <p><span style="text-decoration: underline;"><em>People&nbsp;Management</em></span></p>
            <ol>
            <li>Ensures&nbsp;all&nbsp;Company&nbsp;policies&nbsp;and&nbsp;procedures&nbsp;are&nbsp;properly&nbsp;disseminated&nbsp;and&nbsp;implemented.</li>
            <li>Trains&nbsp;associates&nbsp;of&nbsp;their&nbsp;functions&nbsp;and&nbsp;responsibilities&nbsp;to&nbsp;achieve&nbsp;the&nbsp;department's&nbsp;goals.</li>
            <li>Ensures&nbsp;strong&nbsp;and&nbsp;efficient&nbsp;teamwork&nbsp;culture&nbsp;exists&nbsp;within&nbsp;the&nbsp;team</li>
            <li>Conducts&nbsp;regular&nbsp;performance&nbsp;reviews&nbsp;to&nbsp;make&nbsp;sure&nbsp;associates&nbsp;are&nbsp;performing&nbsp;well,&nbsp;to&nbsp;identify&nbsp;and&nbsp;resolve&nbsp;&nbsp;issues&nbsp;and&nbsp;concerns,&nbsp;&nbsp;and&nbsp;to&nbsp;continuously&nbsp;motivate&nbsp;associates.</li>
            <li>Proposes&nbsp;and&nbsp;recommends&nbsp;employment&nbsp;movements&nbsp;for&nbsp;his/her&nbsp;associates.</li>
            <li>Approves&nbsp;requests&nbsp;for&nbsp;leave&nbsp;of&nbsp;absence,&nbsp;overtime,&nbsp;offset,&nbsp;change&nbsp;of&nbsp;schedule,&nbsp;and&nbsp;other&nbsp;admin&nbsp;functions.</li>
            <li>Enforces&nbsp;disciplinary&nbsp;actions&nbsp;to&nbsp;associates&nbsp;in&nbsp;accordance&nbsp;to&nbsp;The&nbsp;NCCC&nbsp;Spirit.</li>
            <li>Establishes&nbsp;and&nbsp;maintains&nbsp;effective&nbsp;working&nbsp;relationships&nbsp;with&nbsp;subordinates,&nbsp;co-workers,&nbsp;other&nbsp;departments&nbsp;and&nbsp;suppliers.</li>
            <li>Conducts&nbsp;final&nbsp;interview&nbsp;to&nbsp;applicants&nbsp;recommended&nbsp;by&nbsp;PEOPLE&nbsp;for&nbsp;hiring.</li>
            <li>Conducts&nbsp;meetings&nbsp;with&nbsp;his&nbsp;subordinates&nbsp;for&nbsp;updates.</li>
            <li>Consults&nbsp;with&nbsp;immediate&nbsp;head&nbsp;issues&nbsp;and&nbsp;concerns&nbsp;that&nbsp;are&nbsp;beyond&nbsp;his&nbsp;approval.</li>
            </ol>
            <p><span style="text-decoration: underline;"><em>Company&nbsp;Involvement</em></span></p>
            <ol>
            <li>Abides&nbsp;by&nbsp;the&nbsp;NCCC&nbsp;Business&nbsp;Unit&rsquo;s&nbsp;set&nbsp;House&nbsp;Rules.</li>
            <li>Attends&nbsp;meetings&nbsp;(i.e.&nbsp;Weekly&nbsp;or&nbsp;Monthly&nbsp;Meetings)&nbsp;as&nbsp;required&nbsp;by&nbsp;immediate&nbsp;head&nbsp;and&nbsp;other&nbsp;departments.</li>
            <li>Participates&nbsp;in&nbsp;company&nbsp;initiated&nbsp;activities&nbsp;specially&nbsp;those&nbsp;that&nbsp;promote&nbsp;the&nbsp;NCCC&nbsp;Core&nbsp;Values,&nbsp;namely:</li>
            </ol>
            <ul style="list-style-type: circle;">
            <li>
            <ol style="list-style-type: lower-alpha;">
            <li>Sales&nbsp;Up</li>
            <li>Cost&nbsp;Down</li>
            <li>Working&nbsp;in&nbsp;a&nbsp;Healthy&nbsp;and&nbsp;Safe&nbsp;Environment&nbsp;(WHSE)</li>
            <li>Positively&nbsp;Out-Of-The-Box&nbsp;Service&nbsp;(POS)</li>
            <li>Company&nbsp;extra-curricular&nbsp;activities</li>
            </ol>
            </li>
            </ul>
            <ol>
            <li>Suggests&nbsp;and&nbsp;participate&nbsp;in&nbsp;achieving&nbsp;branch&nbsp;plans&nbsp;and&nbsp;goals.</li>
            <li>Represents&nbsp;and&nbsp;promotes&nbsp;positive&nbsp;image&nbsp;of&nbsp;the&nbsp;Company&nbsp;at&nbsp;all&nbsp;times&nbsp;both&nbsp;on&nbsp;and&nbsp;off&nbsp;the&nbsp;job.</li>
            <li>Performs&nbsp;other&nbsp;functions&nbsp;as&nbsp;required&nbsp;by&nbsp;Immediate&nbsp;Head.</li>
            </ol>
            <p><strong>PERFORMANCE&nbsp;EXPECTATIONS/OPPORTUNITIES/LIMITATIONS</strong></p>
            <p><strong>KNOWLEDGE,&nbsp;SKILLS&nbsp;AND&nbsp;ABILITIES</strong></p>
            <ol style="list-style-type: lower-alpha;">
            <li><strong>&nbsp;</strong></li>
            </ol>
            <p><strong>MINIMUM&nbsp;JOB&nbsp;REQUIREMENTS</strong></p>
            <p>Gender &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :&nbsp;</p>
            <p>Height &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :&nbsp;</p>
            <p>Educational&nbsp;Requirement&nbsp; :&nbsp;</p>
            <p>Work&nbsp;Experience &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :&nbsp;</p>
            <p><strong>WORKING&nbsp;CONDITIONS</strong></p>
            <p>&nbsp;</p>'''
    return temp