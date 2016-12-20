# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    score1 = models.FloatField(default=0)
    score1_content = models.CharField(max_length=500, default='着装合理，治学严谨。严于律己，从不迟到早退')
    score1_count = models.IntegerField(default=0)

    score2 = models.FloatField(default=0)
    score2_content = models.CharField(max_length=500, default='教学认真，授课内容详细，课堂效率高')    
    score2_count = models.IntegerField(default=0)
    
    score3 = models.FloatField(default=0)
    score3_content = models.CharField(max_length=500, default='教学方法多样，重点与难点内容区分清楚，讲解得当')    
    score3_count = models.IntegerField(default=0)
    
    score4 = models.FloatField(default=0)
    score4_content = models.CharField(max_length=500, default='授课方式诙谐幽默，讲解深入浅出。')
    score4_count = models.IntegerField(default=0)

    score5 = models.FloatField(default=0)
    score5_content = models.CharField(max_length=500, default='采用多媒体辅助教学，制作的电子教案详略得当，效果好。')
    score5_count = models.IntegerField(default=0)

    score6 = models.FloatField(default=0)
    score6_content = models.CharField(max_length=500, default='强调独立思考，启发引导学生发现问题并解决问题。')
    score6_count = models.IntegerField(default=0)

    score7 = models.FloatField(default=0)
    score7_content = models.CharField(max_length=500, default='课堂气氛活跃，师生互动良好。')
    score7_count = models.IntegerField(default=0)

    score8 = models.FloatField(default=0)
    score8_content = models.CharField(max_length=500, default='在上课过程中会讲授做人的道理，帮助学生形成正确的人生观，关心学生成长。')
    score8_count = models.IntegerField(default=0)

    score9 = models.FloatField(default=0)
    score9_content = models.CharField(max_length=500, default='虚心接受学生的建议，能适时调整教学方法和进度，对学生不厌其烦，耐心讲解。')
    score9_count = models.IntegerField(default=0)

    score10 = models.FloatField(default=0)
    score10_content = models.CharField(max_length=500, default='认真批改作业，能及时准确的发现同学们存在的问题并加以解决。')
    score10_count = models.IntegerField(default=0)

    score_total = models.FloatField(default=0)
    tid = models.AutoField(primary_key=True)
    major = models.CharField(max_length=200, default='工学系')
    intro = models.TextField(default='个人简介，待补充')
    stars_filled = models.CharField(max_length=5, default='x')
    stars_empty = models.CharField(max_length=5, default='yyyy')

    def __str__(self):
        return self.name


