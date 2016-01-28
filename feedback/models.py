#!/usr/bin/python
# vim: set fileencoding=utf-8 :
from django.db import models
from wechat_member.models import Member

class Feedback(models.Model):
    TYPE_CHOICES = (
        ('bug', '错误'),
        ('suggestion', '建议'),
        ('other', '随便说说'),
    )
    member = models.ForeignKey(Member, related_name='feedbacks', verbose_name='会员')
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, verbose_name='类型')
    content = models.TextField(verbose_name='内容')
    is_view = models.BooleanField(default=False, verbose_name='是否查阅')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.content

    class Meta(object):
        verbose_name = '反馈意见'
        verbose_name_plural = '反馈意见'
