from django.db import models,DatabaseError
from readcodes.models import ReadCode
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class StoredHierarchy(models.Model):
    read_code = models.OneToOneField(ReadCode)
    ancestor_codes = models.TextField()
    priority = models.IntegerField()

class BrowsePriority(models.Model):
    readcode = models.OneToOneField(ReadCode)
    priority = models.IntegerField()
    
    
   
def get_ancestor_codes(code):
    try:
        return code.storedhierarchy.ancestor_codes
    except ObjectDoesNotExist:
        result = code.code
        for f in code.parents.all():
            result += ',' + get_ancestor_codes(f.parent_read_code)
        try:
            priority = code.browsepriority.priority
        except ObjectDoesNotExist:
            #update storedhierarchy if needed
            priority = min(100,code.parents.aggregate(models.Min('parent_read_code__storedhierarchy__priority')))
            s = StoredHierarchy(read_code = code,ancestor_codes = result, priority = priority)
            s.save()
        return result

def regenerate_stores():
    StoredHierarchy.objects.all().delete()
    i = 0
    for f in ReadCode.objects.all():
        get_ancestor_codes(f)
        i +=1
        if i % 100 ==0:
            print "%d codes re-organised" % i
