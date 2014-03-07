# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'dopomoga_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dopomoga.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('pictures', self.gf('django.db.models.fields.files.ImageField')(default='/static/img/default.jpg', max_length=100, null=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dopomoga', ['Review'])

        # Adding model 'UserInneedProfile'
        db.create_table(u'dopomoga_userinneedprofile', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.UserProfile'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dopomoga', ['UserInneedProfile'])

        # Adding M2M table for field projects_asked on 'UserInneedProfile'
        m2m_table_name = db.shorten_name(u'dopomoga_userinneedprofile_projects_asked')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userinneedprofile', models.ForeignKey(orm[u'dopomoga.userinneedprofile'], null=False)),
            ('projecthelper', models.ForeignKey(orm[u'dopomoga.projecthelper'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userinneedprofile_id', 'projecthelper_id'])

        # Adding model 'ProjectInneedReview'
        db.create_table(u'dopomoga_projectinneedreview', (
            (u'review_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Review'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dopomoga', ['ProjectInneedReview'])

        # Adding model 'ResourceComment'
        db.create_table(u'dopomoga_resourcecomment', (
            (u'comment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Comment'], unique=True, primary_key=True)),
            ('resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dopomoga.Resource'])),
        ))
        db.send_create_signal(u'dopomoga', ['ResourceComment'])

        # Adding model 'UserInneedComment'
        db.create_table(u'dopomoga_userinneedcomment', (
            (u'comment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Comment'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'dopomoga', ['UserInneedComment'])

        # Adding model 'Resource'
        db.create_table(u'dopomoga_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(default='/static/img/default.jpg', max_length=100, blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'dopomoga', ['Resource'])

        # Adding model 'Project'
        db.create_table(u'dopomoga_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('how_to_help', self.gf('django.db.models.fields.CharField')(default='', max_length=2048, null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(default='/static/img/default.jpg', max_length=100, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('res_qnt', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('funded', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_started', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('date_finished', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('reports', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'dopomoga', ['Project'])

        # Adding M2M table for field resource on 'Project'
        m2m_table_name = db.shorten_name(u'dopomoga_project_resource')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'dopomoga.project'], null=False)),
            ('resource', models.ForeignKey(orm[u'dopomoga.resource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'resource_id'])

        # Adding M2M table for field cause on 'Project'
        m2m_table_name = db.shorten_name(u'dopomoga_project_cause')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'dopomoga.project'], null=False)),
            ('cause', models.ForeignKey(orm[u'dopomoga.cause'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'cause_id'])

        # Adding model 'CauseComment'
        db.create_table(u'dopomoga_causecomment', (
            (u'comment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Comment'], unique=True, primary_key=True)),
            ('cause', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dopomoga.Cause'])),
        ))
        db.send_create_signal(u'dopomoga', ['CauseComment'])

        # Adding model 'Comment'
        db.create_table(u'dopomoga_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('date_commented', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('reports', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'dopomoga', ['Comment'])

        # Adding model 'ProjectInneedComment'
        db.create_table(u'dopomoga_projectinneedcomment', (
            (u'comment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Comment'], unique=True, primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dopomoga.Project'])),
        ))
        db.send_create_signal(u'dopomoga', ['ProjectInneedComment'])

        # Adding model 'ProjectHelperReview'
        db.create_table(u'dopomoga_projecthelperreview', (
            (u'review_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Review'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dopomoga', ['ProjectHelperReview'])

        # Adding model 'UserProfileComment'
        db.create_table(u'dopomoga_userprofilecomment', (
            (u'comment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Comment'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'dopomoga', ['UserProfileComment'])

        # Adding model 'ProjectHelper'
        db.create_table(u'dopomoga_projecthelper', (
            (u'project_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Project'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'dopomoga', ['ProjectHelper'])

        # Adding model 'UserProfile'
        db.create_table(u'dopomoga_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(default='/static/img/default.jpg', max_length=100, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('date_joined', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('reports', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'dopomoga', ['UserProfile'])

        # Adding M2M table for field resources on 'UserProfile'
        m2m_table_name = db.shorten_name(u'dopomoga_userprofile_resources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'dopomoga.userprofile'], null=False)),
            ('resource', models.ForeignKey(orm[u'dopomoga.resource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'resource_id'])

        # Adding M2M table for field causes on 'UserProfile'
        m2m_table_name = db.shorten_name(u'dopomoga_userprofile_causes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'dopomoga.userprofile'], null=False)),
            ('cause', models.ForeignKey(orm[u'dopomoga.cause'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'cause_id'])

        # Adding M2M table for field projects_supported on 'UserProfile'
        m2m_table_name = db.shorten_name(u'dopomoga_userprofile_projects_supported')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'dopomoga.userprofile'], null=False)),
            ('projectinneed', models.ForeignKey(orm[u'dopomoga.projectinneed'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'projectinneed_id'])

        # Adding model 'ProjectInneed'
        db.create_table(u'dopomoga_projectinneed', (
            (u'project_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Project'], unique=True, primary_key=True)),
            ('docs_descr', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
            ('docs_pics', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'dopomoga', ['ProjectInneed'])

        # Adding M2M table for field users_inneed on 'ProjectInneed'
        m2m_table_name = db.shorten_name(u'dopomoga_projectinneed_users_inneed')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectinneed', models.ForeignKey(orm[u'dopomoga.projectinneed'], null=False)),
            ('userinneedprofile', models.ForeignKey(orm[u'dopomoga.userinneedprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projectinneed_id', 'userinneedprofile_id'])

        # Adding model 'ProjectHelperComment'
        db.create_table(u'dopomoga_projecthelpercomment', (
            (u'comment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dopomoga.Comment'], unique=True, primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dopomoga.Project'])),
        ))
        db.send_create_signal(u'dopomoga', ['ProjectHelperComment'])

        # Adding model 'Cause'
        db.create_table(u'dopomoga_cause', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(default='/static/img/default.jpg', max_length=100, blank=True)),
        ))
        db.send_create_signal(u'dopomoga', ['Cause'])

        # Adding M2M table for field resources on 'Cause'
        m2m_table_name = db.shorten_name(u'dopomoga_cause_resources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cause', models.ForeignKey(orm[u'dopomoga.cause'], null=False)),
            ('resource', models.ForeignKey(orm[u'dopomoga.resource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cause_id', 'resource_id'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'dopomoga_review')

        # Deleting model 'UserInneedProfile'
        db.delete_table(u'dopomoga_userinneedprofile')

        # Removing M2M table for field projects_asked on 'UserInneedProfile'
        db.delete_table(db.shorten_name(u'dopomoga_userinneedprofile_projects_asked'))

        # Deleting model 'ProjectInneedReview'
        db.delete_table(u'dopomoga_projectinneedreview')

        # Deleting model 'ResourceComment'
        db.delete_table(u'dopomoga_resourcecomment')

        # Deleting model 'UserInneedComment'
        db.delete_table(u'dopomoga_userinneedcomment')

        # Deleting model 'Resource'
        db.delete_table(u'dopomoga_resource')

        # Deleting model 'Project'
        db.delete_table(u'dopomoga_project')

        # Removing M2M table for field resource on 'Project'
        db.delete_table(db.shorten_name(u'dopomoga_project_resource'))

        # Removing M2M table for field cause on 'Project'
        db.delete_table(db.shorten_name(u'dopomoga_project_cause'))

        # Deleting model 'CauseComment'
        db.delete_table(u'dopomoga_causecomment')

        # Deleting model 'Comment'
        db.delete_table(u'dopomoga_comment')

        # Deleting model 'ProjectInneedComment'
        db.delete_table(u'dopomoga_projectinneedcomment')

        # Deleting model 'ProjectHelperReview'
        db.delete_table(u'dopomoga_projecthelperreview')

        # Deleting model 'UserProfileComment'
        db.delete_table(u'dopomoga_userprofilecomment')

        # Deleting model 'ProjectHelper'
        db.delete_table(u'dopomoga_projecthelper')

        # Deleting model 'UserProfile'
        db.delete_table(u'dopomoga_userprofile')

        # Removing M2M table for field resources on 'UserProfile'
        db.delete_table(db.shorten_name(u'dopomoga_userprofile_resources'))

        # Removing M2M table for field causes on 'UserProfile'
        db.delete_table(db.shorten_name(u'dopomoga_userprofile_causes'))

        # Removing M2M table for field projects_supported on 'UserProfile'
        db.delete_table(db.shorten_name(u'dopomoga_userprofile_projects_supported'))

        # Deleting model 'ProjectInneed'
        db.delete_table(u'dopomoga_projectinneed')

        # Removing M2M table for field users_inneed on 'ProjectInneed'
        db.delete_table(db.shorten_name(u'dopomoga_projectinneed_users_inneed'))

        # Deleting model 'ProjectHelperComment'
        db.delete_table(u'dopomoga_projecthelpercomment')

        # Deleting model 'Cause'
        db.delete_table(u'dopomoga_cause')

        # Removing M2M table for field resources on 'Cause'
        db.delete_table(db.shorten_name(u'dopomoga_cause_resources'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dopomoga.cause': {
            'Meta': {'object_name': 'Cause'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/img/default.jpg'", 'max_length': '100', 'blank': 'True'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dopomoga.Resource']", 'null': 'True', 'blank': 'True'})
        },
        u'dopomoga.causecomment': {
            'Meta': {'object_name': 'CauseComment', '_ormbases': [u'dopomoga.Comment']},
            'cause': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dopomoga.Cause']"}),
            u'comment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Comment']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dopomoga.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'date_commented': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reports': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'dopomoga.project': {
            'Meta': {'object_name': 'Project'},
            'cause': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dopomoga.Cause']", 'symmetrical': 'False'}),
            'date_finished': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'funded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'how_to_help': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/img/default.jpg'", 'max_length': '100', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'project_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'reports': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'res_qnt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resource': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dopomoga.Resource']", 'symmetrical': 'False'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'dopomoga.projecthelper': {
            'Meta': {'object_name': 'ProjectHelper', '_ormbases': [u'dopomoga.Project']},
            u'project_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Project']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dopomoga.projecthelpercomment': {
            'Meta': {'object_name': 'ProjectHelperComment', '_ormbases': [u'dopomoga.Comment']},
            u'comment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Comment']", 'unique': 'True', 'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dopomoga.Project']"})
        },
        u'dopomoga.projecthelperreview': {
            'Meta': {'object_name': 'ProjectHelperReview', '_ormbases': [u'dopomoga.Review']},
            u'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Review']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dopomoga.projectinneed': {
            'Meta': {'object_name': 'ProjectInneed', '_ormbases': [u'dopomoga.Project']},
            'docs_descr': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'docs_pics': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'project_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Project']", 'unique': 'True', 'primary_key': 'True'}),
            'users_inneed': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dopomoga.UserInneedProfile']", 'null': 'True', 'blank': 'True'})
        },
        u'dopomoga.projectinneedcomment': {
            'Meta': {'object_name': 'ProjectInneedComment', '_ormbases': [u'dopomoga.Comment']},
            u'comment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Comment']", 'unique': 'True', 'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dopomoga.Project']"})
        },
        u'dopomoga.projectinneedreview': {
            'Meta': {'object_name': 'ProjectInneedReview', '_ormbases': [u'dopomoga.Review']},
            u'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Review']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dopomoga.resource': {
            'Meta': {'object_name': 'Resource'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/img/default.jpg'", 'max_length': '100', 'blank': 'True'})
        },
        u'dopomoga.resourcecomment': {
            'Meta': {'object_name': 'ResourceComment', '_ormbases': [u'dopomoga.Comment']},
            u'comment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Comment']", 'unique': 'True', 'primary_key': 'True'}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dopomoga.Resource']"})
        },
        u'dopomoga.review': {
            'Meta': {'object_name': 'Review'},
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictures': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/img/default.jpg'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dopomoga.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'dopomoga.userinneedcomment': {
            'Meta': {'object_name': 'UserInneedComment', '_ormbases': [u'dopomoga.Comment']},
            u'comment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Comment']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'dopomoga.userinneedprofile': {
            'Meta': {'object_name': 'UserInneedProfile', '_ormbases': [u'dopomoga.UserProfile']},
            'projects_asked': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dopomoga.ProjectHelper']", 'null': 'True', 'blank': 'True'}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'dopomoga.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'causes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dopomoga.Cause']", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/img/default.jpg'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'projects_supported': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dopomoga.ProjectInneed']", 'null': 'True', 'blank': 'True'}),
            'reports': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dopomoga.Resource']", 'null': 'True', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'dopomoga.userprofilecomment': {
            'Meta': {'object_name': 'UserProfileComment', '_ormbases': [u'dopomoga.Comment']},
            u'comment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dopomoga.Comment']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['dopomoga']