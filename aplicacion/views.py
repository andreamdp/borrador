#encoding= utf-8
from django.http import HttpResponse
from django.views.generic import ListView
from aplicacion.models import *
from django.forms.models import inlineformset_factory
from reportlab.lib.colors import navy, yellow, red, black, blue, purple, green, darkgreen
from django.http import HttpResponse
from geraldo import Report, DetailBand, ObjectValue
from geraldo.generators import PDFGenerator
from Colegio.geraldo.utils import cm
from django.contrib.auth.models import User
from aplicacion.admin import *
from django.core.exceptions import PermissionDenied
from reportlab.lib.pagesizes import legal, A5

def edit(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied


class MyReport(UsersReport):
    title = 'Listado de Residencias'
    page_size = landscape(legal)
    
    
    class band_summary(ReportBand):
        def totalGral(self):
          total=0
          for p in queryset:
               total=total+ self.sumaCantA()
          return total
    
        height = 0.5*cm
        elements = [
            Label(text='Total general:', style={ 'fontSize': 11, 'textColor': navy, 'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cantA_1', top=0.1*cm, left=27.5*cm,\
                action=FIELD_ACTION_SUM, display_format='%s', style={'fontSize': 11, 'textColor': navy, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='cantA_2', top=0.1*cm, left=29*cm,\
                action=FIELD_ACTION_SUM, display_format='%s', style={'fontSize': 11, 'textColor': navy, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='cantA_1', top=0.1*cm, left=30.15*cm,\
                action=FIELD_ACTION_SUM, display_format='%s', style={'fontSize': 11, 'textColor': navy, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='cantA_1', top=0.1*cm, left=31.3*cm,\
                action=FIELD_ACTION_SUM, display_format='%s', style={'fontSize': 11, 'textColor': navy, 'fontName': 'Helvetica-Bold',}),
            ObjectValue(attribute_name='sumaCantA', top=0.1*cm, left=32.6*cm,\
                action=FIELD_ACTION_SUM, display_format='%s', style={'fontSize': 11, 'textColor': navy, 'fontName': 'Helvetica-Bold',}),
            #ObjectValue(expression='totalGral', left=6.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ]
        borders = {'top': True}
        
    class band_page_header(ReportBand):
        height = 3*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
            Label(text="Año de", top=2*cm, left=0, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold',}),
            Label(text="Comienzo", top=2.4*cm, left=0, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Especialidad", top=2*cm, left=2.4*cm, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Coordinador", top=2*cm, left=6.8*cm, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Institución", top=2*cm, left=12*cm, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Jefe Servicio", top=2*cm, left=16.8*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Asesor Docente", top=2*cm, left=21.2*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Jefe de", top=2*cm, left=25.2*cm, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Residentes", top=2.4*cm, left=25.2*cm, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Año", top=2*cm, left=27.2*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="1", top=2.4*cm, left=27.6*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Año",top=2*cm, left=28.7*cm, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="2",top=2.4*cm, left=29.1*cm, style={'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Año",top=2*cm, left=29.95*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="3",top=2.4*cm, left=30.35*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Año",top=2*cm, left=31*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="4",top=2.4*cm, left=31.4*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Total",top=2*cm, left=32*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Alumnos",top=2.4*cm, left=32*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
                    ]
        borders = {'bottom': Line(stroke_color=red, stroke_width=1)}
    class band_detail(DetailBand):
        height = 1.9*cm
        elements=[
          
            ObjectValue(attribute_name='a_Comienzo', top=0.2*cm, left=0.1, height=5*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='especialidad', top=0.2*cm, left=2*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='coordinador', top=0.2*cm, left=6.5*cm, width=4.5*cm, style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='institucion', top=0.2*cm, left=11*cm, width=5*cm, style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='jefeServicio', top=0.2*cm, left=16.5*cm, width=4*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='asesorDocente', top=0.2*cm, left=21*cm, width=4*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='jefeResidentes', top=0.2*cm, left=25.6*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='cantA_1', top=0.2*cm, left=27.5*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='cantA_2', top=0.2*cm, left=29*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='cantA_3', top=0.2*cm, left=30.15*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='cantA_4', top=0.2*cm, left=31.3*cm, width=5*cm,style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='sumaCantA', top=0.2*cm, left=32.6*cm, width=5*cm,style={'fontName': 'Helvetica-Bold', 'fontSize': 10.5}),
         
            ]

def residencias2012(request):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = ResidenciaAut.objects.filter(a_Comienzo=2012).order_by('a_Comienzo','institucion') 
    report = MyReport(queryset=objects_list)
    
    report.generate_by(PDFGenerator, filename=response)

    return response
def residencias2013(request):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = ResidenciaAut.objects.filter(a_Comienzo=2013).order_by('a_Comienzo','institucion') 
    report = MyReport(queryset=objects_list)
    
    report.generate_by(PDFGenerator, filename=response)

    return response
class r_AEval(UsersReport):
    title = 'Listado de Residencias por Año de Evaluación'
    page_size = landscape(legal)
    class band_page_header(ReportBand):
        height = 3*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
            Label(text="Año de", top=2*cm, left=0, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Comienzo", top=2.4*cm, left=0, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Especialidad", top=2*cm, left=4*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Institucion", top=2*cm, left=18*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Fecha de ", top=2*cm, left=30.8*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Evaluación", top=2.4*cm, left=30.8*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            
                    ]
        borders = {'bottom': Line(stroke_color=red, stroke_width=1)}
    
    class band_detail(DetailBand):
        
        height=0.7*cm
        elements=[
          
            ObjectValue(attribute_name='a_Comienzo', top=0.2*cm, left=0.001, height=5*cm),
            ObjectValue(attribute_name='especialidad', top=0.2*cm, left=4*cm, width=8*cm),
            ObjectValue(attribute_name='institucion', top=0.2*cm, left=18.2*cm, width=8*cm),
            ObjectValue(attribute_name='fechaEvalNoNula', top=0.2*cm, left=31*cm),
            
          
            ]

def aEvaluacion(request):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = ResidenciaAut.objects.all() # If you are using Django
    report = r_AEval(queryset=objects_list)
    
    report.generate_by(PDFGenerator, filename=response)

    return response

