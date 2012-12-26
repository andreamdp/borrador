# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Tipo'
        db.create_table('parametricas_tipo', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('parametricas', ['Tipo'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Tipo'
        db.delete_table('parametricas_tipo')
    
    
    models = {
        'parametricas.tipo': {
            'Meta': {'object_name': 'Tipo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }
    
    complete_apps = ['parametricas']
