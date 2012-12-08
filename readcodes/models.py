from django.db import models


# Create your models here.
class Term(models.Model):
    STATUS_CHOICES = (
        ('C','Current'),
        ('O','Obsolete'),
    )
    term_id = models.CharField(max_length = 6,primary_key = True)
    term_status = models.CharField(max_length = 2,choices = STATUS_CHOICES)
    term_30 = models.CharField(max_length = 40)
    term_60 = models.CharField(max_length = 70,null=True,blank=True)
    term_198 = models.CharField(max_length = 210,null=True,blank=True)
    
    def get_term_198(self):
        if self.term_198!="":
            return self.term_198
        if self.term_60!="":
            return self.term_60
        return self.term_30

    def get_term_60(self):
        if self.term_60!="":
            return self.term_60
        return self.term_30

    def get_term_30(self):
        return self.term_30
    
    def __unicode__(self):
        return self.get_term_60()
        
        
class ReadCode(models.Model):
    CONCEPT_CHOICES = (
        ('C','Current'),
        ('O','Obsolete'),
        ('R','Redundant'),
        ('E','Extinct'),
    )
    code = models.CharField(max_length = 6, primary_key = True)
    preferred_term = models.ForeignKey(Term,related_name="primary_read_codes")
    synonyms = models.ManyToManyField(Term,related_name="read_codes")
    concept_status = models.CharField(max_length = 1,choices = CONCEPT_CHOICES)
    is_attribute = models.BooleanField()
    subject_type = models.ForeignKey('self',related_name="subject_type_set")
    hierarchy = models.ManyToManyField('self',symmetrical = False, through = 'Hierarchy',related_name='+')
    
    def __unicode__(self):
        return "%s [%s]" % (self.preferred_term.__unicode__(),self.code)
        
    def get_extra_synonyms(self):
        return self.synonyms.exclude(term_id=self.preferred_term.term_id)
        
class Hierarchy(models.Model):
    read_code = models.ForeignKey(ReadCode,related_name='parents')
    parent_read_code = models.ForeignKey(ReadCode,related_name='children')
    list_order = models.IntegerField()    
    
    
class Key(models.Model):
    KEY_CHOICES = (
        ('P','Partial'),
        ('W','Whole word'),
        ('A','Abbreviation'),
    )
    term_key = models.CharField(max_length = 10)
    term_id = models.ForeignKey(Term)
    key_type = models.CharField(max_length = 1,choices = KEY_CHOICES)
    

