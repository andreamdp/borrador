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
class ResidenciaInline(generic.GenericTabularInline):
    model = ResidenciaAut
class ResidenciaAutInline(admin.TabularInline):
    model = ResidenciaAut
    formfield_overrides = {
	models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':50})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'8'})},
    }
    
    extra = 1
    max_num = 1
class ResidenciaAdmin(admin.ModelAdmin):
  fieldsets = (
        (None,{
            'fields':(('a_Comienzo'),('especialidad','institucion'))}),    
        ('Cantidad Residentes', {
	        'classes' : ('collapse closed',),            
                'classes' : ('grp-collapse grp-open',),
                'fields':(('cantA_1','cantA_2'),('cantA_3','cantA_4','jefeResidentes'),)}),
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
  #inlines = [ResidenciaAutInline]
  #inlines = [        ResidenciaInline,    ]


admin.site.register(Especialidad)
admin.site.register(Institucion)
admin.site.register(Localidad)
admin.site.register(ResidenciaAut, ResidenciaAdmin)
#admin.site.register(Profesional)


