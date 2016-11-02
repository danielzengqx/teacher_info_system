from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField()
    tid = models.IntegerField()
    major = models.CharField(max_length=200)

    def __str__(self):
        return self.name