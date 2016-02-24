# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

POST_STATUS = (
    (0, u"Kapalı"),
    (1, u"Yayında"),
)

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=POST_STATUS, default=1,)
    published_at = models.DateTimeField()
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __unicode__(self):
        return u"%s" % self.title
