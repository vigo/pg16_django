# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

POST_STATUS = (
    (0, u"Kapalı"),
    (1, u"Yayında"),
)

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=POST_STATUS, default=1,)
    published_at = models.DateTimeField(verbose_name=u"Yayınlanma Tarihi")
    title = models.CharField(max_length=255, verbose_name=u"Başlık")
    body = models.TextField(verbose_name=u"Yazı")
    
    def get_delete_url(self):
        return reverse('post-delete', args=[self.pk])
    
    def get_edit_url(self):
        return reverse('post-update', args=[self.pk])
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk])
    
    def __unicode__(self):
        return u"%s" % self.title
