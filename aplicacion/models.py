import os, sys
#encoding= utf-8
from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.db.models.fields import PositiveSmallIntegerField
from django.db.models.fields import DateField
from parametricas.models import Tipo
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Profesional(models.Model):
   
    nombre = models.CharField(max_length = 50)
    residencia = models.ForeignKey('ResidenciaAut')
    class Meta:
	verbose_name = "Profesional"
	verbose_name_plural = "Profesionales"

    def __unicode__(self):
        return self.nombre
    
class Cliente(models.Model):
    codigo = PositiveIntegerField()

class FormHelper(models.Model):
    codigo = PositiveIntegerField()
    cliente = models.ForeignKey(Cliente)
class Direccion(models.Model):
    codigo = PositiveIntegerField()
    calle = models.ForeignKey(Cliente)
class Especialidad(models.Model):
    codigo = PositiveIntegerField()
    nombre = models.CharField(max_length=50)
    cantidad_A = PositiveIntegerField('cantidad de Años')
    tipo = PositiveSmallIntegerField()
    class Meta:
	verbose_name = "Especialidad"
	verbose_name_plural = "Especialidades"

    def __unicode__(self):
        return self.nombre
    
class Institucion(models.Model):
   
    nombre = models.CharField(max_length=50)
    localidad = models.ForeignKey('Localidad')
    director = models.CharField(max_length=50)
    secretaria = models.CharField(max_length=50)
    telefonos = models.CharField(max_length=50)
    OtrosContactos = models.TextField('Otros Contactos', blank = True)
    class Meta:
	verbose_name = "Institución"
	verbose_name_plural = "Instituciones"

    def __unicode__(self):
        return self.nombre
class Localidad(models.Model):
    
    nombre = models.CharField(max_length=50)
    
    class Meta:
	verbose_name = "Localidad"        
	verbose_name_plural = "Localidades"

    def __unicode__(self):
        return self.nombre
    
class ResidenciaAut(models.Model):
    tipo_choice = (
        ('C', 'Colegio'),
        ('M', 'Mixta'),
        
    )
   # content_type = models.ForeignKey(ContentType)
   # object_id = models.PositiveIntegerField()
   # content_object = generic.GenericForeignKey("content_type", "object_id")
    a_Comienzo =  PositiveSmallIntegerField('Año')
    especialidad = models.ForeignKey(Especialidad, related_name='+', null = True, blank = True)
    institucion =  models.ForeignKey('Institucion', related_name='+', null =  True, blank = True)
    cantA_1 = PositiveSmallIntegerField('1er. Año')
    cantA_2 = PositiveSmallIntegerField('2do. Año')
    cantA_3 = PositiveSmallIntegerField('3er. Año')
    cantA_4 = PositiveSmallIntegerField('4to. Año')
    jefeResidentes = PositiveSmallIntegerField('Jefe de Residentes')
    fechaEvaluacColMed = DateField('Fecha de Evaluación en Colegio Médico', blank = True, null = True)
    fechaEvaluacMixta = DateField('Fecha de Evaluación Mixta', blank = True, null = True)
    fechaCeseActividad = DateField('Fecha de cese de evaluación', blank = True, null = True)
    jefeServicio = models.CharField('Jefe de Servicio',max_length=50)
    coordinador = models.CharField('Coordinador',max_length=50)
    asesorDocente = models.CharField('Asesor Docente', max_length=50, blank = True)
    tipo = models.CharField(max_length=2, choices=tipo_choice, blank = True)  
    class Meta:
	verbose_name = "Residencia"        
	verbose_name_plural = "Residencias"

    def __unicode__(self):
        return unicode(self.a_Comienzo)

    
from Colegio.geraldo import Report, DetailBand, ObjectValue
from Colegio.geraldo.utils import cm
from Colegio.geraldo.generators import PDFGenerator

names = ['Mychelle', 'Leticia', 'Tarsila', 'Marta', 'Vera', 'Leni']

class MyReport(Report):
    class band_detail(DetailBand):
        height=0.7*cm
        elements=[
            ObjectValue(attribute_name='capitalize'),
            ]

report = MyReport(queryset=names)
report.generate_by(PDFGenerator, filename='female-names.pdf') 

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

from django.contrib.auth.models import User

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.colors import navy, yellow, red, black, blue, lawngreen
from geraldo import Report, ReportBand, Label, ObjectValue, SystemField,\
    FIELD_ACTION_COUNT, FIELD_ACTION_AVG, FIELD_ACTION_MIN,\
    FIELD_ACTION_MAX, FIELD_ACTION_SUM, FIELD_ACTION_DISTINCT_COUNT, BAND_WIDTH,\
    RoundRect, Line, landscape

from geraldo.base import EmptyQueryset
from reportlab.lib.pagesizes import legal
from reportlab.lib.units import cm
class UsersReport(Report):
    title = 'Listado' 
   # page_size = landscape(legal)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm
    class band_page_header(ReportBand):
       # height = 1.3*cm
        elements = [
           # SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
            #    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0),
            Label(text="name", top=0.8*cm, left=3*cm),
            Label(text="", top=0.8*cm, left=8*cm),
            Label(text="", top=0.8*cm, left=13*cm),
            Label(text="", top=0.8*cm, left=18*cm),
        ]
        borders = {'bottom': Line(stroke_color=navy)}

    class band_page_footer(ReportBand):
        #height = 0.4*cm
        elements = [
            Label(text='Colmed IX - Sistema de Residencias', top=0.1*cm,
                right=0),
            SystemField(expression='%(now:%Y, %b %d)s', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
        ]
        borders = {'top': Line(stroke_color=blue, stroke_width=1)}

    class band_detail(DetailBand):
        #height=0.7*cm
        elements=[
            ObjectValue(attribute_name='capitalize'),
            ]

