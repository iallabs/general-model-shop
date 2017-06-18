from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='aw3aa')
    

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
