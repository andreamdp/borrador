from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from aplicacion.forms import *
from django import template
register = template.Library()  
@csrf_protect
@register.inclusion_tag('aplicacion/residente/add.html', takes_context=True)
def residente_add1(request, residenciaaut_id,form_class=ResidenteForm1, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
          
            return redirect('residente_list',residenciaaut_id)
            
    else:
       form = ResidenteForm1(initial={'residencia': residenciaaut_id})
      
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))

@csrf_protect
#@register.inclusion_tag('aplicacion/residente/add.html', takes_context=True)
def residente_add2(request, residenciaaut_id,form_class=ResidenteForm2, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm2(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))   
@csrf_protect

def residente_add3(request, residenciaaut_id,form_class=ResidenteForm3, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm3(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))
@csrf_protect

def residente_add4(request, residenciaaut_id,form_class=ResidenteForm4, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm4(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))

@csrf_protect
def jefeResidente_add(request, residenciaaut_id,form_class=JefeResidenteForm, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = JefeResidenteForm(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))   

def residente1_edit(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm1(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
       # residente.save()
        return redirect('lista/')

    return render_to_response('aplicacion/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request)) 
    
def residente1_delete(request, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    residente.delete()
    return redirect('/aplicacion/residente')
