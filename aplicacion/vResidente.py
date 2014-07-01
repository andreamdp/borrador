from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from aplicacion.forms import *
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

register = template.Library()  


def residente_list(request,residenciaaut_id,template_name='aplicacion/residente/list.html' ):
    residentes_list = Residente.active.filter(residencia_id=residenciaaut_id).order_by('tipoR')
    paginator = Paginator(residentes_list,  6)
    page = request.GET.get('page')
    try:
        residentes = paginator.page(page)
    except PageNotAnInteger:
        residentes = paginator.page(1)
    except EmptyPage:
        residentes = paginator.page(paginator.num_pages)
    return render_to_response(template_name, {
        'residentes': residentes,
        'idR:': Residente.residencia,
      #  'paginator': paginator,
      #  'page': page,
    })
    
def residente_delete(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    residente.delete()
    return redirect('/'+residenciaaut_id+'/lista/')

@csrf_protect
@register.inclusion_tag('aplicacion/residente/add.html', takes_context=True)
def residente1_add(request, residenciaaut_id,form_class=ResidenteForm1, template_name='aplicacion/residente/add.html'):
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
def residente2_add(request, residenciaaut_id,form_class=ResidenteForm2, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm2(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))   
@csrf_protect

def residente3_add(request, residenciaaut_id,form_class=ResidenteForm3, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm3(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))
@csrf_protect

def residente4_add(request, residenciaaut_id,form_class=ResidenteForm4, template_name='aplicacion/residente/add.html'):
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


