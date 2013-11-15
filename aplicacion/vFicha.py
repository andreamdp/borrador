#encoding= utf-8
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
class ReporteFicha(UsersReport):
    title = 'Ficha de Residencia'
    page_size = landscape(legal)
    class band_page_header(ReportBand):
        height = 1.5*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
	        Label(text="Cantidad de Residentes", top=4*cm, left=0, width=100*cm, style={'fontSize': 14, 'backColor':lightblue,'textColor': black, 'fontName': 'Helvetica-Bold',}),
	        Label(text="Profesionales", top=7*cm, left=0, width=100*cm, style={'fontSize': 14, 'backColor':lightblue,'textColor': black, 'fontName': 'Helvetica-Bold',}),
	        Label(text="Evaluaciones", top=11*cm, left=0, width=100*cm, style={'fontSize': 14, 'backColor':lightblue,'textColor': black, 'fontName': 'Helvetica-Bold',}),
	        Label(text="Conclusiones y Recomendaciones", top=15*cm, left=0, width=100*cm, style={'fontSize': 14, 'backColor':lightblue,'textColor': black, 'fontName': 'Helvetica-Bold',}),
          ]
    class band_detail(DetailBand):
        height = 1.9*cm
        elements=[
            Label(text="N° Interno:", top=0.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='id', top=0.5*cm, left=140, height=5*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
            
            Label(text="N° de Expediente del Ministerio de Salud:", top=0.5*cm, width=13*cm, left=370, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='expediente', top=0.5*cm, left=630, height=5*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
            
            Label(text="Año:", top=0.5*cm, width=14.5*cm, left=750, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='a_Comienzo', top=0.5*cm, left=790, height=5*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
           
            Label(text="Especialidad:", top=1.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='especialidad', top=1.5*cm, left=130, height=5*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
            
            Label(text="Institución:", top=1.5*cm, left=370, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='institucion', top=1.5*cm, left=450, height=5*cm, width=140*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
           #----------------------------------------------------------------------------
            Label(text="1° Año:", top=3.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            Label(text="2° Año:", top=3.5*cm, left=370, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            Label(text="3° Año:", top=4.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            Label(text="4° Año:", top=4.5*cm, left=370, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            
            ObjectValue(attribute_name='cantA_1', top=3.5*cm, left=90, height=5*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
            ObjectValue(attribute_name='cantA_2', top=3.5*cm, left=420, height=4*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
            ObjectValue(attribute_name='cantA_2', top=4.5*cm, left=90, width=400*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
            ObjectValue(attribute_name='cantA_1', top=4.5*cm, left=420, width=400*cm, style={'fontName': 'Helvetica', 'fontSize': 12}),
            
            
            Label(text="Jefe de Residentes:", top=4.5*cm, left=750, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='jefeResidentes', top=4.5*cm, left=880, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 12}),
            #--------------------------------------------------------------------
            Label(text="Jefe de Servicio:", top=6.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='jefeServicio', top=6.5*cm, left=160, width=400*cm,style={'fontName': 'Helvetica', 'fontSize': 12}),
            
            Label(text="Coordinador:", top=7.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='coordinador', top=7.5*cm, left=160, width=140*cm,style={'fontName': 'Helvetica', 'fontSize': 12}),
            
            Label(text="Asesor Docente:", top=8.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='asesorDocente', top=8.5*cm, left=160, width=140*cm,style={'fontName': 'Helvetica', 'fontSize': 12}),
            #-------------------------------------------------------------------------------------
            Label(text="Fecha de Evaluación:", top=10.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='fechaEvalNoNula', top=10.5*cm, left=180, width=140*cm,style={'fontName': 'Helvetica', 'fontSize': 12}),
            
            Label(text="Tipo:", top=10.5*cm, left=370, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='nombreTipo', top=10.5*cm, left=450, width=140,style={'fontName': 'Helvetica', 'fontSize': 12}),
            
            Label(text="Fecha de Vencimiento Acreditación:", top=11.5*cm,  width=540*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='fechaCeseActividadNoNula', top=11.5*cm, left=270, width=140*cm,style={'fontName': 'Helvetica', 'fontSize': 12}),
            #-------------------------------------------------------------------------------
            Label(text="Memo:", top=14.5*cm, left=40, style={'fontSize': 13, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='memo', top=14.5*cm, left=140, width=140*cm,style={'fontName': 'Helvetica', 'fontSize': 12}),
        
          #  ObjectValue(attribute_name='', top=0.2*cm, left=27.5*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
           # ObjectValue(attribute_name='', top=0.2*cm, left=29*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
            #ObjectValue(attribute_name='', top=0.2*cm, left=30.15*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
           # ObjectValue(attribute_name='', top=0.2*cm, left=31.3*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
          #  ObjectValue(attribute_name='sumaCantA', top=0.2*cm, left=32.6*cm, width=5*cm,style={'fontName': 'Helvetica-Bold', 'fontSize': 10.5}),
         
            ]

def reporteFicha(request, residenciaaut_id):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = ResidenciaAut.objects.filter(id=residenciaaut_id) 
    report = ReporteFicha(queryset=objects_list)
    
    report.generate_by(PDFGenerator, filename=response)

    return response   
   
    
    
    
   
    
