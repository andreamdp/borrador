from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from forms import *
from django.template import RequestContext
from django.shortcuts import render
from views import * 
from reportlab.pdfgen  import canvas
from cStringIO import StringIO
from django.template.loader import render_to_string 
import ho.pisa as pisa
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse

def generar_pdf(html):

    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def libro_pdf(request, residenciaaut_id):
   
    residencia = get_object_or_404(ResidenciaAut, pk=residenciaaut_id)

   # residencia=get_object_or_404(Libro, residenciaaut_id=id)
    html = render_to_string('fichaResidencia.html', {'pagesize':'A4', 'residencia':residencia}, context_instance=RequestContext(request))
    return generar_pdf(html)
    

def vfichaResidencia(request, residenciaaut_id):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = ResidenciaAut.objects.filter(pk=residenciaaut_id) 
   # report = MyReport(queryset=objects_list)
    return render_to_response('fichaResidencia.html',
                              {'residenciaaut_id': residenciaaut_id},
                              context_instance=RequestContext(request))   

   # report.generate_by(PDFGenerator, filename=response)

    #return response
    
    
    
   
    
