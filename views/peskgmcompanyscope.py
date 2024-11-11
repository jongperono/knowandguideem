from django.http import HttpResponse
from apps.intent.pes.knowandguideem.models.peskgmcompanyscope import PesKgmCompanyscope
from apps.intent.pes.knowandguideem.forms.peskgmsompanyscope import PesKgmCompanyscopeForm

from django.shortcuts import render_to_response,  get_object_or_404, redirect
from django.template import RequestContext    
from apps.intent.pes.knowandguideem.helpers.employeevalidation import isemployee

def index(request):
    val = {}
    val['title'] = 'Company Structure'
    val['feature'] = 'companyscope'
    val['tabgroup'] = 'listgroup'

    company_scope = PesKgmCompanyscope.objects.all().order_by('id')
    return render_to_response('companyscope/list.html',{'list':company_scope,'page' : val},context_instance=RequestContext(request))

def create(request):  
    val = {}
    val['title'] = 'Company Structure'
    val['feature'] = 'companyscope'
    val['tabgroup'] = 'listgroup'
    try:
        if(request.method=='POST'):
            form=PesKgmCompanyscopeForm(request.POST)
            if(form.is_valid()):
                #if request.POST['employee']
                if isemployee(request.POST['employee'])==True:
                    form.save(commit=True)
                    return redirect(index)
                else:
                    return render_to_response('companyscope/form.html',{'form':form, 'create':form,'error':'Not A Valid Employee','page' : val},context_instance=RequestContext(request))

            else:
                return render_to_response('companyscope/form.html',{'form':form, 'create':form,'page' : val},context_instance=RequestContext(request))
        else:
            form=PesKgmCompanyscopeForm()
            return render_to_response('companyscope/form.html',{'form':form, 'create':form,'page' : val},context_instance=RequestContext(request))
    except Exception as error:
        form=PesKgmCompanyscopeForm()
        return render_to_response('companyscope/form.html',{'form':form, 'create':form,'error':error,'page' : val},context_instance=RequestContext(request))


def edit(request,id):
    val = {}
    val['title'] = 'Company Structure'
    val['feature'] = 'companyscope'
    val['tabgroup'] = 'listgroup'
    try:
        if(request.method=='POST'):
            division = get_object_or_404(PesKgmCompanyscope, pk=id)
            form=PesKgmCompanyscopeForm(request.POST,instance=division)
            if(form.is_valid()):
                if isemployee(request.POST['employee'])==True:
                    form.save(commit=True) 
                    return redirect(index)
                else:
                    return render_to_response('companyscope/form.html',{'form':form, 'edit':form,'id':id,'error':'Not A Valid Employee','page' : val},context_instance=RequestContext(request))
            else:
                return render_to_response('companyscope/form.html',{'form':form, 'edit':form,'id':id,'page' : val},context_instance=RequestContext(request))       
        else:        
            division = get_object_or_404(PesKgmCompanyscope, pk=id)
            form = PesKgmCompanyscopeForm(instance=division)  
            return render_to_response('companyscope/form.html',{'form':form, 'edit':form,'id':id,'page' : val},context_instance=RequestContext(request))
        
    except Exception as error: 
        division = get_object_or_404(PesKgmCompanyscope, pk=id)
        form=PesKgmCompanyscopeForm(instance=division)
        return render_to_response('companyscope/form.html',{'form':form, 'edit':form,'id':id,'error':error,'page' : val},context_instance=RequestContext(request))

def delete(request,id):
    try:
        companyscope = get_object_or_404(PesKgmCompanyscope, pk=id)
        companyscope.delete()
        return redirect(index)
    except Exception as error:
        company_scope = PesKgmCompanyscope.objects.all().order_by('id')
        return render_to_response('companyscope/list.html',{'list':company_scope,'error':error},context_instance=RequestContext(request))
    
         
    

