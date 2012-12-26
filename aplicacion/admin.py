# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import Especialidad, Institucion, Localidad, ResidenciaAut, Profesional
from views import *
from parametricas.models import Tipo
from forms import *
from django.views.generic.simple import direct_to_template
from django.forms import TextInput, Textarea
from parametricas.models import Tipo
from django.contrib.contenttypes import generic



class InstitucionAdmin(admin.ModelAdmin):
        list_display = ['id','nombre', 'localidad','director','secretaria','telefonos','OtrosContactos']

class EspecialidadAdmin(admin.ModelAdmin):
        list_display = ['id','nombre','cantidad_A','tipo']

class LocalidadAdmin(admin.ModelAdmin):
        list_display = ['id','nombre']
        
class ResidenciaAdmin(admin.ModelAdmin):

  list_display = ['id', 'a_Comienzo','institucion','jefeServicio','coordinador','asesorDocente'] 
  fieldsets = (
        (None,{
            'fields':(('a_Comienzo'),('especialidad','institucion'))}),    
        ('Cantidad Residentes', {
	        'classes' : ('collapse closed',),            
                'classes' : ('grp-collapse grp-open',),
                'fields':(('cantA_1','cantA_2','cantA_3'),('cantA_4','jefeResidentes'),())}),
        ('Profesionales', { 
            'classes' : ('collapse closed',),
            'classes' : ('grp-collapse grp-open',),
            'fields':(('jefeServicio'),('coordinador'),('asesorDocente'),)
            }),
        ('Evaluaciones', { 
            'classes' : ('collapse closed',),
            'classes' : ('grp-collapse grp-open',),
            'fields':(('fechaEvaluacColMed','tipo'),('fechaEvaluacMixta'),('fechaCeseActividad'),)
            }),
        
	        )



admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(ResidenciaAut, ResidenciaAdmin)
#admin.site.register(Profesional)


