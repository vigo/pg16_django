# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.views.generic import ListView,\
                                 DetailView,\
                                 UpdateView,\
                                 CreateView,\
                                 DeleteView

from django.core.urlresolvers import reverse_lazy

from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'post-list.html'
    ordering = ['-published_at']
    queryset = Post.objects.filter(status=1)

class PostDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'

    def get_queryset(self):
        qs = super(PostDetail, self).get_queryset()
        return qs.filter(status=1, pk=self.kwargs.get('pk', None))


class PostUpdate(UpdateView):
    model = Post
    template_name = 'post-add-update.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('post-list')


class PostCreate(CreateView):
    model = Post
    template_name = 'post-add-update.html'
    fields = ['title', 'body', 'published_at']
    initial = {
        'published_at': datetime.datetime.now(),
    }
    success_url = reverse_lazy('post-list')


class PostDelete(DeleteView):
    model = Post
    template_name = 'post-check-delete.html'
    success_url = reverse_lazy('post-list')
