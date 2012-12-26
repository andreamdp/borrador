# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Profesional'
        db.create_table('aplicacion_profesional', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('residencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aplicacion.ResidenciaAut'])),
        ))
        db.send_create_signal('aplicacion', ['Profesional'])

        # Adding model 'Cliente'
        db.create_table('aplicacion_cliente', (
            ('codigo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('aplicacion', ['Cliente'])

        # Adding model 'FormHelper'
        db.create_table('aplicacion_formhelper', (
            ('codigo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aplicacion.Cliente'])),
        ))
        db.send_create_signal('aplicacion', ['FormHelper'])

        # Adding model 'Direccion'
        db.create_table('aplicacion_direccion', (
            ('calle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aplicacion.Cliente'])),
            ('codigo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('aplicacion', ['Direccion'])

        # Adding model 'Especialidad'
        db.create_table('aplicacion_especialidad', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('codigo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('cantidad_A', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('aplicacion', ['Especialidad'])

        # Adding model 'Institucion'
        db.create_table('aplicacion_institucion', (
            ('OtrosContactos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('telefonos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('secretaria', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aplicacion.Localidad'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('aplicacion', ['Institucion'])

        # Adding model 'Localidad'
        db.create_table('aplicacion_localidad', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('aplicacion', ['Localidad'])

        # Adding model 'ResidenciaAut'
        db.create_table('aplicacion_residenciaaut', (
            ('coordinador', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('jefeServicio', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('fechaEvaluacColMed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fechaCeseActividad', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('especialidad', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['aplicacion.Especialidad'])),
            ('institucion', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['aplicacion.Institucion'])),
            ('cantA_4', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('jefeResidentes', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('cantA_1', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('asesorDocente', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('cantA_3', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('cantA_2', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('fechaEvaluacMixta', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('a_Comienzo', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('aplicacion', ['ResidenciaAut'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Profesional'
        db.delete_table('aplicacion_profesional')

        # Deleting model 'Cliente'
        db.delete_table('aplicacion_cliente')

        # Deleting model 'FormHelper'
        db.delete_table('aplicacion_formhelper')

        # Deleting model 'Direccion'
        db.delete_table('aplicacion_direccion')

        # Deleting model 'Especialidad'
        db.delete_table('aplicacion_especialidad')

        # Deleting model 'Institucion'
        db.delete_table('aplicacion_institucion')

        # Deleting model 'Localidad'
        db.delete_table('aplicacion_localidad')

        # Deleting model 'ResidenciaAut'
        db.delete_table('aplicacion_residenciaaut')
    
    
    models = {
        'aplicacion.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'codigo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aplicacion.direccion': {
            'Meta': {'object_name': 'Direccion'},
            'calle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aplicacion.Cliente']"}),
            'codigo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aplicacion.especialidad': {
            'Meta': {'object_name': 'Especialidad'},
            'cantidad_A': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'codigo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'aplicacion.formhelper': {
            'Meta': {'object_name': 'FormHelper'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aplicacion.Cliente']"}),
            'codigo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aplicacion.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'OtrosContactos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aplicacion.Localidad']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'secretaria': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aplicacion.localidad': {
            'Meta': {'object_name': 'Localidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aplicacion.profesional': {
            'Meta': {'object_name': 'Profesional'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'residencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aplicacion.ResidenciaAut']"})
        },
        'aplicacion.residenciaaut': {
            'Meta': {'object_name': 'ResidenciaAut'},
            'a_Comienzo': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'asesorDocente': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'cantA_1': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'cantA_2': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'cantA_3': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'cantA_4': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'coordinador': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'especialidad': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['aplicacion.Especialidad']"}),
            'fechaCeseActividad': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fechaEvaluacColMed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fechaEvaluacMixta': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['aplicacion.Institucion']"}),
            'jefeResidentes': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'jefeServicio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'})
        }
    }
    
    complete_apps = ['aplicacion']
