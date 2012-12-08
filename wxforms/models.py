from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Grouping(MPTTModel):
    name = models.CharField(max_length=80,unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    info = models.TextField(blank=True)
    contact_details = models.TextField(blank=True)
    app_label="clinics"
    module_name="Grouping"
    class Meta:
        app_label="clinics"
        ordering = ['tree_id', 'lft']

    def __unicode__(self):
        return self.name

    def get_path(self):
        return list(self.get_ancestors())+[self]

    @models.permalink
    def get_absolute_url(self):
        return('clinics.views.grouping',[self.name])

    def get_all_and_me(self):
        return self.get_ancestors(include_self=True)
        
    @staticmethod
    def get_all():
        return Grouping.objects.all()

class Service(models.Model):
    name = models.CharField(max_length=80,unique=True)
    description = models.TextField()
    groupings = models.ManyToManyField(Grouping,null=True)
    modified_time = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return('clinics.views.service',[self.name])

    def get_descriptors(self):
        return self.servicedescription_set.order_by('service_description_type')

    def get_files(self):
        return self.attachment_set.order_by('attachment_type')

class ServiceDescriptionType(models.Model):
    name = models.CharField(max_length=40)
    order = models.IntegerField(blank = True, null = True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering=('order',)

class ServiceDescription(models.Model):
    description = models.CharField(max_length=500)
    service = models.ForeignKey(Service)
    service_description_type = models.ForeignKey(ServiceDescriptionType)
    def __unicode__(self):
        return self.description

class AttachmentType(models.Model):
    name = models.CharField(max_length = 80)
    order = models.IntegerField(blank = True, null = True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering=('order',)

class Attachment(models.Model):
    def upload_destination(instance,filename):
        return instance.service.name+'/'+filename
    resource = models.FileField(upload_to=upload_destination)
    description = models.CharField(max_length=80)
    attachment_type = models.ForeignKey(AttachmentType)
    modified_time = models.DateTimeField(auto_now=True)
    service = models.ForeignKey(Service)
    def __unicode__(self):  
        return self.description

    


# Create your models here.
