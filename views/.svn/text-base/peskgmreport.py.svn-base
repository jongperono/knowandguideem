from apps.intent.pes.knowandguideem.models.peskgmrpb import PesKgmRpb
import csv
from apps.intent.pes.base.helpers.pes_session import get_person_id
#from apps.intent.pes.knowandguideem.views.rpb import date_to_str
from django.http.response import HttpResponse, HttpResponseRedirect
from apps.intent.pes.security.decorator import access
from apps.intent.pes.knowandguideem.models.peskgmto import PesKgmTo
from apps.intent.pes.knowandguideem.models.peskgmpositionclassification import PesKgmPositionClassification
from apps.intent.pes.knowandguideem.models.peskgmhierarchy import PesKgmHierarchy
from django.shortcuts import render_to_response
from django.template.context import RequestContext
#from apps.intent.upload.forms.uploadform import AvatarForm
from apps.intent.pes.security.models.logs import PesSecGenericLog
import datetime
from django.core.urlresolvers import reverse

@access.has_access('kg-rp-up',3)
def report(request):
    val = {}
    val['title'] = 'PES - Planning & Development - Update Code/Description'
    val['feature'] = 'kgm_report'
    val['tabgroup'] = 'report'
    val['urlargs'] = {}
    person_id = get_person_id(request)
    lists = []
    try:
        if request.method == 'POST':
            rtype = int(request.POST['category'])
            if rtype == 1:
                lists = PesKgmTo.objects.filter(deleted=0)
                shct = 'T.O.'
            elif rtype == 2:
                lists = PesKgmPositionClassification.objects.filter(deleted=0)
                shct = 'POSITION'
            elif rtype == 3:
                lists = PesKgmRpb.objects.filter(deleted=0)
                shct = 'RPB'
            elif rtype == 4:
                lists = PesKgmHierarchy.objects.filter(deleted=0)
                shct = 'STRUCTURE'
            
            if int(request.POST['type']) == 2:
                upload = request.FILES['file']
                files =  upload.read()
                #print files
                for u in files.split('\r\n'):
                    if ',' in files:
                        row = u.split(',')
                    elif ';' in files:
                        row = u.split(';')
                    if not row:
                        return HttpResponse('No updated code/description.')
                    if row:
                        if row[0] != '':
                            #--Update Code
                            try:
                                if row[3].strip() != '':
                                    if rtype == 1:
                                        ls = PesKgmTo.objects.get(id=int(row[0]))
                                        tble = 'pes_kgm_to'
                                    elif rtype == 2:
                                        ls = PesKgmPositionClassification.objects.get(id=int(row[0]))
                                        tble = 'pes_kgm_position_classification'
                                    elif rtype == 3:
                                        ls = PesKgmRpb.objects.get(id=int(row[0]))
                                        tble = 'pes_kgm_rpb'
                                    elif rtype == 4:
                                        ls = PesKgmHierarchy.objects.get(id=int(row[0]))
                                        
                                        tble = 'pes_kgm_hierarchy'
                                    if rtype == 4:
                                        if ls.numcode == row[3]:
                                            continue
                                    else:
                                        if ls.code == row[3]:
                                            continue
                                    logs = PesSecGenericLog()
                                    logs.person_id = person_id
                                    if rtype == 4:
                                        logs.old_desc = ls.numcode
                                    else:
                                        logs.old_desc = ls.code
                                    logs.new_desc = row[3]
                                    logs.table = tble
                                    logs.table_id = ls.id
                                    logs.remarks = 'Updated Code'
                                    logs.datetime = datetime.datetime.now()
                                    logs.save()
                                    if rtype == 4:
                                        ls.numcode = str(row[3]).replace('"', '')
                                    else:
                                        ls.code = str(row[3]).replace('"', '')
                                    ls.save()
                            except:
                                pass
                            #--Update Description
                            try:
                                if row[4].strip() != '':
                                    if rtype == 1:
                                        ls = PesKgmTo.objects.get(id=int(row[0]))
                                        tble = 'pes_kgm_to'
                                    elif rtype == 2:
                                        ls = PesKgmPositionClassification.objects.get(id=int(row[0]))
                                        tble = 'pes_kgm_position_classification'
                                    elif rtype == 3:
                                        ls = PesKgmRpb.objects.get(id=int(row[0]))
                                        tble = 'pes_kgm_rpb'
                                    elif rtype == 4:
                                        ls = PesKgmHierarchy.objects.get(id=int(row[0]))
                                        tble = 'pes_kgm_hierarchy'
                                    if ls.description == row[4]:
                                        continue
                                    logs = PesSecGenericLog()
                                    logs.person_id = person_id
                                    logs.old_desc = ls.description
                                    logs.new_desc = row[4]
                                    logs.table = tble
                                    logs.table_id = ls.id
                                    logs.remarks = 'Updated Description'
                                    logs.datetime = datetime.datetime.now()
                                    logs.save()
                                    ls.description = str(row[4]).replace('"', '')
                                    ls.save()
                            except:
                                pass
                        #print row
                        #print '======================'
                        #print row[0],' = ',row[1]
                    #for row in u.split(';'):
                    #    print row
                    #PesSecGenericLog()
                return HttpResponseRedirect(reverse('kgm_report_generic'))
                #return HttpResponse('Yeah!')
            else:
                pass
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="'+ shct +'_UpdateReport.csv"'
            writer = csv.writer(response)
            row = 0
            
            
            
            if lists:
                #sheet.col(0).width = 30 * 256
                #sheet.col(1).width = 50 * 256
                #sheet.col(2).width = 30 * 256
                #sheet.col(3).width = 50 * 256
                writer.writerow(['ID',shct +' - CODE',shct +' - DESCRIPTION','NEW CODE','NEW DESCRIPTION'])
                for l in lists:
                    #print l.id
                    row += 1
                    if rtype == 4:
                        writer.writerow([l.id, l.numcode,l.description])
                    else:
                        writer.writerow([l.id, l.code,l.description])
            #--Download--
            return response
        else:
            return render_to_response('kgm_report/genericreport.html',{'page':val},context_instance=RequestContext(request))
    except Exception as error:
        return render_to_response('kgm_report/genericreport.html',{'page':val,'error':error,'display_error':1},context_instance=RequestContext(request))
    
    