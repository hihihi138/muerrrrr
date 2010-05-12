# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from youku.models import Video
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def main_page(request):
    return video_list_page(request, 1)

def video_list_page(request, pid):
    try:
	pid = int(pid)
    except ValueError:
	raise Http404()
    videos = Video.objects.all()
    paginator = Paginator(videos, 5)
    if pid > paginator.num_pages: pid = paginator.num_pages
    video_list = videos[(5*(pid-1)):(5*pid)]
    page = paginator.page(pid)
    return render_to_response('index.html', locals())
