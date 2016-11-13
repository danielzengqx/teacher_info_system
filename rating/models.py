# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    score1 = models.IntegerField(default=10)
    score1_content = models.CharField(max_length=500, default='着装合理，治学严谨。严于律己，从不迟到早退')
    score2 = models.IntegerField(default=10)
    score2_content = models.CharField(max_length=500, default='教学认真，授课内容详细，课堂效率高')    
    score3 = models.IntegerField(default=10)
    score3_content = models.CharField(max_length=500, default='教学方法多样，重点与难点内容区分清楚，讲解得当')    
    score4 = models.IntegerField(default=10)
    score4_content = models.CharField(max_length=500, default='评分内容4')
    tid = models.CharField(max_length=20)
    major = models.CharField(max_length=200)
    intro = models.TextField(default='个人简介，待补充')

    def __str__(self):
        return self.name