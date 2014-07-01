def residente1_edit(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm1(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/'+residenciaaut_id+'/lista/')

    return render_to_response('aplicacion/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request)) 
                              
def residente2_edit(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm2(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/'+residenciaaut_id+'/lista/')

    return render_to_response('aplicacion/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))
                              
def residente3_edit(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm3(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/'+residenciaaut_id+'/lista/')

    return render_to_response('aplicacion/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))   
                              
def residente4_edit(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm1(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/'+residenciaaut_id+'/lista/')

    return render_to_response('aplicacion/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))  
                              
def jefeResidente_edit(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm1(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/'+residenciaaut_id+'/lista/')

    return render_to_response('aplicacion/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))                                                                                                                      
    
