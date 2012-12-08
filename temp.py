# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        db_table = u'auth_group'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class ClinicsGrouping(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    parent = models.ForeignKey('self')
    info = models.TextField()
    contact_details = models.TextField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    class Meta:
        db_table = u'clinics_grouping'

class ClinicsServiceGroupings(models.Model):
    id = models.IntegerField(primary_key=True)
    service = models.ForeignKey(ClinicsService)
    grouping = models.ForeignKey(ClinicsGrouping)
    class Meta:
        db_table = u'clinics_service_groupings'

class ClinicsServicedescriptiontype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    order = models.IntegerField()
    class Meta:
        db_table = u'clinics_servicedescriptiontype'

class ClinicsServicedescription(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    service = models.ForeignKey(ClinicsService)
    service_description_type = models.ForeignKey(ClinicsServicedescriptiontype)
    class Meta:
        db_table = u'clinics_servicedescription'

class ClinicsAttachmenttype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    order = models.IntegerField()
    class Meta:
        db_table = u'clinics_attachmenttype'

class ClinicsService(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    description = models.TextField()
    modified_time = models.DateTimeField()
    class Meta:
        db_table = u'clinics_service'

class ClinicsAttachment(models.Model):
    id = models.IntegerField(primary_key=True)
    resource = models.CharField(max_length=100)
    description = models.CharField(max_length=80)
    attachment_type = models.ForeignKey(ClinicsAttachmenttype)
    modified_time = models.DateTimeField()
    service = models.ForeignKey(ClinicsService)
    class Meta:
        db_table = u'clinics_attachment'

class ReadcodesReadcodeSynonyms(models.Model):
    id = models.IntegerField(primary_key=True)
    readcode = models.ForeignKey(ReadcodesReadcode)
    term = models.ForeignKey(ReadcodesTerm)
    class Meta:
        db_table = u'readcodes_readcode_synonyms'

class ReadcodesHierarchy(models.Model):
    id = models.IntegerField(primary_key=True)
    read_code = models.ForeignKey(ReadcodesReadcode)
    parent_read_code = models.ForeignKey(ReadcodesReadcode)
    list_order = models.IntegerField()
    class Meta:
        db_table = u'readcodes_hierarchy'

class ReadcodesTerm(models.Model):
    term_id = models.CharField(max_length=6, primary_key=True)
    term_status = models.CharField(max_length=2)
    term_30 = models.CharField(max_length=40)
    term_60 = models.CharField(max_length=70)
    term_198 = models.CharField(max_length=210)
    class Meta:
        db_table = u'readcodes_term'

class ReadcodesKey(models.Model):
    id = models.IntegerField(primary_key=True)
    term_key = models.CharField(max_length=10)
    term_id = models.ForeignKey(ReadcodesTerm)
    key_type = models.CharField(max_length=1)
    class Meta:
        db_table = u'readcodes_key'

class ReadcodesStoredhierarchy(models.Model):
    id = models.IntegerField(primary_key=True)
    read_code = models.ForeignKey(ReadcodesReadcode)
    ancestor_codes = models.CharField(max_length=256)
    priority = models.IntegerField()
    class Meta:
        db_table = u'readcodes_storedhierarchy'

class CodebrowserBrowsepriority(models.Model):
    id = models.IntegerField(primary_key=True)
    readcode = models.ForeignKey(ReadcodesReadcode)
    priority = models.IntegerField()
    class Meta:
        db_table = u'codebrowser_browsepriority'

class ReadcodesReadcode(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    preferred_term = models.ForeignKey(ReadcodesTerm)
    concept_status = models.CharField(max_length=1)
    is_attribute = models.BooleanField()
    subject_type = models.ForeignKey('self')
    class Meta:
        db_table = u'readcodes_readcode'

class CodebrowserStoredhierarchy(models.Model):
    id = models.IntegerField(primary_key=True)
    read_code = models.ForeignKey(ReadcodesReadcode)
    ancestor_codes = models.TextField()
    priority = models.IntegerField()
    class Meta:
        db_table = u'codebrowser_storedhierarchy'

class ProblemsProblem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(ReadcodesReadcode)
    parent = models.ForeignKey('self')
    severity = models.CharField(max_length=1)
    activity = models.CharField(max_length=1)
    expiry = models.DateField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    class Meta:
        db_table = u'problems_problem'

class ProblemsNote(models.Model):
    id = models.IntegerField(primary_key=True)
    problem = models.ForeignKey(ProblemsProblem)
    subjective = models.TextField()
    objective = models.TextField()
    assessment = models.TextField()
    plan = models.TextField()
    class Meta:
        db_table = u'problems_note'

