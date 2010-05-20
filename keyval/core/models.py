from django.db import models
from django.contrib.auth.models import User

class KeyVal(models.Model):
    """A Key Value pair owned by a user"""
    
    user = models.ForeignKey(User, related_name='keyvals')
    key = models.CharField(max_length=100, db_index=True)
    value = models.CharField(max_length=100)

    class Admin:
        list_display = ('user', 'key', 'value')
        search_fields = ('user', 'key', 'value')
    
    class Meta:
        unique_together = ('user', 'key')

    def __unicode__(self):
        return u"%s => %s" % (self.key, self.value)
    
    @models.permalink
    def get_absolute_url(self):
        return ('keyval_profile', (), {
            'username': self.user.username,
            'key': self.key,
        })
