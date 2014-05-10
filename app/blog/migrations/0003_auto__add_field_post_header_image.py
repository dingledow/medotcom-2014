# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.header_image'
        db.add_column(u'blog_post', 'header_image',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.header_image'
        db.delete_column(u'blog_post', 'header_image')


    models = {
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'excerpt': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'header_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']