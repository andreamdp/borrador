#encoding= utf-8
from django.http import HttpResponse
from django.views.generic import ListView
from aplicacion.models import *
from django.forms.models import inlineformset_factory
from reportlab.lib.colors import navy, yellow, red, black, blue
from django.http import HttpResponse
from geraldo import Report, DetailBand, ObjectValue
from geraldo.generators import PDFGenerator
from Colegio.geraldo.utils import cm
from django.contrib.auth.models import User

from django.core.exceptions import PermissionDenied
from reportlab.lib.pagesizes import legal

def edit(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied

class MyReport(UsersReport):
    title = 'Listado de Residencias'
    page_size = landscape(legal)
    class band_page_header(ReportBand):
        height = 2.7*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
            Label(text="Año_Comienzo", top=2*cm, left=0),
            Label(text="Especialidad", top=2*cm, left=3*cm),
            Label(text="Coordinador", top=2*cm, left=6*cm),
            Label(text="Institucion", top=2*cm, left=10*cm),
            Label(text="Jefe de Residentes", top=2*cm, left=14*cm),
            Label(text="Asesor Docente", top=2*cm, left=18*cm),
            Label(text="Jefe de Servicio", top=2*cm, left=22*cm),
            Label(text="Año 1", top=2*cm, left=26*cm),
            Label(text="Año 2", top=2*cm, left=28*cm),
            Label(text="Año 3", top=2*cm, left=30*cm),
            Label(text="Año 4", top=2*cm, left=32*cm),
            
                    ]
        borders = {'bottom': Line(stroke_color=black, stroke_width=1)}
    class band_detail(DetailBand):
        height=0.7*cm
        elements=[
            ObjectValue(attribute_name='a_Comienzo', top=0.1*cm, left=0),
            ObjectValue(attribute_name='especialidad', top=0.1*cm, left=3.10*cm),
            ObjectValue(attribute_name='coordinador', top=0.1*cm, left=6.10*cm),
            ObjectValue(attribute_name='institucion', top=0.1*cm, left=10.10*cm),
            ObjectValue(attribute_name='jefeResidentes', top=0.1*cm, left=14.10*cm),
            ObjectValue(attribute_name='asesorDocente', top=0.1*cm, left=18.10*cm),
            ObjectValue(attribute_name='jefeServicio', top=0.1*cm, left=22.10*cm),
            ObjectValue(attribute_name='cantA_1', top=0.1*cm, left=26.18*cm),
            ObjectValue(attribute_name='cantA_2', top=0.1*cm, left=28.18*cm),
            ObjectValue(attribute_name='cantA_3', top=0.1*cm, left=30.18*cm),
            ObjectValue(attribute_name='cantA_4', top=0.1*cm, left=32.18*cm),
            
            
            ]

def my_view(request):
    response = HttpResponse(mimetype='application/pdf')


    objects_list = ResidenciaAut.objects.all() # If you are using Django
    report = MyReport(queryset=objects_list)
    
    report.generate_by(PDFGenerator, filename=response)

    return response



