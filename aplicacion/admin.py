# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import Especialidad, Institucion, Localidad, ResidenciaAut, Profesional
from views import *
from parametricas.models import Tipo
from forms import *

from django.forms import TextInput, Textarea
from parametricas.models import Tipo
from django.contrib.contenttypes import generic
import copy  # (1) use python copy
def copiar_residencia(modeladmin, request, queryset):
    # sd is an instance of resiencias
    for sd in queryset:
        sd_copy = copy.copy(sd) # (2) django copy object
        sd_copy.id = None   # (3) set 'id' to None to create new object
        sd_copy.save()    # initial save
    sd_copy.save()  # (7) save the copy to the database for M2M 
    
copiar_residencia.short_description = 'Copiar Residencias seleccionadas'

from django import forms

class ResidenciaForm(forms.ModelForm):
    exp = forms.CharField(initial="",max_length=12, min_length=12,
    widget=forms.TextInput(attrs={'placeholder':'0000-0000/00'}))

    class Meta:
        model = ResidenciaAut

def actualiza_a(self, request, queryset):
        rows_updated =  queryset.update(a_Comienzo='2013')
        if rows_updated == 1:
            message_bit = "1 residencia fue correctamente actualizada"
        else:
            message_bit = "%s residencias fueron correctamente actualizadas" % rows_updated
        self.message_user(request, "%s ." % message_bit)
actualiza_a.short_description = "Actualizar a Año 2013"

class InstitucionAdmin(admin.ModelAdmin):
        list_display = ['id','nombre', 'localidad','director','secretaria','telefonos','OtrosContactos']

class EspecialidadAdmin(admin.ModelAdmin):
        list_display = ['codigo','nombre','cantidad_A','tipo']

class LocalidadAdmin(admin.ModelAdmin):
        list_display = ['id','nombre']
        
class ResidenciaAdmin(admin.ModelAdmin):
  change_form_template = 'admin/aplicacion/residenciaaut/change_form.html'
  add_form_template = 'admin/change_form.html'
  actions = [copiar_residencia, actualiza_a]  
 # form = ResidenciaForm
  def getID(self,obj):
        if obj.id is None:
          return ''
        else:
	  return obj.id
  getID.short_description = 'Número Interno'
  readonly_fields = ("getID",) 
  list_display = ['id', 'a_Comienzo','institucion','especialidad','fechaEvaluacColMed','fechaCeseActividad'] 
  fieldsets = (
        (None,{
            'fields':(('getID','expediente','a_Comienzo'),('especialidad','institucion'))}),    
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
            'fields':(('fechaEvaluacColMed','tipo'),('fechaCeseActividad'),)
            }),
        ('Conclusiones y Recomendaciones', { 
            'classes' : ('grp-collapse grp-open',),
            'fields':(('memo'),)
            }),
	        )



admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(ResidenciaAut, ResidenciaAdmin)
admin.site.register(Residente)


