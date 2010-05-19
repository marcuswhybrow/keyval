from django.db import models
from django.contrib.auth.models import User

class KeyVal(models.Model):
    """A Key Value pair owned by a user"""
    
    user = models.ForeignKey(User, related_name='keyvals')
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Admin:
        list_display = ('user', 'key', 'value')
        search_fields = ('user', 'key', 'value')

    def __unicode__(self):
        return u"%s => %s" % (self.key, self.value)
